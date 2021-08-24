# ---------- For Generate .so File Use This Command in Terminal ---------- 
# cc -fPIC -shared -o my_func.so my_func.c 

from ctypes import *
so_file = "my_func.so"
my_function = CDLL(so_file)
print (my_function.square(2))


