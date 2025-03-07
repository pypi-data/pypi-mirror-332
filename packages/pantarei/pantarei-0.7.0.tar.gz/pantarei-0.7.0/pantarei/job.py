"""
Job
"""
import os
import time
import inspect
import dill
import subprocess

from . import core
from . import task
from .scheduler import Scheduler
from .helpers import mkdir, serialize_kwargs, rmd

class JobFailure(Exception):
    """Exception raised when a failed job is found in the session"""
    pass

def _load_yaml(path):
    with open(path) as fh:
        db = {}
        for line in fh:
            key, value = line.split(':')
            db[key] = value
    return db


_stack_index = -1

class Job:

    """
    Batch execution on distibuted memory environment (ex. scheduler)
    """

    mode = core.mode

    def __init__(self, task_or_func, tag="", scheduler=None, cores=1, wall_time=None,
                 output=None, error=None, memory=None,
                 **kwargs):
        """
        :param task_or_func: the `Task` or function to execute
        :param tag: string to identify the task, relevant if task_or_func is a `Task`
        :param scheduler: the scheduler to usel if `None` it will be auto-detected
        :param cores: number of cores to use
        :param wall_time: the maximum wall time
        :param memory: requested memory (RAM)
        :param output: output file
        :param error: error file
        """
        if not isinstance(task_or_func, task.Task):
            task_or_func = task.Task(task_or_func, tag=tag)
        self.task = task_or_func
        self.scheduler = scheduler
        self.cores = cores
        self.wall_time = wall_time
        self.memory = memory
        self.output = output
        self.error = error
        # Arguments for task (as keyword arguments only)
        self.kwargs = kwargs
        if self.scheduler is None:
            from .core import scheduler
            self.scheduler = scheduler

    @property
    def path(self):
        """Path to the cache of the job"""
        return os.path.join(self.task.cache.path, self.qualified_name())

    def name(self):
        """General name of job (independent of arguments)"""
        return self.task.name(**self.kwargs)

    def qualified_name(self):
        """Unique name of job"""
        return self.task.qualified_name(**self.kwargs)

    def pretty_name(self):
        """Pretty printed name of job (with args)"""
        args = []
        for key in self.kwargs:
            if self.task.ignore is not None:
                if key in self.task.ignore:
                    continue
            if isinstance(self.kwargs[key], str):
                args.append(f'{key}="{self.kwargs[key]}"')
            else:
                args.append(f'{key}={self.kwargs[key]}')
        kwargs = ','.join(args)
        return f'{self.task.name()}({kwargs})'

    def clear(self, **kwargs):
        """Clear undelrying task and its artifacts"""
        self.task.clear(self.task, **kwargs)
        # Clear job artifacts too
        rmd(self.path)

    # TODO: drop?
    def done(self, **kwargs):
        """Return True is Job is done"""
        # TODO: add condition on job execution
        if hasattr(self.task, 'done'):
            return self.task.done(**kwargs)
        return False

    @property
    def artifacts(self):
        """Job artifacts, possibly as a sequence"""
        return self.task.artifacts(**self.kwargs)

    @property
    def duration(self):
        """Current duration of job. If job is ended, return the elapsed duration"""
        import datetime
        job_file = os.path.join(self.path, 'job.yaml')
        if not os.path.exists(job_file):
            return datetime.timedelta(seconds=0)

        db = _load_yaml(job_file)
        if 'job_start' in db and 'job_end' in db:
            delta = float(db['job_end']) - float(db['job_start'])
        elif 'job_start' in db and 'job_fail' in db:
            delta = float(db['job_fail']) - float(db['job_start'])
        elif 'job_start' in db:
            delta = time.time() - float(db['job_start'])
        else:
            delta = 0
        return datetime.timedelta(seconds=int(delta))

    @property
    def state(self):
        """
        State of job.

        Possible values:
        - failed
        - ended
        - running
        - queued
        - unknown
        """
        job_file = os.path.join(self.path, 'job.yaml')
        if not os.path.exists(job_file):
            return ''
        else:
            db = _load_yaml(job_file)
            if 'job_fail' in db:
                return 'failed'
            elif 'job_end' in db:
                return 'ended'
            elif 'job_start' in db:
                # return 'started'
                return 'running'
            elif 'job_queue' in db:
                return 'queued'
            elif len(db) == 0:
                return 'unknown'
            else:
                raise ValueError(f'wrong state {list(db.keys())} in {self.path}')

    def __call__(self, **kwargs):
        # If no arguments are passed than we assume they were passed
        # to the constructor
        if len(kwargs) > 0:
            self.kwargs = kwargs

        # Add this job qname to global list
        from pantarei import core
        core.jobs.append(self.qualified_name())

        # This is not properly done atm, but it should work. The
        # point is that without the line below, when the task is not
        # done, the wrapped job will not store its path anywhere, and
        # will be missing. Jobs that are not ended would be phantom
        from . import core
        core._tasks.append(self.task.cache._storage(self.qualified_name()))

        # Check again
        assert self.mode in ['safe', 'brave', 'dry']

        # This was at the end, matching safe + ended
        # elif self.task.done(**self.kwargs):
        #     return self.task(**self.kwargs)

        # The execution modes are mutually exclusive, we check each
        # one independent of the others. This leads to some
        # redundance, but the switch will be more robust.
        results = None

        if self.mode == 'dry':
            # Get the results right away if done, but do not submit.
            # We do not do anything with failed jobs.
            if self.task.done(**self.kwargs):
                results = self.task(**self.kwargs)

        elif self.mode == 'safe':
            # Get the results right away if done, else submit,
            # but stop at the first failure
            if self.task.done(**self.kwargs):
                results = self.task(**self.kwargs)
            elif self.state == 'failed':
                raise JobFailure(f'stop because of previous job failure {self.qualified_name()}')
            elif self.state in ['running', 'queued'] or self.scheduler.queued(self.qualified_name()):
                # If job is running or queued (ex. on a remote cluster), do nothing
                pass
            else:
                self._submit()

        elif self.mode == 'brave':
            # In brave mode we skip failed jobs
            if self.task.done(**self.kwargs):
                results = self.task(**self.kwargs)
            elif self.state == 'failed':
                # TODO: this should only be done if there are no deps
                print(f'WARNING: skipping failed job {self.qualified_name()}')
            elif self.state in ['running', 'queued'] or self.scheduler.queued(self.qualified_name()):
                # If job is running or queued (ex. on a remote cluster), do nothing
                pass
            else:
                self._submit()

        # We reset the arguments if they were passed to __call__
        if len(kwargs) > 0:
            self.kwargs = {}

        return results

    def _submit(self):
        import dill
        
        # dirname = os.path.join(self.task.cache.path, self.qualified_name())
        mkdir(self.path)
        session_pkl = os.path.join(self.path, '.session.pkl')
        context_pkl = os.path.join(self.path, '.context.pkl')
        job_state = os.path.join(self.path, 'job.yaml')
        job_output = os.path.join(self.path, 'job.out')
        kwargs = serialize_kwargs(self.kwargs)

        n = _stack_index
        n = -2  # for
        # s = stacks[n]
        stacks = inspect.stack()
        s = stacks[n]
        for n in range(len(stacks)-1, -1, -1):
            if 'job' in stacks[n].frame.f_locals:
                s = stacks[n]
                # print('FOUND', n)
                # from .helpers import debug_stacks
                # debug_stacks([s])
                break

        # Fix issues with emacs python shell execution
        # This should not be needed anymore
        # var = s.frame.f_locals
        # if '__pyfile' in var:
        #     # s = stacks[-2]
        #     s = stacks[n - 1]
        #     garbage = var.pop('__pyfile')
        #     del garbage

        # Attempt to clear the imported module session for pickling
        # var = s.frame.f_locals
        # if '__builtins__' in var:
        #     for clear in ['__builtins__', '__cached__']:
        #         garbage = var.pop(clear)
        #         del garbage
        #         var['__cached__'] = None
        #         var['__name__'] = '__main__'
        #         var['__package__'] = None
        #         var['__spec__'] = None

        # from pprint import pprint
        # print('local')
        # pprint(s.frame.f_locals)
        # print('global')
        # pprint(s.frame.f_globals.keys())

        
        # pprint.pprint(s.frame.f_locals)
        # pprint.pprint(s.frame.f_globals)

        # Store session and local context separately.
        # The session stores all objects in the module of the frame
        # containing the job instance
        probls_objs = ['__pyfile', '_ih', '_oh', '_dh', 'In', 'Out',
                       'get_ipython', 'exit', 'quit',
                       '__session__', '_i', '_ii', '_iii', '_i1']
        for f in probls_objs:
            probls = {}
            if f in s.frame.f_globals:
                probls[f] = s.frame.f_globals.pop(f)
            
        dill.dump_module(session_pkl, module=inspect.getmodule(s.frame.f_code),
                         refimported=True)
        # Check if it works, otherwise it makes no sense to submit
        dummy = dill.load_module_asdict(session_pkl)
        
        # The context session stores the job instance itself
        # to cover the case in which this is defined in a function
        from types import ModuleType
        context = ModuleType('context')
        # context.__dict__.update(s.frame.f_globals)
        # args = s.frame.f_locals
        # import pprint
        # pprint.pprint(s.frame.f_locals)
        # pprint.pprint(s.frame.f_globals)
        # context.__dict__.update(s.frame.f_globals)
        context.job = s.frame.f_locals['job']
        # TODO: query cannot be pickled in context? How come, we only have job here...
        # print('query' in s.frame.f_globals)
        # print('query' in s.frame.f_locals)
        # Nothing of this works
        # query = s.frame.f_globals.pop('query')
        # del query
        # s.frame.f_locals.pop('query')

        # Here we get warnings sometimes:
        # dill.py:1087: PicklingWarning: Cannot pickle __main__.f has
        # recursive self-references that trigger a RecursionError.
        # However, the dumped context works well, so it is not clear
        # that this is really an issue. The origin of the warning is unclear:
        # there are no self-references in the function.
        # For the time being, we silence these warnings.
        # One day we will perhaps understand what is going on.

        # import dill.detect
        # with dill.detect.trace():
        #     dill.dump_module(context_pkl, module=context, refimported=True)
        dill.dump_module(context_pkl, module=context, refimported=True)
        import warnings
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=dill.PicklingWarning)
            dill.dump_module(context_pkl, module=context, refimported=True)
        # except TypeError:
        #     # Empty module when pickling fails. This is rather drastic
        #     # and currently prevents jobs in functions within jupyter
        #     context = ModuleType('context')
        #     dill.dump_module(context_pkl, module=context, refimported=True)
        # Check if it works, otherwise it makes no sense to submit
        dummy = dill.load_module_asdict(session_pkl)
        # from .helpers import debug_stacks
        # debug_stacks(stacks)

        # Finally restore problematic objects in the original frame
        for key in probls:
            s.frame.f_globals[key] = probls[key]
            
        # TODO: at the line of the called there should be a Job instance
        # else it
        # for s in stacks[:0:-1]:
        #     print(s.frame, s.frame.f_lineno, s.frame.f_code.co_name)
        #     #print(s.frame.f_code)
        #     j = s.frame.f_lineno - s.frame.f_code.co_firstlineno
        #     src, _ = inspect.getsourcelines(s.frame.f_code)
        #     found = False
        #     for i, l in enumerate(src):
        #         if i == j:
        #             if l.strip().startswith('job('):
        #                 print(i, l.strip())
        #                 found = True
        #             break
        #     if found:
        #         break
        # print(s.frame.f_locals)
        # https://stackoverflow.com/questions/1253528/is-there-an-easy-way-to-pickle-a-python-function-or-otherwise-serialize-its-cod
        # TODO: process the calling line to get the job object instead of hardcoding job
        script = f"""\
#!/usr/bin/env -S python -u
__name__ = '__main__'
import sys
import os
import time
import signal
import dill
sys.path.append('.')

run = True

def handler_stop_signals(signum, frame):
    global run
    run = False
    raise RuntimeError('received SIGINT/SIGTERM')

signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)

while True:
    if os.path.exists('{job_state}'): break

hostname = 'unknown'
if 'HOSTNAME' in os.environ:
    hostname = os.environ['HOSTNAME']

# We must unset the env variables else we get a report at the end
if 'pantarei' in os.environ:
    del os.environ['pantarei']
if 'pantarei_report' in os.environ:
    del os.environ['pantarei_report']
# print('mode', 'pantarei' in os.environ)
# print('report', 'pantarei_report' in os.environ)

fh = open('{job_state}', 'a')
print('job_node:', hostname, file=fh, flush=True)
print('job_start:', time.time(), file=fh, flush=True)

try:
    dill.load_module('{session_pkl}')

    context = dill.load_module('{context_pkl}')
    # print('context', context.job)
    context.job.task({kwargs})

    #import pprint
    #pprint.pprint(locals())
    #pprint.pprint(globals())
    #print()
    #pprint.pprint(context.__dict__)
    
except:
    print('job_fail:', time.time(), file=fh, flush=True)
    raise
else:
    print('job_end:', time.time(), file=fh, flush=True)
finally:
    fh.close()
    # Remove session data when job is over
    os.remove('{session_pkl}')
    os.remove('{context_pkl}')
"""
        self.scheduler.submit(script, self.qualified_name(), job_output=job_output,
                              job_error=None, wall_time=self.wall_time,
                              memory=self.memory)

        # Job is queued
        if self.scheduler is not None:
            with open(f'{job_state}', 'w') as fh:
                print('job_queue:', time.time(), file=fh, flush=True)
