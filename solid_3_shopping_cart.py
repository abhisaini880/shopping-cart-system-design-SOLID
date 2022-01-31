""" Implementing  Liskov substitution principle """

from enum import Enum
from abc import ABC, abstractmethod


class Status(Enum):
    open = 1
    paid = 2
    paymentFailed = 3


class Order:
    def __init__(self):
        self.items = []
        self.status = Status.open.value

    def add_item(self, name, quantity, price):
        item = {"name": name, "quantity": quantity, "price": price}
        self.items.append(item)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item["quantity"] * item["price"]
        return total

    def set_status(self, status):
        self.status = status


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitPayment(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status(Status.paid.value)


class CreditPayment(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status(Status.paid.value)


class UPIPayment(PaymentProcessor):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, order):
        print("Processing upi payment type")
        print(f"Verifying upi_id: {self.upi_id}")
        order.set_status(Status.paid.value)


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    print(order.total_price())

    upi_payment = UPIPayment("1234@ybl")
    upi_payment.pay(order)

    print(order.status)
