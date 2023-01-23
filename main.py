import os
from Car import Car
from MyFunctions import *

try:
    c = Car()
    c.drive(1100, 3)

except Exception as e:
    Log(os.getenv("LOG_ERROR_PATH"),e)





