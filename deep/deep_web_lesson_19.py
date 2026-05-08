#Прототип
# import copy
#
# class Knight:
#     def __init__(self, name, weapon):
#         self.name = name
#         self.weapon = weapon
#         self.achievements = []
#
#     def clone(self):
#         return copy.deepcopy(self)
#
#     def __str__(self):
#         return (f"Knight {self.name}\n"
#                 f"with weapon - {self.weapon}\n"
#                 f"Achievements: {self.achievements}")
#
#
# # 1. Эталонный рыцарь
# prototype_knight = Knight("Artur", "Excalibur")
# prototype_knight.achievements.append("Dragon fighter")
#
# # 2. Клоны для армии
# Knight_clone = prototype_knight.clone()
# Knight_clone.name = "Joe"
# Knight_clone.achievements.append("Fire ball master")
#
# print(prototype_knight)
# print(Knight_clone)



#Структурные

#Декоратор
#@ - декоратор
#1 - Базовый интерфес
# class IterBaseEverage:
#     def get_cost(self):
#         pass
#
#     def get_description(self):
#         pass
#
# #2. Конкретный объект
# class SimpleCoffe(IterBaseEverage):
#     def get_cost(self):
#         return 100
#
#     def get_description(self):
#         return "BlackCoffe"
#
# #3. базовый класс декоратора
# class CoffeDecorator(IterBaseEverage):
#     def __init__(self, coffe):
#         self._decorated_coffe = coffe # - Хранение оборачиваемых в декораторе объектов
#
#     def get_cost(self):
#         return self._decorated_coffe.get_cost()
#
#     def get_description(self):
#         return self._decorated_coffe.get_description()
#
# #4. Конкретные декораторы
# class Milk(CoffeDecorator):
#     def get_cost(self):
#         return super().get_cost() + 50 # +50р за молоко
#
#     def get_description(self):
#         return super().get_description() + ", c  молоком"
#
# class Sirope(CoffeDecorator):
#     def get_cost(self):
#         return super().get_cost() + 30 # + 30р за сироп
#
#     def get_description(self):
#         return super().get_description() + ", ванильный сироп"
#
# my_coffe = SimpleCoffe()
#
# print(f' {my_coffe.get_description()}: {my_coffe.get_cost()} руб.')
#
# my_coffe_with_milk = Milk(my_coffe)
#
# coffe_with_sirope = Sirope(my_coffe_with_milk)
#
# print(f" {coffe_with_sirope.get_description()}: {coffe_with_sirope.get_cost()} руб.")

#Адаптер

class EmailNotifications:
    def send(self,title, text):
        print(f"Email: {title} --> {text}")

class SMSLib:
    def send_sms_message(self,phone, text_body):
        print(f"SMS on: {phone} --> {text_body}")


class SmsAdapter:
    def __init__(self, sms_service, phone_number):
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send(self,title,text):
        text_body = f"{title}:{text}"
        self.sms_service.send_sms_message(self.phone_number,text_body)



def notify_user(notifier):
    notifier.send("Delivery Status", "Your dish is ready!")


email = EmailNotifications()
notify_user(email)

exernal_lib = SMSLib()
adapter = SmsAdapter(exernal_lib, "+000000000")
notify_user(adapter)




#Фасад
#Прокси
#Компоновщик


#Поведенческие паттерны

#Стратегия
#Наблюдатель
#Итератор
#Состояние
#Цепочка обязанностей