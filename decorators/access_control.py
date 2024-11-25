# Access control dựa vào role: chỉ có một vài role mới được thực hiện một số quyền nhất định. 
# Ví dụ: chỉ có role admin mới có quyền xóa user.

from functools import wraps

# Simulate the current user
current_user = {
    "username": "haongnd",
    "role": "viewer",
}

def requires_role(role):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_role = current_user.get("role")
            if current_role == role:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"Access denied. Required role: {role}. Curent role: {current_role}.")
        
        return wrapper
    
    return decorator


if __name__ == "__main__":
    @requires_role("admin")          # This returns the decorator function
    def delete_user(user_id):        # This returns the wrapper function
        ...
        print(f"User {user_id} has been deleted.")

    @requires_role("viewer")
    def view_dashboard():
        print("Dashboard accessed.")
        ...

    # Execution
    view_dashboard()     # OK
    delete_user(1234)    # PermissionError