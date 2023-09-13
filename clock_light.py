import os
import datetime
import time

num_1 = "███ ", " ██ ", " ██ ", " ██ ", "████"
num_2 = "█████", "   ██", "█████", "██   ", "█████"
num_3 = "█████", "   ██", " ████", "   ██", "█████"
num_4 = "██ ██", "██ ██", "█████", "   ██", "   ██"
num_5 = "█████", "██   ", "█████", "   ██", "█████"
num_6 = "█████", "██   ", "█████", "██ ██", "█████"
num_7 = "█████", "   ██", "   ██", "   ██", "   ██"
num_8 = "█████", "██ ██", "█████", "██ ██", "█████"
num_9 = "█████", "██ ██", "█████", "   ██", "█████"
num_0 = "█████", "██ ██", "██ ██", "██ ██", "█████"
symbol_1 = "  ", "  ", "  ", "  ", "  "
symbol_2 = "  ", "██", "  ", "██", "  "
symbol = symbol_1


def tn_func():
    tn_new = []
    str_tn = datetime.datetime.now().strftime("%H:%M:%S")
    for i in str_tn:
        if i == "0":
            tn_new.append(num_0)
        if i == "1":
            tn_new.append(num_1)
        if i == "2":
            tn_new.append(num_2)
        if i == "3":
            tn_new.append(num_3)
        if i == "4":
            tn_new.append(num_4)
        if i == "5":
            tn_new.append(num_5)
        if i == "6":
            tn_new.append(num_6)
        if i == "7":
            tn_new.append(num_7)
        if i == "8":
            tn_new.append(num_8)
        if i == "9":
            tn_new.append(num_9)
        if i == ":":
            tn_new.append(list())
    return tn_new


def layer():
    global symbol
    tn_new = tn_func()
    for i in range(5):
        print(
            tn_new[0][i],
            tn_new[1][i],
            symbol[i],
            tn_new[3][i],
            tn_new[4][i],
            symbol[i],
            tn_new[6][i],
            tn_new[7][i],
        )
    if symbol == symbol_1:
        symbol = symbol_2
    else:
        symbol = symbol_1


while True:
    layer()
    time.sleep(0.2)
    os.system("cls")
