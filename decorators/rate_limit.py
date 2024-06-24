"""Rate limitting ensures that a function is called a maximum number of times within a specified time window. 
This can be useful for controlling access to APIs, preventing abuse, or managing resource usage.
"""

import time 
from functools import wraps


def rate_limit(max_calls=5, period=60):
    """Ensure that a function is called at most `max_calls` times per `period` window.
    """

    def decorator(func):
        call_times = []     # This is initialized when define the @ operator

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_times

            now = time.time()
            call_times.append(now)

            # Remove call times older than 'period' seconds 
            call_times = [t for t in call_times if t > (now - period)]    # time - interval

            if len(call_times) <= max_calls:
                return func(*args, **kwargs)
            else:
                raise Exception(f"Rate limit exceeded. Maximum {max_calls} calls allowed in {period} seconds.") 
            
        return wrapper

    return decorator

    
if __name__ == "__main__":
    @rate_limit(max_calls=3, period=10)
    def api_call():
        print("API call executed successfully.")

    # Simulate API calls
    for _ in range(5):             # this will fail at the 4th attempt because of rate limit
        api_call()
        time.sleep(2)
