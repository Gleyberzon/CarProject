import pytest
from MyFunctions import *
from Car import Car

@pytest.fixture
def c():
    car=Car()
    car.dc = get_vars()
    car.pt = car.dc["TEST_LOG_PATH"]
    return car


# Turn on engine while not driving
def test_gear_up_1(c):
    par = c.dc["GEAR_PAR"]
    testName = "test_gear_up_1"
    testDescription = "Try to gear up from n to n+1"
    parametres = f"n = {par}"
    expected = f"Gear = {par + 1}"
    try:
        c.start_driving()
        c.gear = c.dc["GEAR_PAR"];
        c.gear_up()
        assert (c.gear == par + 1 and c.gear <= c.dc["MAX_GEAR"])
        actual = f"Gear = {c.gear}"
        passed = True
        LogTest(c.pt, testName, testDescription, parametres, expected, actual, passed)
    except:
        actual = f"Error"
        passed = False
        LogTest(c.pt, testName, testDescription, parametres, expected, actual, passed)
        c.fail()


# Boundery test: gear up from max
def test_gear_ap_2(c):
    par = c.dc["MAX_GEAR"]
    testName="test_gear_up_2"
    testDescription="Try to gear up from n to n+1 when n is max possible value"
    parametres=f"n = {par}"
    expected=f"Gear = {par}"
    try:
        c.start_driving()
        c.gear=c.dc["MAX_GEAR"];
        with pytest.warns(UserWarning):
            c.gear_up()
        assert (c.gear == par and c.gear<=c.dc["MAX_GEAR"])
        actual=f"Gear = {c.gear}"
        passed=True
        LogTest(c.pt, testName, testDescription, parametres, expected, actual, passed)
    except Exception as e:
        actual = f"Error {e}"
        passed = False
        LogTest(c.pt, testName, testDescription, parametres, expected, actual, passed)
        assert False


# Test drive: positive test
def test_drive_1(c):
    km = c.dc["PAR_DRIVE_KM"]
    gear = c.dc["PAR_DRIVE_GEAR"]
    testName="test_drive_1"
    testDescription="Try to drive {}km with gear {}".format(km,gear)
    parametres=f"km = {km}, gear = {gear}"
    expected=f"Success drive"
    try:
        c.drive(km, gear)
        actual = "Success drive"
        passed=True
        LogTest(c.pt, testName, testDescription, parametres, expected, actual, passed)
    except Exception as e:
        actual = f"Error {e}"
        passed = False
        LogTest(c.pt, testName, testDescription, parametres, expected, actual, passed)
        assert False


# Test drive: negative test
def test_drive_2(c):
    km = c.dc["PAR_DRIVE_KM_BIG"]
    gear = c.dc["PAR_DRIVE_GEAR"]
    testName="test_drive_2"
    testDescription="Try to drive {}km with gear {}".format(km,gear)
    parametres=f"km = {km}, gear = {gear}"
    expected=f"Warning"
    try:
        with pytest.warns(UserWarning):
            c.drive(km, gear)
        actual = "Warning"
        passed=True
        LogTest(c.pt, testName, testDescription, parametres, expected, actual, passed)
    except Exception as e:
        actual = f"No warning"
        passed = False
        LogTest(c.pt, testName, testDescription, parametres, expected, actual, passed)
        assert False

@pytest.mark.skip
# Test drive: invalid value
def test_drive_3(c):
    km = "Hello"
    gear = "World"
    testName="test_drive_3"
    testDescription="Try to drive with invalid values: km = {}, gear = {}".format(km,gear)
    parametres=f"km = {km}, gear = {gear}"
    expected=f"ValueError"
    try:
        with pytest.raises(ValueError):
            c.start_driving()
            c.drive(km, gear)
        actual = "ValueError"
        passed=True
        LogTest(c.pt, testName, testDescription, parametres, expected, actual, passed)
    except Exception as e:
        actual = f"Not raises error"
        passed = False
        LogTest(c.pt, testName, testDescription, parametres, expected, actual, passed)
        assert False


