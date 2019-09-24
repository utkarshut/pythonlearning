import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')


# In multiprocessing, the system allows executing multiple programs and tasks at the same time, whereas, in multithreading, the system executes multiple threads of the same or different processes at the same time.
#
# Multiprocessing increases the computing speed of the system. In contrast, Multithreading increase the responsiveness of the system.
#
# Multiprocessing allocates separate memory and resources for each process/program whereas, in multithreading threads belonging to the same process shares the same memory and resources as that of the process.
#
