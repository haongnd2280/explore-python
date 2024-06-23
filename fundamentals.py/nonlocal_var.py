def my_func1():
    name = "haongnd"

    def my_func2():
        nonlocal name      # use the variable in the outer function
        name = "ndhao"     # assign new value to name

    my_func2()             # execute the inner function
    return name 


if __name__ =='__main__':
    name = my_func1()
    print(name)


