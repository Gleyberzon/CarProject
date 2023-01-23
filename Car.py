import os
from dotenv import load_dotenv
from MyFunctions import *
class Car:
    def __init__(self):
        load_dotenv()
        self.dc = get_vars()
        self.fuel = self.dc["DEFAULT_FUEL"]
        self.max_fuel = self.dc["DEFAULT_MAX_FUEL"]
        self.fuel_consumption = self.dc["DEFAULT_FUEL_CONSUMPTION"]
        self.money = self.dc["DEFAULT_MONEY"]
        self.gear = self.dc["DEFAULT_GEAR"]
        # Status of engine: 0 - off, 1 - on
        self.status = 0
        self.path = self.dc["LOG_PATH"]

    def gear_up(self):
        """
        Name: Roman Gleyberzon
        Date: 22/1/2023
        Description: This method increase current gear level to 1
        Input: Name
        Output: None
        """
        if self.status == 0:
            self.start_driving()
        if self.gear < self.dc["MAX_GEAR"]:
            self.gear += 1
            # Log
            Log(self.path,self.dc["MESS_GEAR_UPED_TO"].format(self.gear))
        else:
            raise OverflowError(self.dc["GEAR_ERR"].format("max"))

    def gear_down(self):
        """
        Name: Roman Gleyberzon
        Date: 22/1/2023
        Description: This method decrease current gear level to 1
        Input: Name
        Output: None
        """
        if self.status == 0:
            self.start_driving()
        if self.gear > 0:
            self.gear -= 1
            # Log
            Log(self.path,self.dc["MESS_GEAR_DOWNED_TO"].format(self.gear))
        else:
            raise OverflowError(self.dc["GEAR_ERR"].format(0))

    def calc_current_speed(self):
        """
        Name: Roman Gleyberzon
        Date: 22/1/2023
        Description: This calculates current speed
        Input: Gear level
        Output: Speed
        """
        return self.gear * self.dc["DEFAULT_SPEED_FOR_GEAR_LEVEL"]

    def start_driving(self):
        """
        Name: Roman Gleyberzon
        Date: 22/1/2023
        Description: This method enables engine
        Input: Name
        Output: None
        """
        if self.status==1:
            Log(self.path, "Try to start driving: warning - already started")
        self.status = 1
        self.gear = 0
        Log(self.path,self.dc["MESS_ENGINE_ON"])

    def drive(self, val, gear):
        """
        Name: Roman Gleyberzon
        Date: 22/1/2023
        Description: This method makes car driving
        Input: km, gaer
        Output: None
        """
        if (self.status == 0):
            self.start_driving()
        elif not (isinstance(val, int) or isinstance(val, float)):
            raise ValueError(self.dc["KM_NOT_VALID"])
        elif val < 0:
            raise ValueError(self.dc["KM_NOT_VALID"])
        elif not (isinstance(gear, int) or isinstance(gear, float)):
            raise ValueError(self.dc["GEAR_NOT_VALID"])
        elif not (gear > 0 and gear < self.dc["MAX_GEAR"]+1):
            raise ValueError(self.dc["GEAR_NOT_VALID"])
        if (val * self.fuel_consumption > self.fuel+self.money*self.fuel_consumption):
            raise ValueError(self.dc["NOT_ENOUGH_FUEL_AND_MONEY"].format(val))
        else:
            if (self.gear<gear):
                while (self.gear != gear):
                    self.gear_up()
            if (self.gear>gear):
                while (self.gear != gear):
                    self.gear_down()
            remain = val
            while remain != 0:
                if (remain<self.fuel):
                    self.fuel -= remain
                    remain = 0
                else:
                    passed_km = self.fuel*self.fuel_consumption
                    remain -= self.fuel
                    Log("Passed {}km, fuel ended, remain to pass {}km".format(passed_km, remain))
                    self.fuel = 0
                    self.add_fuel(self.money*self.dc["PRICE_FOR_1L"])



            speed = self.calc_current_speed()
            time = val / speed
            # Log
            Log(self.path,self.dc["CAR_DRIVE_MESS"].format(val,time,speed))

    def stop_driving(self):
        """
        Name: Roman Gleyberzon
        Date: 22/1/2023
        Description: This method turns off engine
        Input: Name
        Output: None
        """
        if (self.status == 0):
            raise SystemError(self.dc["ERR_ENGINE_OFF"])
        else:
            while (self.gear > 0):
                self.gear_down()
            self.status = 0
            Log(self.path,self.dc["MESS_ENGINE_OFF"])

    def get_current_fuel(self):
        """
        Name: Roman Gleyberzon
        Date: 22/1/2023
        Description: This method returns current remaining fuel
        Input: Name
        Output: None
        """
        return self.fuel

    def add_fuel(self, amount, price_for_litr):
        """
        Name: Roman Gleyberzon
        Date: 22/1/2023
        Description: This method takes amount and price for 1L, add amount to current fuel and decrease money
        Input: amount, price for 1L
        Output: None
        """
        if not (isinstance(amount, int) or isinstance(amount, float)):
            raise ValueError(self.dc["AMOUNT_ERR"])
        elif amount < 0:
            raise ValueError(self.dc["AMOUNT_ERR"])
        elif not (isinstance(price_for_litr, int) or isinstance(price_for_litr, float)):
            raise ValueError(self.dc["PRICE_ERR"])
        elif (amount * price_for_litr > self.money):
            raise OverflowError(self.dc["ERR_FUEL_OVERFLOW"])
        else:
            if (amount + self.fuel> self.max_fuel):
                Log(f"Current amount fuel: {self.fuel}L, max amount of fuel {self.max_fuel}L, tried to add {amount}L")
                new_amount = self.max_fuel - self.fuel
                Log(f"Will add {new_amount}L")
                price = new_amount * price_for_litr
                self.money -= price
                self.fuel += new_amount
                Log(self.path, self.dc["MESS_ADD_FUEL_SUCCSESS"].format(new_amount, price))
            else:
                Log(f"Current amount fuel: {self.fuel}L, max amount of fuel {self.max_fuel}L, tried to add {amount}L")
                price = amount * price_for_litr
                self.money -= price
                self.fuel += amount
                Log(self.path, self.dc["MESS_ADD_FUEL_SUCCSESS"].format(amount, price))

