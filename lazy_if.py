num_1, num_2, num_3 = int(input()), int(input()), int(input())
result_1 = num_1 and num_2 and num_3 and "Нет нулевых значений!!!"
print(result_1)
result_2 = num_1 or num_2 or num_3 or "Введены все нули!"
print(result_2)
if num_1 > num_2 + num_3:
    print(num_1 - num_2 - num_3)
if num_1 < num_2 + num_3:
    print(num_2 + num_3 - num_1)
if num_1 > 50 and (num_2 > num_1 or num_3 > num_1):
    print("Вася")
if num_1 > 5 or num_2 == 7 and num_3 == 7:
    print("Петя")
