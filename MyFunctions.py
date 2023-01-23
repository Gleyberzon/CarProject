import os
from dotenv import load_dotenv, dotenv_values


def Log(path,mess,time=True):
    """
    Name: Roman Gleyberzon
    Date: 18/1/2023
    Description: This function write logs to log.txt
    Input: Content of log
    Output: None
    """
    import datetime
    try:
        f = open(path, "a")
        if (time):
            f.write(f"{datetime.datetime.now()} Author: Roman Gleyberzon {mess}\n")
        else:
            f.write(f"{mess}\n")
        f.close()
    except Exception:
        print("Log writing error")


def get_vars():
    """
    Name: Roman Gleyberzon
    Date: 18/1/2023
    Description: This function returns all parametrs from file .env as a dictionary
    Input: Content of log
    Output: None
    """
    load_dotenv()
    dc = {}
    edc = dict(dotenv_values())
    for key in edc.keys():
        try:
            dc[key] = int(edc[key])
        except:
            try:
                dc[key] = float(edc[key])
            except:
                dc[key] = edc[key]
    return dc