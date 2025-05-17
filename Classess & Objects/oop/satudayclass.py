class Orderreceived:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)


.

class OrderProcess:
    def __init__(self, orderrepo):
        self.orderrepo = orderrepo

    def process_order(self, order):
        # Process the order (e.g., payment, shipping)
        print(f"Processing order: {order}")
        self.orderrepo.add_order(order)

class OrderServe:
    def __init__(self, orderrepo):
        self.orderrepo = orderrepo

    def serve_order(self, order):
        # Serve the order (e.g., delivery)
        print(f"Serving order: {order}")