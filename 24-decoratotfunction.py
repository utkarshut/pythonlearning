
def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args,**kwargs):
            print('executed brfore',original_function.__name__)
            result = original_function(*args,**kwargs)
            print(('executed after',original_function.__name__))
            return result
        return wrapper_function
    return  decorator_function


@prefix_decorator('log:')
def display_infor(name, age):
    print('display {}{}'.format(name,age))


display_infor('john',23)