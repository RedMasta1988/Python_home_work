import os
import datetime
import time
import functools

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


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        time.sleep(0.5)
        os.system("cls")
        value = func(*args, **kwargs)
        return value

    return wrapper_decorator


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


@decorator
def first_layer():
    tn_new = tn_func()
    for i in range(5):
        print(
            tn_new[0][i],
            tn_new[1][i],
            symbol_1[i],
            tn_new[3][i],
            tn_new[4][i],
            symbol_1[i],
            tn_new[6][i],
            tn_new[7][i],
        )


@decorator
def second_layer():
    tn_new = tn_func()
    for i in range(5):
        print(
            tn_new[0][i],
            tn_new[1][i],
            symbol_2[i],
            tn_new[3][i],
            tn_new[4][i],
            symbol_2[i],
            tn_new[6][i],
            tn_new[7][i],
        )


while True:
    first_layer()

    second_layer()
