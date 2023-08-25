height, weight = float(input("Рост: ")), float(input("Вес: "))
BMI = round(weight / ((height / 100) ** 2),1)
print("Ваш индекс массы тела:", BMI)
a_MBI, b_MBI = 10, 60
a1 = round((BMI - a_MBI) / 2) * "="
b1 = round((b_MBI - BMI) / 2) * "="
print(str(a_MBI) + a1 + "|" + b1 + str(b_MBI))
