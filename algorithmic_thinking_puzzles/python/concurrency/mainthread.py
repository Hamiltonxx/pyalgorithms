from time import sleep, perf_counter
from threading import Thread 
def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    print(f'The task {id} completed')

start_time = perf_counter()
threads = []
for i in range(1,11):
    t = Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = perf_counter()
print(end_time - start_time)
