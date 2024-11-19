from typing import Any 


a: Any = None 
a = []      # OK 
a = 2       # OK 

s: str = ''
s = a       # OK: no checking when assigning a value of type Any to a more precise type. 

def foo(item: Any) -> int: 
    """Passes type checking, 'item' could be any type.
    """
    item.bar()     # that type might have a 'bar' method (or not)


# All functions without a return type or parameter types will implicitly default to using Any 
def legacy_parser(text): 
    ...
    return data 

# A static type checker will treat the above functions as having the same signature as: 
def legacy_parser(text: Any) -> Any: 
    ...
    return data 

