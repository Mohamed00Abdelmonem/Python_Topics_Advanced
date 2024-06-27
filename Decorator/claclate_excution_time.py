import time

def claclte_excution_time(func):
    def wrapper_function(*args, **kwargs):

        print('start excute ...')
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'excute time {end_time- start_time}')
        print('end excute ... ')

    return wrapper_function
    

    
@claclte_excution_time
def myfunc():
    time.sleep(5)


myfunc()