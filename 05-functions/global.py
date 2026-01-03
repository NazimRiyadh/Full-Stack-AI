from ast import Global


chai_order="Lemon"
def chai_counter():
    def print_order():
        global chai_order
        chai_order="Ginger"
    print_order()
    print(f"Updated Chai: {chai_order}")

chai_counter()
