height, weight = int(input("Рост: ")), int(input("Вес: "))
bmi = round(weight / ((height / 100) ** 2), 1)
print("Ваш индекс массы тела:", bmi)
a_bmi, b_bmi = 20, 50
a1 = round((bmi - a_bmi) / 2) * "="
b1 = round((b_bmi - bmi) / 2) * "="
print(str(a_bmi) + a1 + "|" + b1 + str(b_bmi))
