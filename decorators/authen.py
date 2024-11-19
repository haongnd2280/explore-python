from functools import wraps 


# Simulated user authentication 
current_user = None 
ADMIN = {
    'user_name': 'admin', 
    'password': '123456'
}

def login(user_name, password):
    # Simulated user authentication logic 
    global current_user

    # For demonstration, only admin user can login
    if user_name == ADMIN['user_name'] and password == ADMIN['password']: 
        current_user = ADMIN['user_name']
        return True 

    return False 

def logout(): 
    # Simulated user logout logic 
    global current_user
    current_user = None 

def require_authentication(func): 
    """The function to be executed need to be authenticated first. 
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user: 
            return func(*args, **kwargs)
        else: 
            return "Access denied. Please log in."
        
    return wrapper 

# Example that requires authentication
@require_authentication
def view_profile():
    return f"Welcom, {current_user}!"

print(view_profile())       # Access denied because not log in yet 
login('admin', '123456')    # Login successfully 
print(view_profile())       # Sucessful 
print('-' * 50)

# Authorization: only admin can do the task 
def require_role(role: str): 
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user and current_user == role: 
                return func(*args, **kwargs)
            else: 
                return f"Access denied. Role {role} required."
        
        return wrapper 
    
    return decorator

@require_role('admin')
def delete_user(user_name): 
    return f"User {user_name} deleted successfully."

print(delete_user("user123"))  
print('-' * 50)

# Log out
logout()

print(view_profile())   # Access denied because already logged out 






