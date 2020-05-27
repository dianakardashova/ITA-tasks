import functools
import time
import requests


def timer(func):
    """Prints the runtime of the decorated function."""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('Finished {} in run_time: {}'.format(func.__name__, run_time))
        return value
    return wrapper_timer


@timer
def fetch_webpage(url: str):
    """Send request to the server and return its encoding."""
    try:
        response = requests.get(url, timeout=0.1)
        response.raise_for_status()
    except requests.Timeout as err:
        """The request timed out."""
        print(err)
    except requests.ConnectionError as err:
        """The request timed out while trying to connect to the remote server."""
        print(err)
    except requests.HTTPError as err:
        """An HTTP error occurred."""
        print(err)
    except requests.RequestException as err:
        """There was an ambiguous exception that occurred while handling your request."""
        print(err)
    else:
        return response.encoding

def main():
    url = input('Enter URL: ')
    print(fetch_webpage(url))


if __name__ == '__main__':
    main()

