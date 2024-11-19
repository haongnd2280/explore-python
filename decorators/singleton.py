"""The singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.
If a class already has an instance, if we initialize that class again, it will not be initialized (regardless of the same of diff init parameters).
"""

from functools import wraps


def singleton(cls_):
    """Accept a class definition instead of a function definition.
    """

    instances = {}

    @wraps(cls_)
    def get_instance(*args, **kwargs):
        """The arguments is for the __init__ method of the class.
        """

        if cls_ not in instances:
            instances[cls_] = cls_(*args, **kwargs)    # initialize that class instance

        return instances[cls_]
    
    return get_instance


if __name__ == "__main__":
    @singleton
    class DatabaseConnection:
        def __init__(self, connection_string):
            self.connection_string = connection_string

    # Test the singleton
    db1 = DatabaseConnection("mysql://user:password@localhost/db")         # first create the DatabaseConnection instance
    db2 = DatabaseConnection("postgresql://user:password@localhost/db")    # this is not initialized because an instance alreay exists
    print(db1 is db2)                  # (compare the identity) True 
    print(db1.connection_string)       # mysql://user:password@localhost/db
    print(db2.connection_string)       # still MySQL

    print(db1.__doc__)





