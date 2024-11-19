import os 
import multiprocessing as mp 


print(os.cpu_count())

print(mp.current_process())
print(mp.current_process().name)
print(mp.parent_process())