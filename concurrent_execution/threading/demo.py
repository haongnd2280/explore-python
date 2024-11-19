import time
from threading import Thread

def cal_square(numbers):
	print("Calculate square number")
	for n in numbers:
		time.sleep(0.2)
		print("Square:", n * n)

def cal_cube(numbers):
	print("Calculate cube number")
	for n in numbers:
		time.sleep(0.2)
		print("Cube:", n * n * n)


arr = [2, 3, 7, 9]

start = time.time()
# cal_square(arr)
# cal_cube(arr)
t1 = Thread(target=cal_square, args=(arr,))
t2 = Thread(target=cal_cube, args=(arr,))

t1.start()      # run thread 1 
t2.start()      # run thread 2

t1.join()
t2.join()

end = time.time()

print("Execution done in", end - start, "s.")

