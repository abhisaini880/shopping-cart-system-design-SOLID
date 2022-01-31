""" Shopping cart design before implementing SOLID principles """


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

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            self.status = "paymentFailed"
            raise Exception(f"Unknown payment type: {payment_type}")


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    print(order.total_price())
    order.pay("debit", "0372846")
