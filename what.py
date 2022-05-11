def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def isStr(v, str):
    if v == 1:
        if str == type(str):
            return True
        else:
            return False
    if v == 2:
        try:
            float(str)
            return False
        except ValueError:
            return True

def isLst(list):
    try:
        list[0]
        return True
    except ValueError:
        return False
