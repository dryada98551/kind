import multiprocessing
import time

def cpu_stress():
    while True:
        pass

if __name__ == "__main__":
    processes = []
    for i in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
