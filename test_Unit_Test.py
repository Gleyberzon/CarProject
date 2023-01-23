import unittest
from Car import Car
from MyFunctions import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.c = Car()
        self.dc = get_vars()
        self.path = self.dc["TEST_LOG_PATH"]

    # Turn on engine while not driving
    def test_start_driving_1(self):
        try:
            self.c.start_driving()
            self.assertTrue(self.c.status==1)
            self.assertTrue(self.c.gear==0)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TURN_ON_WHILE_NOT_DRIVING"]))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TURN_ON_WHILE_NOT_DRIVING"]))
            self.assert_(False)

    # Turn on engine while driving
    def test_start_driving_2(self):
        try:
            self.c.status=1
            with self.assertRaises(SystemError):
                self.c.start_driving()
            Log(self.path,self.dc["TEST_PASS"].format(self.dc["MESS_TURN_ON_WHILE_DRIVING"]))
        except:
            Log(self.path,self.dc["TEST_UNPASS"].format(self.dc["MESS_TURN_ON_WHILE_DRIVING"]))
            self.assert_(False)

    # Gear up while not started to drive
    def test_gear_up_1(self):
        try:
            with self.assertRaises(SystemError):
                self.c.gear_up()
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_GEAR_UP_WHILE_NOT_STARTED"]))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_GEAR_UP_WHILE_NOT_STARTED"]))
            self.assert_(False)

    # Gear up while started to drive 6 times
    def test_gear_up_2(self):
        try:
            self.c.start_driving()
            for i in range(1,7):
                self.c.gear_up()
            self.assert_(True)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_GEAR_UP_6"]))
        except Exception as e:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_GEAR_UP_6"]))
            self.assert_(False)

    # Gear up while started to drive 7 times
    def test_gear_up_3(self):
        try:
            self.c.start_driving()
            for i in range(1, 7):
                self.c.gear_up()
        except:
            Log(self.path,self.dc["TEST_UNPASS"].format(self.dc["MESS_GEAR_UP_7"]))
            self.assert_(False)
        try:
            with self.assertRaises(OverflowError):
                self.c.gear_up()
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_GEAR_UP_7"]))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_GEAR_UP_7"]))
            self.assert_(False)

    # Gear up while started to drive 2 times
    def test_gear_up_4(self):
        try:
            self.c.start_driving()
            self.c.gear_up()
            self.c.gear_up()
            self.assertEqual(self.c.gear,2)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_GEAR_UP_2"]))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_GEAR_UP_2"]))
            self.assert_(False)

    # Gear down while not started to drive
    def test_gear_down_1(self):
        try:
            with self.assertRaises(SystemError):
                self.c.gear_down()
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_GEAR_DOWN_WHILE_NOT_STARTED"]))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_GEAR_DOWN_WHILE_NOT_STARTED"]))
            self.assert_(False)

    # Gear down while started to drive from 6 to 0
    def test_gear_down_2(self):
        try:
            self.c.start_driving()
            self.c.gear = 6
            for i in range(1, 7):
                self.c.gear_down()
            self.assertTrue(True)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_GEAR_DOWN_6"]))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_GEAR_DOWN_6"]))
            self.assert_(False)

    # Gear down while started to drive from 6 to -1
    def test_gear_down_3(self):
        try:
            self.c.start_driving()
            self.c.gear=6
            for i in range(1, 7):
                self.c.gear_down()
        except:
            self.assertFalse("")
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_GEAR_DOWN_7"]))
            self.assert_(False)
        try:
            with self.assertRaises(OverflowError):
                self.c.gear_down()
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_GEAR_DOWN_7"]))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_GEAR_DOWN_7"]))
            self.assert_(False)

    # Gear down while started to drive from 4 to 1
    def test_gear_down_4(self):
        try:
            self.c.start_driving()
            self.c.gear=4
            self.c.gear_down()
            self.c.gear_down()
            self.c.gear_down()
            self.assertEqual(self.c.gear, 1)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_GEAR_DOWN_4"]))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_GEAR_DOWN_4"]))
            self.assert_(False)

    # Try to drive while enough fuel, 100 km and valid gear
    def test_drive_1(self):
        try:
            self.c.start_driving()
            self.c.drive(100, 4)
            self.assertEqual(self.c.fuel, 45)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_DRIVE"].format(1)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_DRIVE"].format(1)))
            self.assert_(False)

    # Try to drive while enough not fuel and valid gear
    def test_drive_2(self):
        try:
            with self.assertRaises(ValueError):
                self.c.start_driving()
                self.c.drive(1000.5, 4)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_DRIVE"].format(2)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_DRIVE"].format(2)))
            self.assert_(False)

    # Try to drive while enough not fuel, 100 km and valid gear
    def test_drive_3(self):
        try:
            with self.assertRaises(ValueError):
                self.c.start_driving()
                self.c.drive(1000.5, 4)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_DRIVE"].format(3)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_DRIVE"].format(3)))
            self.assert_(False)

    # Try to drive with invalid km and invalid gear
    def test_drive_4(self):
        try:
            with self.assertRaises(ValueError):
                self.c.start_driving()
                self.c.drive("A", "B")
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_DRIVE"].format(4)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_DRIVE"].format(4)))
            self.assert_(False)

    # Try to drive with valid km and invalid gear
    def test_drive_5(self):
        try:
            with self.assertRaises(ValueError):
                self.c.start_driving()
                self.c.drive(1, "B")
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_DRIVE"].format(5)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_DRIVE"].format(5)))
            self.assert_(False)

    # Try to drive with invalid km and valid gear
    def test_drive_6(self):
        try:
            with self.assertRaises(ValueError):
                self.c.start_driving()
                self.c.drive("A", 4)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_DRIVE"].format(6)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_DRIVE"].format(6)))
            self.assert_(False)

    # Try to drive with valid km with enough fuel and invalid gear number
    def test_drive_7(self):
        try:
            with self.assertRaises(ValueError):
                self.c.start_driving()
                self.c.drive(10, 7)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_DRIVE"].format(7)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_DRIVE"].format(7)))
            self.assert_(False)

    # Try to drive with engine turned off
    def test_drive_8(self):
        try:
            with self.assertRaises(SystemError):
                self.c.drive(10, 4)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_DRIVE"].format(8)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_DRIVE"].format(8)))
            self.assert_(False)

    # Test calculating speed
    def test_calculate_speed(self):
        self.c.gear=2
        try:
            self.assertEqual(self.c.calc_current_speed(),60)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_SPEED"]))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_SPEED"]))
            self.assert_(False)

    #@unittest.skip
    # Test adding fuel: Try add 20L fuel to default value with valid price 1$ for 1L
    def test_fuel_1(self):
        try:
            self.c.add_fuel(20, 1)
            self.assertEqual(self.c.fuel,70)
            self.assertEqual(self.c.money, 480)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_FUEL"].format(1)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_FUEL"].format(1)))
            self.assert_(False)
        finally:
            Log(self.path,"DESCRIPTION:",False)
            Log(self.path, f"Start value fuel: {50}L, start value money: {500}$",False)
            Log(self.path,"Entered parametres: fuel: 20L, price for 1L: 1$",False)
            Log(self.path,f"Expected: fuel {70}L, Actual: fuel {self.c.fuel}L",False)
            Log(self.path,f"Expected: money: {480}$, Actual: money: {self.c.money}$",False)

    # Test adding fuel: Try add 51L fuel to default value with valid price 1$ for 1L
    def test_fuel_2(self):
        try:
            with self.assertRaises(OverflowError):
                self.c.add_fuel(51,1)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_FUEL"].format(2)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_FUEL"].format(1)))
            self.assert_(False)

    # Test adding fuel: Try add 10L fuel to default value with valid price 51$ for 1L
    def test_fuel_3(self):
        try:
            with self.assertRaises(OverflowError):
                self.c.add_fuel(10,51)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_FUEL"].format(3)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_FUEL"].format(3)))
            self.assert_(False)

    # Test adding fuel: Try to add several times valid count of fuel
    def test_fuel_4(self):
        try:
            self.c.fuel=0
            self.c.money=500
            self.c.add_fuel(10,10)
            self.c.add_fuel(20,10)
            self.assertEqual(self.c.fuel, 30)
            self.assertEqual(self.c.money, 200)
            Log(self.path, self.dc["TEST_PASS"].format(self.dc["MESS_TEST_FUEL"].format(4)))
        except:
            Log(self.path, self.dc["TEST_UNPASS"].format(self.dc["MESS_TEST_FUEL"].format(4)))
            self.assert_(False)


if __name__ == '__main__':
    unittest.main()

