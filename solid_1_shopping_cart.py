""" Implementing Single responsibility principle """


class Order:
    def __init__(self):
        self.items = []
        self.status = "open"

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


class PaymentProcessor:
    def payDebit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status("paid")

    def payCredit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status("paid")


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    print(order.total_price())

    pay = PaymentProcessor()
    pay.payDebit(order, "0372846")
