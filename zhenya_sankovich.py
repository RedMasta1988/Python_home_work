example = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. \
А у нас управдом — друг человека!"
example_2 = example.split()
print("Шаг1 - Количество символов -", len(example))
print("Шаг2 - Развернуть строку -", example[::-1])
print("Шаг3 - Каждое слово с большой буквы -", example.title()) 
print("Шаг4 - Весь текст прописными буквами -", example.upper())
print(
    "Шаг5 - Число вхождений 'нд','ам','о' в строку -",
    str(example.count("нд"))
    + ","
    + str(example.count("ам"))
    + ","
    + str(example.count("о")),
)
print("Шаг6 - Состоит ли строка из цифр -", example.isdigit())
print("Шаг7 - Развернуть предложение -", " ".join(example_2[::-1]))
print("Шаг8 - Исходная строка -", example)
