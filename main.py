from dotenv import load_dotenv
from Car import Car
from MyFunctions import *
load_dotenv()
try:
    c = Car()
    c.start_driving()
    c.drive(900, 3)
    c.drive(2500, 2)
    c.drive(1500, 6)
    c.stop_driving()

except Exception as e:
    Log(os.getenv("LOG_ERROR_PATH"),e)





