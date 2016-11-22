import pstats
import tempfile
import cProfile
import timeit
import time
from cmd_profile import main
from cmd_profile import light
from cmd_profile import heavy


def profile(column='time',list='5'):
    def _profile(function):
        def __profile(*args,**kw):
            s = tempfile.mktemp()
            profiler = cProfile.Profile()
            profiler.runcall(function,*args,**kw)
            profiler.dump_stats(s)
            p = pstats.Stats(s)
            p.sort_stats(column).print_stats(list)

        return __profile
    return _profile


timer = time.time
stats = {}
def duration(name='stats',stats=stats):
    def _duration(function):
        def __duration(*args,**kw):
            start_time = timer()
            try:
                return function(*args,**kw)
            finally:
                stats[name] = timer() - start_time
        return __duration
    return _duration

@profile('time',7)
def main_profiled():
    return main()


main_profiled()
p = profile()(light)
print p()


profiler = cProfile.Profile()
profiler.runcall(main)
profiler.print_stats()


cProfile.run('main()','study.stats')
p = pstats.Stats('study.stats')
print p.total_calls
print p.sort_stats('time').print_stats(3)
print p.print_callers('heavy')


t = timeit.Timer('main()')
print t.timeit(number=10)




h = duration('this_func_is')(heavy)
heavy()
print stats['this_func_is']