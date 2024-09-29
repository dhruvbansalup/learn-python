import time

# Basic implementation
class TimerA:
    def __itit__(self):
        self._start_time=0
        self._elapsed_time=0

    def start(self):
        self._start_time=time.perf_counter()
    
    def stop(self):
        self._elapsed_time=time.perf_counter()-self._start_time
    
    def elapsed(self):
        return(self._elapsed_time)
    


# MORE ELABORATION
class TimerError(Exception):
    """A custom exception used to report error in use of timer class"""
class Timer:
    def __init__(self):
        self._start_time=None
        self._elapsed_time=None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop()")
        self._start_time=time.perf_counter()
    
    def stop(self):
        """Save the elapsed time and re-initialize timer"""
        if self._start_time is None:
            raise TimerError("Timer not running. Use .start()")
        self._elapsed_time=time.perf_counter()-self._start_time
        self._start_time=None
    
    def elapsed(self):
        """Report elapsed time"""
        if self._elapsed_time is None:
            raise TimerError("Timer is not running. Use .start()")
        return (self._elapsed_time)
    
    def __str__(self)->str:
        """print() prints elapsed time"""
        return(str(self._elapsed_time))
    


t=Timer()
for j in range(4,9):
    t.start()
    n=0
    for i in range(10**j):
        n=n+i
    t.stop()
    print(j,t,sep=": ")