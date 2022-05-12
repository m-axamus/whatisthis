def isFlt(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def isInt(num):
    try:
        int(num)
        if type(num) == float:
            return False
        else:
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

def isLst(lst):
    if type(lst) == list:
        return True
    else:
        return False

def isCmp(num):
    if type(num) == complex:
        return True
    elif type(num) != complex:
        return False

def isTpl(tpl):
    if type(tpl) == tuple:
        return True
    else:
        return False

def isNum(num):
    try:
        int(num)
        return True
    except:
        try:
            float(num)
            return True
        except ValueError:
            return False

