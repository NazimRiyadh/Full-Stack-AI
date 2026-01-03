def chai_counter():
    chai_order="Lemon"
    def print_order():
        nonlocal chai_order
        chai_order="Ginger"
    print_order()
    print(f"Updated Chai: {chai_order}")

chai_counter()
