#Фасад

#Логика
# class WareHouse:
#     def check_stock(self,item) -> bool:
#         print(f'[Склад] Проверка наличия товара: {item}')
#         return True
#
# class PaymentSystem:
#     def process_payment(self,amount: float) -> bool:
#         print(f'[Оплата] списание суммы: {amount} руб.')
#         return True
#
# class Logistics:
#     def ship_item(self,item: str):
#         print(f"[Доставка] Товар {item} передан в доставку")
#
#
# class OrderFacade:
#     def __init__(self):
#         self.warehouse = WareHouse()
#         self.payment = PaymentSystem()
#         self.logistics = Logistics()
#
#     def create_order(self, item: str, price: float):
#         print("___Старт сбора заказа___")
#
#         if not self.warehouse.check_stock(item):
#             print("___Error___")
#             return
#
#         if not self.payment.process_payment(price):
#             print("___Error___")
#             return
#
#
#         self.logistics.ship_item(item)
#         print("_Заказ успешно оформлен_")
#         return
#
#
#
# shop = OrderFacade()
# shop.create_order(item="Phone", price=23300.0)

#Прокси
#Компоновщик


#Поведенческие паттерны

#Стратегия

from abc import ABC, abstractmethod

class DeliveryStrategy(ABC):
    @abstractmethod
    def calc_cost(self,weight:float) -> float:
        '''Расчет стоймости доставки на основе веса груза'''
        pass


class CourierDelivery(DeliveryStrategy):
    def calc_cost(self,weight:float) -> float:
        return 300.0 + (weight * 50.0)

class PostDelivery(DeliveryStrategy):
    def calc_cost(self,weight:float) -> float:
        return weight * 30.0

class PickUpDelivery(DeliveryStrategy):
    def calc_cost(self,weight:float) -> float:
        return 0.0


class OrderContext:
    def __init__(self,strategy: DeliveryStrategy):
        self._strategy=  strategy

    def set_strategy(self, strategy:DeliveryStrategy):
        self._strategy=strategy

    def process_order(self,item:str, weight: float):
        cost = self._strategy.calc_cost(weight)
        print(f"Заказ : {item} оформлен. Стоймость доставки - {cost} руб.")


item_name = "Laptop"
item_weight = 5.0

print("---Выбрана доставка - Курьером---")
order = OrderContext(CourierDelivery())
order.process_order(item_name,item_weight)

print("---Выбрана доставка - Почтой---")
order = OrderContext(PostDelivery())
order.process_order(item_name,item_weight)

print("---Выбрана доставка - Самовывоз---")
order = OrderContext(PickUpDelivery())
order.process_order(item_name,item_weight)

#Наблюдатель
#Итератор
#Состояние
#Цепочка обязанностей
