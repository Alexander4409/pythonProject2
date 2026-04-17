#Пораждающие
# Одиночка (Singleton) - гарантирует, что у класса есть только один экземпляр.
# class DataBase:
#     _instance = None
#     logs = []
#     def __new__(cls):
#         if cls._instance is None:
#             print("Data base connection")
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
# db1 = DataBase()
# db2 = DataBase()
#
# print(db1 is db2)

#фабрика - нужен когда заранее не знаем какие дополнительные у нас будут классы
class Transport:
    def delivery(self):
        pass

class Car(Transport):
    def delivery(self):
        return "delivery by car"

class Scooter(Transport):
    def delivery(self):
        return "delivery by scooter"

class DeliveryService:
    def get_transport(self,type):
        if type == "fast":
            return Scooter()
        if type == "heavy":
            return Car()

service = DeliveryService()

my_delivery = service.get_transport("fast")
my_delivery1 = service.get_transport("heavy")
print(my_delivery1.delivery())

# Абстрактная фабрика



#Структурные





#Поведенческие паттерны