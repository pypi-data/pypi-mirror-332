import threading
import functools
from concurrent.futures import Future
#Saving Threads.
threads = []
def multithread(func):
    """Multi-Thread Func, One-Thread Per wrap."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        threads.append(thread)
        thread.start()
    return wrapper
def multithread_return(func):
    """ Decorate returns values. """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        future = Future()

        def run():
            try:
                result = func(*args, **kwargs)
                future.set_result(result)
            except Exception as e:
                future.set_exception(e)

        thread = threading.Thread(target=run)
        threads.append(thread)
        thread.start()
        return future

    return wrapper

def wait_for_threads():
    """ Asyncing all threads before End-thread. """
    for thread in threads:
        thread.join()
    threads.clear()