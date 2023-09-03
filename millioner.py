import os
import random
import colorama
from colorama import Fore, Style

colorama.init()
os.system("cls")
print()
print("Всем Привет! С Вами игра 'КТО ХОЧЕТ СТАТЬ МИЛЛИОНЕРОМ!'")
print()
name = input("Как Вас зовут? ")
os.system("cls")
print()
print("Здравствуйте, ", name)
print()
print(
    "И так, немного о правилах игры:\nУ нас есть 10 вопрос, в каждом вопросе 4 варианта ответа \
и только 1 ответ правильный.\nЗа каждый правильный ответ Вам будет начисляться определенная сумма. \
Так же есть 3 подсказки:\n50/50, звонок другу и помощь зала. \
Каждую подсказку можно использовать только 1 раз,\nпосле чего она пропадает."
)
print()
input("Если Вы готовы, то жмите Enter... ")
os.system("cls")
bank = 0
random_fifty_fifty = []
questions = [
    "Столица Республики Беларусь?",
    "Что есть на лице у каждого человека?",
    "Какая фигура получила имя летчика Петра Нестерова?",
    "Бочонок с каким числом в русском лото принято называть «топориками»?",
    "Какой сад воспел Алексей Глызин?",
    "Что в книге Джеймса Крюса мальчик Тим Талер променял на возможность выиграть любое пари?",
    "Какое растение коренные жители Мексики называли маисом?",
    "Что из перечисленного название концертного зала, а не стадиона?",
    "В какой стране находится храм, который Книга рекордов Гиннесса называет самым большим христианским храмом мира?",
    "В каком городе происходит действие пушкинского «Каменного гостя»?",
]
answers = [
    ["Минск", "Лондон", "Пекин", "Рим"],
    ["Несушка", "Носильщица", "Переносчица", "Переносица"],
    ["Штопор", "Мертвая петля", "Горка", "Бочка"],
    ["11", "77", "44", "69"],
    ["Летний", "Осенний", "Зимний", "Весенний"],
    ["Слезы", "Смех", "Веснушки", "Возраст"],
    ["Кукурузу", "Картофель", "Томат", "Табак"],
    ["«Камп Ноу»", "«Альберт-холл»", "«Сан-Сиро»", "«Энфилд»"],
    ["ЮАР", "Аргентина", "Китай", "Кот-д Ивуар"],
    ["Мадрид", "Севилья", "Толедо", "Валенсия"],
]
true_answers = [
    "Минск",
    "Переносица",
    "Мертвая петля",
    "77",
    "Зимний",
    "Смех",
    "Кукурузу",
    "«Альберт-холл»",
    "Кот-д Ивуар",
    "Мадрид",
]
help = ["50/50", "звонок другу", "помощь зала"]
for i in range(1, 11):
    print("Вопрос №" + str(i), questions[i - 1])
    for ans in range(1, 5):
        print(ans, answers[i - 1][ans - 1])
    print(30 * "-")
    if len(help) == 1:
        print("У Вас есть", len(help), "подсказка:")
    if len(help) == 0:
        print("У Вас есть", len(help), "подсказок:")
    if len(help) == 2 or len(help) == 3:
        print("У Вас есть", len(help), "подсказки:")
    for hp in range(len(help)):
        if len(help) > 0:
            print(hp + 5, help[hp])
    print(30 * "-")
    your_answer = int(input("Ваш вариант ответа: "))
    while your_answer > (len(help) + 4) or your_answer == 0:
        print("Попробуйте ещё раз ")
        your_answer = int(input("Ваш вариант ответа: "))
    if 8 > your_answer > 4 and (
        help[your_answer - 5] == "звонок другу"
        or help[your_answer - 5] == "помощь зала"
    ):
        random_number = random.randint(0, 3)
        help.pop(your_answer - 5)
        print("Возможно ответ ", answers[i - 1][random_number])
        print(30 * "-")
        your_answer = int(input("Ваш вариант ответа: "))
        while your_answer > (len(help) + 4) or your_answer == 0:
            print("Попробуйте ещё раз ")
            your_answer = int(input("Ваш вариант ответа: "))
    if your_answer == 5 and help[your_answer - 5] == "50/50":
        while len(random_fifty_fifty) < 2:
            random_number = random.randint(0, 3)
            if (
                answers[i - 1][random_number] not in true_answers
                and answers[i - 1][random_number] not in random_fifty_fifty
            ):
                random_fifty_fifty.append(answers[i - 1][random_number])
        help.pop(your_answer - 5)
        print("Возможно ответ ", random_fifty_fifty[0], random_fifty_fifty[1])
        print(30 * "-")
        your_answer = int(input("Ваш вариант ответа: "))
        while your_answer > (len(help) + 4) or your_answer == 0:
            print("Попробуйте ещё раз ")
            your_answer = int(input("Ваш вариант ответа: "))
    if answers[i - 1][your_answer - 1] in true_answers:
        bank += 100_000
        print(30 * "-")
        print(Fore.GREEN + "Правильно!")
        print(Fore.GREEN + "Ваш выигрыш составляет", bank, "BYN")
        print(Style.RESET_ALL)
        input("Если Вы готовы продолжить, то жмите Enter... ")
        os.system("cls")
    else:
        print(30 * "-")
        print(Fore.RED + name, ", очень жаль, но Вы проиграли")
        print(Style.RESET_ALL)
        break
if bank == 1000_000:
    a = round((29 - len(name)) / 2)
    print()
    print()
    print(29 * "-")
    print("----" + Fore.YELLOW + "ПОЗДРАВЛЯЕМ С ПОБЕДОЙ" + Style.RESET_ALL + "----")
    print(a * "-" + Fore.YELLOW + name + Style.RESET_ALL + a * "-")
    print("--------" + Fore.YELLOW + "ВЫ МИЛЛИОНЕР" + Style.RESET_ALL + "---------")
    print(29 * "-")
    print()
    print()
