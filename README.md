Purpose - To provide capabilities to check what types of variable something is and return True or False.


Functions - 
what.isFloat(num)
what.isInt(num)
what.isLst(list)
what.isStr(m, str)

m is method, this is due to the fact that it can check for strings in 2 different situations
m = 1
this method checks if something is a string, this method may return true even if something isn't a string. this is due to the fact that things that aren't just text can be strings too
m = 2
this method checks if something can be floated, if it can, this means that it isn't a string and is just text
