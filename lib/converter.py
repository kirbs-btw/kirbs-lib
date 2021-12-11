from datetime import datetime

def dateConverter_yyyy_mm_dd():
    """gives current date as yyyy-mm-dd"""
    nowDate = datetime.now()
    year = ""
    month = ""
    day = ""
    n = 0
    stop = True
    for letter in str(nowDate):
        if letter == " ":
            stop = False
        elif letter == "-":
            n += 1
        elif n == 0 and stop == True:
            year = year + letter
        elif n == 1 and stop == True:
            month = month + letter
        elif n == 2 and stop == True:
            day = day + letter

    date = f'{year}-{month}-{day}'

    return date

def dateConverter_dd_mm_yyyy():
    """gives current date as dd-mm-yyyy"""

    nowDate = datetime.now()
    year = ""
    month = ""
    day = ""
    n = 0
    stop = True
    for letter in str(nowDate):
        if letter == " ":
            stop = False
        elif letter == "-":
            n += 1
        elif n == 0 and stop == True:
            year = year + letter
        elif n == 1 and stop == True:
            month = month + letter
        elif n == 2 and stop == True:
            day = day + letter

    date = f'{day}-{month}-{year}'
    return date

#Bastian Lipka