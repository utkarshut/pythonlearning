import threading
import time
import concurrent.futures
start = time.perf_counter()


def do_some(seconds):
    print(f'sleep {seconds} sec')
    time.sleep(seconds)
    print('done sleep')
def do_some1(seconds):
    print(f'sleep {seconds} sec')
    time.sleep(seconds)
    return 'done sleep'

#do_some()
#do_some()

# t1 = threading.Thread(target=do_some)
# t2 = threading.Thread(target=do_some)
# t1.start()
# t2.start()
#
# t1.join()  # for doing finish after both thread start simultaneos
# t2.join()


# submit method return future object but map direclty result
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_some1,1)
#     print(f1.result())
#     results = [ executor.submit(do_some1,1) for _  in range(10)]  # to exectut above in comprhension list
#     for f in  concurrent.futures.as_completed(results):
#          print (f.result())

threads = [] # to join simultaneso
for _ in range(10):
    t = threading.Thread(target=do_some,args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()


print(f'finished in {round(finish-start,2)} seconds')