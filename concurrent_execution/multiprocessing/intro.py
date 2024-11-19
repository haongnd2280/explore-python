import os
import multiprocessing as mp 


print(mp.cpu_count())    # return logical processor, not physical processor 
print(mp.current_process().name)     # MainProcess
print(mp.parent_process())
print(mp.active_children())
 
print(os.cpu_count())
print(os.getpid())
