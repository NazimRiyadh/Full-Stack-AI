def serve_chai():
    chai_type="ginger"
    print(chai_type)

chai_type="lemon"
serve_chai()

chai_order="Banana"
def chai_counter():
    def print_order():
        chai_order="Ginger"
        print(f"Inner: {chai_order}")
    chai_order="Lemon"
    print_order()
    print(f"Outter: {chai_order}")

chai_counter()
print(f"Global: {chai_order}")

