import multiprocessing
import time
import concurrent.futures

import concurrent.futures
start = time.perf_counter()

processs = []
def do_some(seconds):
    print(f'sleep  {seconds} sec')
    time.sleep(seconds)
    print('done sleep')

def do_some1(seconds):
    print(f'sleep  {seconds} sec')
    time.sleep(seconds)
    return  'done sleep1'

# p1 = multiprocessing.Process(target=do_some)
# p2 = multiprocessing.Process(target=do_some)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()

# serialize arg means it can deconstruct in pythons

for _ in range(10):
    p = multiprocessing.Process(target=do_some, args=[1])
    p.start()
    processs.append(p)
for process in processs:
    process.join()


with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_some1 , 1)
    # results = [executor.submit(do_some1, 1) for _ in range(10)] for multiple times
    print(f1.result())
#    for f in concurrent.futures.as_completed(results):
#          print (f.result())

finish = time.perf_counter()


print(f'finished in {round(finish-start,2)} seconds')