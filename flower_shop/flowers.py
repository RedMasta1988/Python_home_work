class Flower:
    def __init__(self, name=str, withering=int, price=int):
        self.name = name
        self.withering = withering
        self.price = price


class Rosa(Flower):
    def __init__(self, lepestki=int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lepestki = lepestki


class Pion(Flower):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Tulip(Flower):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Chamomile(Flower):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MyBouquet:
    def __init__(self, all_flower):
        self.all_flower = all_flower

    def bouquet_price(self):
        bouquet_price = sum(i.price for i in self.all_flower)
        print("Стоимость букета: ", bouquet_price, "byn")

    def bouquet_withering(self):
        bouquet_withering = sum(i.withering for i in self.all_flower) / len(
            self.all_flower
        )
        if bouquet_withering >= 5:
            print("Время жизни букета: ", bouquet_withering, "дней")
        else:
            print("Время увядания букета: ", bouquet_withering, "дня")

    def bouquet_sorted(self):
        bouquet_sorted = sorted(self.all_flower, key=lambda flower: flower.price)
        print("Сортировка по цене: ", end=" ")
        for i in bouquet_sorted:
            print(i.name, end=" ")
        print()

    def bouquet_search(self, flower_search):
        for i in self.all_flower:
            if flower_search == i.name:
                print("Цветок:", flower_search, ", есть в букете")
                break
        else:
            print("Цветка:", flower_search, ", нет в букете")

    def bouquet_info(self):
        return self.bouquet_price(), self.bouquet_withering()


tulip = Tulip("Тюльпан", 2, 5)
rosa = Rosa(25, "Роза", 5, 12)
chamomile = Chamomile("Ромашка", 8, 3)
pion = Pion("Пион", 4, 10)


bouquet_1 = MyBouquet([tulip, rosa, chamomile, pion])
bouquet_1.bouquet_info()
bouquet_1.bouquet_sorted()
bouquet_1.bouquet_search("Пион")
print("*" * 30)

bouquet_2 = MyBouquet([tulip, rosa, chamomile])
bouquet_2.bouquet_info()
bouquet_2.bouquet_sorted()
bouquet_2.bouquet_search("Пион")
print("*" * 30)

bouquet_3 = MyBouquet([rosa, chamomile])
bouquet_3.bouquet_info()
bouquet_3.bouquet_sorted()
bouquet_3.bouquet_search("Пион")
print("*" * 30)
