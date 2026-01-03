from sys import float_repr_style


def add(num1, num2):
    return num1+num2

print(add(10,12))

def dual(num1, num2):
    return num1+num2, num1*num2

a, b= dual(10, 12)

print(f"addition: {a} Multiplication: {b}")

#sales report generator
def fetch_data():
    print(f"fetching data")
def filter_data():
    print("filtering the data")
def summary():
    print("summarizing the data")

def create_report():
    fetch_data()
    filter_data()
    summary()
    print("report is ready!")

create_report()
