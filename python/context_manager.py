
from contextlib import contextmanager
 
@contextmanager
def tracing():
   print("start")
   yield
   print("stop")
 
try:
   with tracing():
       print("in progress")
       raise RuntimeError("error")
   print("exit")
except RuntimeError:
   print("error")
else:
   print("ok")
   
   
    
 start
 inptogress
 error
 stop
    
