from typing import NewType 


UserId = NewType('UserId', int)    # the new class is of type 'int'
some_id = UserId(12345)

print(some_id)
print(type(some_id))   
print('-' * 50)

def get_user_name(user_id: UserId) -> str: 
    ...

# Pass type checking 
user_a = get_user_name(UserId(12345))
print(user_a)

# Fails type checking: an int is not a UserId 
user_b = get_user_name(-1)
print(user_b)
    