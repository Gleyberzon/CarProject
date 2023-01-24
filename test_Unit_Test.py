import unittest
import warnings

from Car import Car
from MyFunctions import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.c = Car()
        self.dc = get_vars()
        self.pt = self.dc["TEST_LOG_PATH"]

    # Positive test: gear up from n to n+1
    def test_gear_up_1(self):
        par = self.dc["GEAR_PAR"]
        testName="test_gear_up_1"
        testDescription="Try to gear up from n to n+1"
        parametres=f"n = {par}"
        expected=f"Gear = {par + 1}"
        try:
            self.c.start_driving()
            self.c.gear=self.dc["GEAR_PAR"];
            self.c.gear_up()
            self.assert_(self.c.gear == par+1 and self.c.gear<=self.dc["MAX_GEAR"])
            actual=f"Gear = {self.c.gear}"
            passed=True
            LogTest(self.pt, testName, testDescription, parametres, expected, actual, passed)
        except:
            actual = f"Error"
            passed = False
            LogTest(self.pt, testName, testDescription, parametres, expected, actual, passed)
            self.fail()

    # Boundery test: gear up from max
    def test_gear_ap_2(self):
        par = self.dc["MAX_GEAR"]
        testName="test_gear_up_2"
        testDescription="Try to gear up from n to n+1 when n is max possible value"
        parametres=f"n = {par}"
        expected=f"Gear = {par}"
        try:
            self.c.start_driving()
            self.c.gear=self.dc["MAX_GEAR"];
            with self.assertWarns(UserWarning):
                self.c.gear_up()
            self.assert_(self.c.gear == par and self.c.gear<=self.dc["MAX_GEAR"])
            actual=f"Gear = {self.c.gear}"
            passed=True
            LogTest(self.pt, testName, testDescription, parametres, expected, actual, passed)
        except Exception as e:
            actual = f"Error {e}"
            passed = False
            LogTest(self.pt, testName, testDescription, parametres, expected, actual, passed)
            self.fail()

    # Test drive: positive test
    def test_drive_1(self):
        km = self.dc["PAR_DRIVE_KM"]
        gear = self.dc["PAR_DRIVE_GEAR"]
        testName="test_drive_1"
        testDescription="Try to drive {}km with gear {}".format(km,gear)
        parametres=f"km = {km}, gear = {gear}"
        expected=f"Success drive"
        try:
            self.c.drive(km, gear)
            actual = "Success drive"
            passed=True
            LogTest(self.pt, testName, testDescription, parametres, expected, actual, passed)
            self.assert_(True)
        except Exception as e:
            actual = f"Error {e}"
            passed = False
            LogTest(self.pt, testName, testDescription, parametres, expected, actual, passed)
            self.fail()

    # Test drive: negative test
    def test_drive_2(self):
        km = self.dc["PAR_DRIVE_KM_BIG"]
        gear = self.dc["PAR_DRIVE_GEAR"]
        testName="test_drive_2"
        testDescription="Try to drive {}km with gear {}".format(km,gear)
        parametres=f"km = {km}, gear = {gear}"
        expected=f"Warning"
        try:
            with self.assertWarns(UserWarning):
                self.c.drive(km, gear)
            actual = "Warning"
            passed=True
            LogTest(self.pt, testName, testDescription, parametres, expected, actual, passed)
        except Exception as e:
            actual = f"No warning"
            passed = False
            LogTest(self.pt, testName, testDescription, parametres, expected, actual, passed)
            self.fail()

    # Test drive: invalid value
    def test_drive_3(self):
        km = "Hello"
        gear = "World"
        testName="test_drive_3"
        testDescription="Try to drive with invalid values: km = {}, gear = {}".format(km,gear)
        parametres=f"km = {km}, gear = {gear}"
        expected=f"ValueError"
        try:
            with self.assertRaises(ValueError):
                self.c.start_driving()
                self.c.drive(km, gear)
            actual = "ValueError"
            passed=True
            LogTest(self.pt, testName, testDescription, parametres, expected, actual, passed)
        except Exception as e:
            actual = f"Not raises error"
            passed = False
            LogTest(self.pt, testName, testDescription, parametres, expected, actual, passed)
            self.fail()


if __name__ == '__main__':
    unittest.main()

