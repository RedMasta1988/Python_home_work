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
            
    for i in range(5):
        print(
            tn_new[0][i],
            tn_new[1][i],
            symbol_1[i],
            tn_new[2][i],
            tn_new[3][i],
            symbol_1[i],
            tn_new[4][i],
            tn_new[5][i],
        )
    time.sleep(0.2)
    os.system("cls")
    
    for i in range(5):
        print(
            tn_new[0][i],
            tn_new[1][i],
            symbol_2[i],
            tn_new[2][i],
            tn_new[3][i],
            symbol_2[i],
            tn_new[4][i],
            tn_new[5][i],
        )
    time.sleep(0.2)
    os.system("cls")
    
