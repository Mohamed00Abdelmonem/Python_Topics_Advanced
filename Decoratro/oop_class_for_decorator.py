
# So I used (oop) inhertance classes  instead of decoratro functionss
from datetime import datetime

class Decorator():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Start...')
        print(self.func(3,4))
        print(datetime.now())


@Decorator   # call decorator
def sum(x,y):
    return(x+y)


sum(4,7)        