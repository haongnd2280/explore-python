"""Try to implement functions that may fail due to transient errors, 
such as network timeouts or temporary resoure unavailability. 
"""

import time 
import random 
from functools import wraps 


def retry(max_entries=3, delay=1): 
    """Automatically retry a function call a certain number of times 
    with a delay between entries. 
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attemps = 0 
            while attemps < max_entries:
                try: 
                    return func(*args, **kwargs)
                except Exception as e: 
                    print(f"Attemp {attemps + 1}/{max_entries} failed: {e}")
                    attemps += 1 
                    time.sleep(delay)

            # The below command will be executed if the above return command is not executed
            raise Exception(f"Failed after {max_entries} attempts.")
        
        return wrapper
    return decorator


@retry(max_entries=5, delay=2)
def connect_to_server():
    """Simulated function that may fail intermittently.
    """

    if random.random() < 0.3:    # Simulate 30% failure rate 
        raise ConnectionError("Connection timed out.")      # user-defined error 
    else: 
        print("Connected successfully.")

# Call the function 
connect_to_server()
    