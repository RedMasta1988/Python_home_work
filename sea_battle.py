import os
from random import *
from pygame import *

os.system("cls")


class Color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (
            Color.WARNING
            + f"Добро пожаловать в игру Морской Бой, {self.name}!"
            + Color.ENDC
        )


class GamePole:
    def __init__(self, size):
        self.size = size
        self.tabl = [["⬜" for _ in range(1, size + 1)] for _ in range(1, size + 1)]

    def pole(self):
        print(
            "   ",
            "а " + "б " + "в " + "г " + "д " + "е " + "ж " + "з " + "и " + "к",
        )
        for num in range(self.size):
            for row in self.tabl:
                if num + 1 < 10:
                    print(num + 1, "", end=" ")
                else:
                    print(num + 1, end=" ")
                print("".join(row))
            return


class Ship:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity


class Game:
    pass


player_1 = Player(input("Игрок №1 введите своё имя: "))
print(player_1)
time.wait(5000)
os.system("cls")

player_2 = Player(input("Игрок №2 введите своё имя: "))
print(player_2)
time.wait(5000)
os.system("cls")


ship_1 = Ship("⬛", 4)
ship_2 = Ship("⬛⬛", 3)
ship_3 = Ship("⬛⬛⬛", 2)
ship_4 = Ship("⬛⬛⬛⬛", 1)
tabl_1 = GamePole(10)
tabl_2 = GamePole(10)
time.wait(5000)
