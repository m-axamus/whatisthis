import string


def isFloat(num):
    try: #trying to float the data, if it can, return True
        float(num)
        return True
    except ValueError: #if it can't be floated, return False
        return False

def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def isString(v, str):
    if v == 1:
        try:
            string(str)
            return True
        except ValueError:
            return False
    if v == 2:
        try:
            float(str)
            return False
        except ValueError:
            return True

def isList():
    print('Work In Progress')