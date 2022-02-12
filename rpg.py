#! /usr/bin/env python3

class Character():

    def __init__(self, name, age):
        self.name = name
        self.age  = age
        self.level = 1
        self.inventory = []
        
        print("Hurray! A new character was created! Their name is {}!".format(self.name))

    def agea(self): return self.age


    def add_age(self, age):
        self.age = self.age + age


    def add_to_inventory(self, item):
        self.inventory.append(item)
        return self.inventory
        

class Items():
    def __init__(self, name, gold_value):
        self.name = name
        self.gold_value = gold_value


class Food(Items):
    def eat(self):
        print("Yumm!")


class IndianFood(Food):
    pass

def main():
    tanmay = Character("Tanmay", 23)
    chinmay = Character("Chinmay", 26)


    chicken_curry = Food("Chicken Curry", 10)

    chicken_curry.eat()


if __name__ == "__main__":
    main()
