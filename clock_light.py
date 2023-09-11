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


while True:
    xxx = []
    str_tn = datetime.datetime.now().strftime("%H:%M:%S")
    for i in str_tn:
        if i == "0":
            xxx.append(num_0)
        if i == "1":
            xxx.append(num_1)
        if i == "2":
            xxx.append(num_2)
        if i == "3":
            xxx.append(num_3)
        if i == "4":
            xxx.append(num_4)
        if i == "5":
            xxx.append(num_5)
        if i == "6":
            xxx.append(num_6)
        if i == "7":
            xxx.append(num_7)
        if i == "8":
            xxx.append(num_8)
        if i == "9":
            xxx.append(num_9)
        if i == ":":
            xxx.append(list())

    print(
        xxx[0][0],
        xxx[1][0],
        symbol_1[0],
        xxx[3][0],
        xxx[4][0],
        symbol_1[0],
        xxx[6][0],
        xxx[7][0],
    )
    print(
        xxx[0][1],
        xxx[1][1],
        symbol_1[1],
        xxx[3][1],
        xxx[4][1],
        symbol_1[1],
        xxx[6][1],
        xxx[7][1],
    )
    print(
        xxx[0][2],
        xxx[1][2],
        symbol_1[2],
        xxx[3][2],
        xxx[4][2],
        symbol_1[2],
        xxx[6][2],
        xxx[7][2],
    )
    print(
        xxx[0][3],
        xxx[1][3],
        symbol_1[3],
        xxx[3][3],
        xxx[4][3],
        symbol_1[3],
        xxx[6][3],
        xxx[7][3],
    )
    print(
        xxx[0][4],
        xxx[1][4],
        symbol_1[4],
        xxx[3][4],
        xxx[4][4],
        symbol_1[4],
        xxx[6][4],
        xxx[7][4],
    )
    time.sleep(0.2)
    os.system("cls")
    print(
        xxx[0][0],
        xxx[1][0],
        symbol_2[0],
        xxx[3][0],
        xxx[4][0],
        symbol_2[0],
        xxx[6][0],
        xxx[7][0],
    )
    print(
        xxx[0][1],
        xxx[1][1],
        symbol_2[1],
        xxx[3][1],
        xxx[4][1],
        symbol_2[1],
        xxx[6][1],
        xxx[7][1],
    )
    print(
        xxx[0][2],
        xxx[1][2],
        symbol_2[2],
        xxx[3][2],
        xxx[4][2],
        symbol_2[2],
        xxx[6][2],
        xxx[7][2],
    )
    print(
        xxx[0][3],
        xxx[1][3],
        symbol_2[3],
        xxx[3][3],
        xxx[4][3],
        symbol_2[3],
        xxx[6][3],
        xxx[7][3],
    )
    print(
        xxx[0][4],
        xxx[1][4],
        symbol_2[4],
        xxx[3][4],
        xxx[4][4],
        symbol_2[4],
        xxx[6][4],
        xxx[7][4],
    )
    time.sleep(0.2)
    os.system("cls")
    