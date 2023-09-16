class Flower:
    def __init__(self, name, withering, price):
        self.name = name
        self.withering = withering
        self.price = price


class Rosa(Flower):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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
        for i in bouquet_sorted:
            print(i.name)

    def bouquet_search(self,flower_search):
        for i in self.all_flower:
            if flower_search == i.name:
                print("Цветок:",flower_search,", есть в букете")
                return
        else:
            print("Цветка:",flower_search,", нет в букете")


tulip = Flower("Тюльпан", 2, 5)
rosa = Flower("Роза", 5, 12)
chamomile = Flower("Ромашка", 8, 3)
pion = Flower("Пион", 4, 10)


all_flower = [tulip, rosa, chamomile, pion]


bouquet_1 = MyBouquet([tulip, rosa, chamomile, pion])
bouquet_1.bouquet_price()
bouquet_1.bouquet_withering()
bouquet_1.bouquet_sorted()
bouquet_1.bouquet_search("Пион")


bouquet_2 = MyBouquet([tulip, rosa, chamomile])
bouquet_2.bouquet_price()
bouquet_2.bouquet_withering()
bouquet_2.bouquet_sorted()
bouquet_2.bouquet_search("Пион")


bouquet_3 = MyBouquet([rosa, chamomile])
bouquet_3.bouquet_price()
bouquet_3.bouquet_withering()
bouquet_3.bouquet_sorted()
bouquet_3.bouquet_search("Пион")
