from MyFunctions import *
import warnings
class Car:
    def __init__(self):
        load_dotenv()
        self.dc = get_vars()
        self.fuel = self.dc["DEFAULT_FUEL"] # L
        self.max_fuel = self.dc["DEFAULT_MAX_FUEL"] #L
        self.fuel_consumption = self.dc["DEFAULT_FUEL_CONSUMPTION"] # L/KM
        self.money = self.dc["DEFAULT_MONEY"] # $
        self.gear = self.dc["DEFAULT_GEAR"]
        # Status of engine: 0 - off, 1 - on
        self.status = 0
        self.path = self.dc["LOG_PATH"]
        Log(self.path, "*********** New Car Created ***********")

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
            warnings.warn(self.dc["GEAR_ERR"].format(self.dc["MAX_GEAR"]), category=UserWarning)

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
            warnings.warn(self.dc["GEAR_ERR"].format(0))

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
            Log(self.path, self.dc["WARN_MESS_ALREADY_STARTED"])
            warnings.warn(self.dc["WARN_MESS_ALREADY_STARTED"])
        self.status = 1
        self.gear = 0
        Log(self.path,self.dc["MESS_ENGINE_ON"])

    def drive(self, km, gear):
        """
        Name: Roman Gleyberzon
        Date: 22/1/2023
        Description: This method makes car driving
        Input: km, gear
        Output: None
        """
        if (self.status == 0):
            self.start_driving()
        elif not (isinstance(km, int) or isinstance(km, float)):
            raise ValueError(self.dc["KM_NOT_VALID"])
        elif km < 0:
            raise ValueError(self.dc["KM_NOT_VALID"])
        elif not (isinstance(gear, int) or isinstance(gear, float)):
            raise ValueError(self.dc["GEAR_NOT_VALID"].format(self.dc["MAX_GEAR"]))
        elif not (gear > 0 and gear < self.dc["MAX_GEAR"]+1):
            raise ValueError(self.dc["GEAR_NOT_VALID"].format(self.dc["MAX_GEAR"]))
        Log(self.path, self.dc["TRY_TO_DRIVE"].format(km))
        need_fuel_for_km = km * self.fuel_consumption
        max_possible_fuel_amount = self.fuel + self.money/self.dc["PRICE_FOR_1L"]
        Log(self.path, self.dc["NEED_FUEL_MAX_POSSIBLE"].format(need_fuel_for_km,max_possible_fuel_amount))
        if (need_fuel_for_km > max_possible_fuel_amount):
            warnings.warn(self.dc["NOT_ENOUGH_FUEL_AND_MONEY"].format(km))
            Log(self.path, self.dc["NOT_ENOUGH_FUEL_AND_MONEY"].format(km))
        else:
            if (self.gear<gear):
                while (self.gear != gear):
                    self.gear_up()
            if (self.gear>gear):
                while (self.gear != gear):
                    self.gear_down()
            remain_km = km
            while remain_km != 0:
                if (remain_km * self.fuel_consumption <= self.fuel):
                    self.fuel -= remain_km * self.fuel_consumption
                    Log(self.path, self.dc["DRIVE_LOG"].format(remain_km, self.fuel, self.money))
                    remain_km = 0
                else:
                    passed_km = self.fuel/self.fuel_consumption
                    remain_km -= passed_km
                    Log(self.path,self.dc["DRIVE_LOG_2"].format(passed_km, remain_km))
                    self.fuel = 0
                    self.add_fuel(self.money*self.dc["PRICE_FOR_1L"], self.dc["PRICE_FOR_1L"])

            speed = self.calc_current_speed()
            time = int(((km / speed)*100))/100
            # Log
            Log(self.path, self.dc["DRIVE_LOG_TOTAL"].format(km, time, speed, self.fuel, self.money))

    def stop_driving(self):
        """
        Name: Roman Gleyberzon
        Date: 22/1/2023
        Description: This method turns off engine
        Input: Name
        Output: None
        """
        if (self.status == 0):
            Log(self.path, self.dc["WARN_MESS_ALREADY_STOPPED"])
        else:
            while (self.gear > 0):
                self.gear_down()
            Log(self.path, self.dc["MESS_ENGINE_OFF"])
            self.status = 0


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
        elif price_for_litr<=0:
            raise ValueError(self.dc["PRICE_ERR"])
        elif (amount * price_for_litr > self.money):
            warnings.warn("NO_MONEY".format(amount, amount * price_for_litr, self.money))
        else:
            if (amount + self.fuel> self.max_fuel):
                Log(self.path,self.dc["FUEL_MONEY_MESS"].format(self.fuel,self.max_fuel,amount))
                new_amount = self.max_fuel - self.fuel
                Log(self.path,f"Will add {new_amount}L")
                price = new_amount * price_for_litr
                self.money -= price
                self.fuel += new_amount
                Log(self.path, self.dc["MESS_ADD_FUEL_SUCCSESS"].format(new_amount, price))
            else:
                Log(self.path,self.dc["FUEL_MONEY_MESS"].format(self.fuel,self.max_fuel,amount))
                price = amount * price_for_litr
                self.money -= price
                self.fuel += amount
                Log(self.path, self.dc["MESS_ADD_FUEL_SUCCSESS"].format(amount, price))
            Log(self.path, self.dc["ADD_FUEL_TOTAL_LOG"].format(self.fuel, self.money))

