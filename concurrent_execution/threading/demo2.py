# Python 3.11.2

import time 
from threading import Thread


class MyThread(Thread):
    
    def __init__(self, name, counter, delay):
        super().__init__()

        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print("Ready to run", self.name)
        while self.counter:
            time.sleep(self.delay)
            print(f"{self.name}: {time.ctime(time.time())}")
            self.counter -= 1
        
        print("End of loop", self.name)
    

if __name__ == "__main__":
    thread1 = MyThread("Thread 1", 10, 2)    # countdown from 10 with delay of 2s
    thread2 = MyThread("Thread 2", 10, 3)    # countdown from 10 with delay of 3s

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
