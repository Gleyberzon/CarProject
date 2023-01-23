import pytest
from MyFunctions import *
from Car import Car

@pytest.fixture
def c():
    car=Car()
    car.dc = get_vars()
    car.tpath = car.dc["TEST_LOG_PATH"]
    return car


# Turn on engine while not driving
def test_start_driving_1(c):
    try:
        c.start_driving()
        assert c.status == 1
        assert c.gear == 0
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TURN_ON_WHILE_NOT_DRIVING"]))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TURN_ON_WHILE_NOT_DRIVING"]))
        assert False


@pytest.mark.skip
# Turn on engine while driving
def test_start_driving_2(c):
    try:
        c.status=1
        with pytest.raises(SystemError):
            c.start_driving()
        Log(c.tpath,c.dc["TEST_PASS"].format(c.dc["MESS_TURN_ON_WHILE_DRIVING"]))
    except:
        Log(c.tpath,c.dc["TEST_UNPASS"].format(c.dc["MESS_TURN_ON_WHILE_DRIVING"]))
        assert False

    # Gear up while not started to drive


# Gear up while not started to drive
def test_gear_up_1(c):
    try:
        with pytest.raises(SystemError):
            c.gear_up()
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_GEAR_UP_WHILE_NOT_STARTED"]))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_GEAR_UP_WHILE_NOT_STARTED"]))
        assert False


# Gear up while started to drive 6 times
def test_gear_up_2(c):
    try:
        c.start_driving()
        for i in range(1,c.dc["MAX_GEAR"]+1):
            c.gear_up()
        assert True
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_GEAR_UP_6"]))
    except Exception as e:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_GEAR_UP_6"]))
        assert False


# Gear up while started to drive 7 times
def test_gear_up_3(c):
    try:
        c.start_driving()
        for i in range(1, c.dc["MAX_GEAR"]):
            c.gear_up()
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_GEAR_UP_7"]))
        assert False

    try:
        with pytest.raises(OverflowError):
            c.gear_up()
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_GEAR_UP_7"]))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_GEAR_UP_7"]))


# Gear up while started to drive 2 times
def test_gear_up_4(c):
    try:
        c.start_driving()
        c.gear_up()
        c.gear_up()
        assert c.gear == 2
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_GEAR_UP_2"]))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_GEAR_UP_2"]))
        assert False


# Gear down while not started to drive
def test_gear_down_1(c):
    try:
        with pytest.raises(SystemError):
            c.gear_down()
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_GEAR_DOWN_WHILE_NOT_STARTED"]))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_GEAR_DOWN_WHILE_NOT_STARTED"]))
        assert False


# Gear down while started to drive from 6 to 0
def test_gear_down_2(c):
    try:
        c.start_driving()
        c.gear = 6
        for i in range(1, 7):
            c.gear_down()
        assert True
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_GEAR_DOWN_6"]))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_GEAR_DOWN_6"]))
        assert False


# Gear down while started to drive from 6 to -1
def test_gear_down_3(c):
    try:
        c.start_driving()
        c.gear=6
        for i in range(1, 7):
            c.gear_down()
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_GEAR_DOWN_7"]))
        assert False
    try:
        with pytest.raises(OverflowError):
            c.gear_down()
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_GEAR_DOWN_7"]))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_GEAR_DOWN_7"]))
        assert False


# Gear down while started to drive from 4 to 1
def test_gear_down_4(c):
    try:
        c.start_driving()
        c.gear=4
        c.gear_down()
        c.gear_down()
        c.gear_down()
        assert c.gear == 1
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_GEAR_DOWN_4"]))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_GEAR_DOWN_4"]))
        assert False


# Try to drive while enough fuel, 100 km and valid gear
def test_drive_1(c):
    try:
        c.start_driving()
        c.drive(100, 4)
        assert c.fuel == 45
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_DRIVE"].format(1)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_DRIVE"].format(1)))
        assert False


# Try to drive while enough not fuel and valid gear
def test_drive_2(c):
    try:
        with pytest.raises(ValueError):
            c.start_driving()
            c.drive(1000.5, 4)
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_DRIVE"].format(2)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_DRIVE"].format(2)))
        assert False


# Try to drive while enough not fuel, 100 km and valid gear
def test_drive_3(c):
    try:
        with pytest.raises(ValueError):
            c.start_driving()
            c.drive(1000.5, 4)
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_DRIVE"].format(3)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_DRIVE"].format(3)))
        assert False


# Try to drive with invalid km and invalid gear
def test_drive_4(c):
    try:
        with pytest.raises(ValueError):
            c.start_driving()
            c.drive("A", "B")
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_DRIVE"].format(4)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_DRIVE"].format(4)))
        assert False


# Try to drive with valid km and invalid gear
def test_drive_5(c):
    try:
        with pytest.raises(ValueError):
            c.start_driving()
            c.drive(1, "B")
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_DRIVE"].format(5)))
    except:
        Log(c.path, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_DRIVE"].format(5)))
        assert False


# Try to drive with invalid km and valid gear
def test_drive_6(c):
    try:
        with pytest.raises(ValueError):
            c.start_driving()
            c.drive("A", 4)
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_DRIVE"].format(6)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_DRIVE"].format(6)))
        assert False


# Try to drive with valid km with enough fuel and invalid gear number
def test_drive_7(c):
    try:
        with pytest.raises(ValueError):
            c.start_driving()
            c.drive(10, 7)
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_DRIVE"].format(7)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_DRIVE"].format(7)))
        assert False


# Try to drive with engine turned off
def test_drive_8(c):
    try:
        with pytest.raises(SystemError):
            c.drive(10, 4)
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_DRIVE"].format(8)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_DRIVE"].format(8)))
        assert False


# Test calculating speed
def test_calculate_speed(c):
    c.gear=2
    try:
        assert c.calc_current_speed() == 60
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_SPEED"]))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_SPEED"]))
        assert False


# Test adding fuel: Try add 20L fuel to default value with valid price 1$ for 1L
def test_fuel_1(c):
    try:
        c.add_fuel(20, 1)
        assert c.fuel == 70
        assert c.money == 480
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_FUEL"].format(1)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_FUEL"].format(1)))
        assert False


# Test adding fuel: Try add 51L fuel to default value with valid price 1$ for 1L
def test_fuel_2(c):
    try:
        with pytest.raises(OverflowError):
            c.add_fuel(51,1)
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_FUEL"].format(2)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_FUEL"].format(1)))
        assert False


# Test adding fuel: Try add 10L fuel to default value with valid price 51$ for 1L
def test_fuel_3(c):
    try:
        with pytest.raises(OverflowError):
            c.add_fuel(10,51)
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_FUEL"].format(3)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_FUEL"].format(3)))
        assert False


# Test adding fuel: Try to add several times valid count of fuel
def test_fuel_4(c):
    try:
        c.fuel=0
        c.money=500
        c.add_fuel(10,10)
        c.add_fuel(20,10)
        assert c.fuel == 30
        assert c.money == 200
        Log(c.tpath, c.dc["TEST_PASS"].format(c.dc["MESS_TEST_FUEL"].format(4)))
    except:
        Log(c.tpath, c.dc["TEST_UNPASS"].format(c.dc["MESS_TEST_FUEL"].format(4)))
        assert False