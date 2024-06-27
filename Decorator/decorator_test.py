
# decorator =  decorator is a design pattern in Python that allows a user to 
# add new functionality to an existing object without modifying its structure

import datetime

def decorator(func):
    def wrapper_function(*args, **kwargs):

        print('Start....')
        func(*args, **kwargs)
        print(datetime.datetime.now())
        print("End decoratro")

    return wrapper_function



@decorator   # call decorator
def sum(x,y):
    print(x+y)

sum(4,7)



'''
examples for decorator:

login_required
permission_required
cache
'''