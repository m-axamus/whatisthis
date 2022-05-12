def isFlt(num, m = 1):
    if m == 1:
        try:
            float(num)
            return True
        except ValueError:
            return False
    elif m == 2:
        if type(num) == float:
            return True
        else:
            return False

def isInt(num, m = 1):
    if m == 1:
        try:
            int(num)
        except ValueError:
            return False
    elif m == 2:
        if type(num) == int:
            return True
        else:
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
    if type(num) != bool:
        try:
            int(num)
            return True
        except:
            try:
                float(num)
                return True
            except ValueError:
                return False
    else:
        return False

def isBol(bol, m = 1):
    if m == 1:
        if type(bol) == bool:
            return True
        else:
            return False
    elif m == 2:
        try:
            bool(bol)
            return True
        except ValueError:
            return False
