from time import sleep, perf_counter

def task():
    print('Starting a task...')
    sleep(1)
    print('done')

# start_time = perf_counter()
# task()
# task()
# end_time = perf_counter()
# print(end_time - start_time)

from threading import Thread
start_time = perf_counter()
t1 = Thread(target=task)
t2 = Thread(target=task)
t1.start()
t2.start()
t1.join()
t2.join()
end_time = perf_counter()
print(end_time - start_time)