
# decorator ---> 

def decorator(func):
    def wrapper_function(*args, **kwargs):

        print('Start....')
        func(*args, **kwargs)
       

    return wrapper_function



@decorator      # call decorator
def sum(x,y):
    print(x+y)


sum(4,7)