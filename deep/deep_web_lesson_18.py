# Абстрактная фабрика

# #--- 1. Cемейство стульев---
# class Chair:
#     def sit_on(self):pass
#
#
# class VictorianChair(Chair):
#     def sit_on(self):
#         return "Sit on vict chair"
#
#
# class ModernChair(Chair):
#     def sit_on(self):
#         return "Sit on modern chair"
#
# # --- 2. Семейство Диванов ---
# class Sofa:
#     def lie_on(self): pass
#
#
# class VictSofa(Sofa):
#     def lie_on(self):
#         return "lie on vict Sofa"
#
#
# class ModernSofa(Sofa):
#     def lie_on(self):
#         return "lie on modern Sofa"
#
# #--- 3. Абстрактная фабрика ---
#
# class FurnitureFactory:
#     def create_chair(self): pass
#     def create_sofa(self):pass
#
# #--- 4. Конкретные фабрики ---
#
# class VictorianFactory(FurnitureFactory):
#     def create_chair(self):
#         return VictorianChair()
#
#     def create_sofa(self):
#         return VictSofa()
#
# class ModernFactory(FurnitureFactory):
#     def create_chair(self):
#         return ModernChair()
#
#     def create_sofa(self):
#         return ModernSofa()
#
# # использование
#
# def setup_room(factory: FurnitureFactory):
#     chair = factory.create_chair()
#     sofa = factory.create_sofa()
#     print(chair.sit_on())
#     print(sofa.lie_on())
#
# setup_room(VictorianFactory())
#
# setup_room(ModernFactory())

#Строитель
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.toppings = []

    def __str__(self):
        return (f"Pizza on {self.dough} dough, "
                f"sauce: {self.sauce}, "
                f"with: {', '.join(self.toppings) if self.toppings else 'empty'}")


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self,dough):
        self.pizza.dough = dough
        return self

    def set_sauce(self,sauce):
        self.pizza.sauce = sauce
        return self

    def add_cheese(self):
        self.pizza.toppings.append("cheese")
        return self

    def add_peperoni(self):
        self.pizza.toppings.append("peperoni")
        return self

    def add_mushrooms(self):
        self.pizza.toppings.append("mushrooms")
        return self

    def build(self):
        return self.pizza

#сборка пиццы
margarita = (PizzaBuilder()
             .set_dough("thin")
             .set_sauce("tomato")
             .add_cheese()
             .build())

pepperoni_pizza =(PizzaBuilder()
                  .set_dough("thick")
                  .set_sauce("tomato")
                  .add_cheese()
                  .add_peperoni()
                  .add_mushrooms()
                  .build())


print(margarita)
print(pepperoni_pizza)

