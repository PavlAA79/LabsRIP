from contextlib import contextmanager
import time

@contextmanager
def cm_timer_1():
    start_time = time.clock()
    yield 
    print ('time: ',time.clock()-start_time)

class Cm_Timer_2:

    def __init__(self):
        self.all_time = 0
        
    def __enter__(self):
        self.all_time = time.clock()
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            self.all_time = time.clock()-self.all_time
            print ('time: ',self.all_time)

def main():
    print('Задание 6:')
    print('cm_timer_1:')
    with cm_timer_1(): 
        try:
            time.sleep(5.5)
        except:
            pass
    print('Cm_timer_2:')
    try:
        with Cm_Timer_2() as cm_object:
            time.sleep(5.5)
    except:
            pass
if __name__ == "__main__":
    main()