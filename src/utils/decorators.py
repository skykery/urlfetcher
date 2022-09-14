import time
from functools import wraps


def retry(exceptions, retries=4, delay=3, backoff_multiplier=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    :param exceptions: the exception to check. may be a tuple of
        exceptions to check
    :type exceptions: Single Exception or tuple
    :param retries: number of times to try (not retry) before giving up
    :type retries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff_multiplier: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff_multiplier: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """

    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = retries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except exceptions as exc:
                    msg = f"{exc}, Retrying in {delay} seconds..."
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff_multiplier
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry
