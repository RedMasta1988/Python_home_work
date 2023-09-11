bank = 0
random_fifty_fifty = []
help = ["50/50", "звонок другу", "помощь зала"]

# Когда ответ вне цифровова диапозона
def one_more(your_answer):
    while your_answer > (len(help) + 4) or your_answer == 0 or your_answer == None:
        print("Попробуйте ещё раз, ответ вне цифрового диапозона... ")
        your_answer = int(input("Ваш вариант ответа: "))
    return your_answer

