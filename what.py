def isFlt(num):
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

def isStr(string):
    if type(string) == str:
        return True
    else:
        return False

def isTxt(txt):
    try:
        float(txt)
        return False
    except ValueError:
        return True

def isLst(list):
    try:
        list[0]
        return True
    except ValueError:
        return False
