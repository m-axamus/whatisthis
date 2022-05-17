Purpose - To provide capabilities to check what types of variable something is and return True or False. 

Can also check if a variable can be something else, e.g. if variable x is a float, but contains only the number 2, isInt(x) will return true.


All methods (m) will default to 1, unless specified

Usage -

what.isFlt(num, m)      m = 1, checking if the variable can be a float. m = 2, checking if the variable is a float

what.isInt(num)         m = 1, checking if the variable can be an integer. m = 2, checking if the variable is an integer

what.isLst(list)        checking if the variable is a list

what.isStr(string)      checking if the variable is a string

what.isTxt(txt)         checking if a variable contains text (anything but numbers)

what.isCmp(num)         checking if the variable is a complex number

what.isNum(num)         checking if the variable is a number (either float or int)

what.isBol(bol, m)      m = 1, checking if the variable is a boolean. m = 2, checking if the variable can be booled (will return True for anything that isn't nothing or 0)

what.lstThis(lst, app)  basically just appending the variable app to the variable lst, extremely situational

what.doLst(file, lst)   splits the file into a blank list vairable (blank by default) file must be formatted a certain way available at example.txt

The plan is to turn this into a python package