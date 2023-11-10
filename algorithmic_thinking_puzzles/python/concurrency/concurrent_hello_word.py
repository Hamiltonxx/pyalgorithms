import itertools
import time 
from threading import Thread, Event 

def spin(msg, done):
    for char in itertools.cycle('\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    print(f'\r{" " * len(status)}\r', end='')

def slow():
    time.sleep(3)
    return 42

def supervisor():
    done = Event()
    spinner = Thread(target=spin, args=('thinking!',done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

if __name__ == '__main__':
    result = supervisor()
    print(f'Answer: {result}')
