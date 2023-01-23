import os
from Car import Car
from MyFunctions import *

try:
    c = Car()
    c.start_driving()
    c.drive(10, 3)
    c.drive(5,4)
    c.stop_driving()
    c.add_fuel(50,4)
    c.drive(10,1)
except Exception as e:
    Log(os.getenv("LOG_ERROR_PATH"),e)





