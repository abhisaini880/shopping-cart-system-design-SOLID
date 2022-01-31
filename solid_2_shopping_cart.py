""" Implementing  Open/Closed principle """

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
    def pay(self, order, security_code):
        pass


class DebitPayment(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status(Status.paid.value)


class CreditPayment(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status(Status.paid.value)


class UPIPayment(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing upi payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status(Status.paid.value)


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    print(order.total_price())

    upi_payment = UPIPayment()
    upi_payment.pay(order, "0372846")

    print(order.status)
