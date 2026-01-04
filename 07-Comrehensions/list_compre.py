"""
sytax:
[expression for item in iterable if condition]

applicatons:
-> filter
-> covertion
and so more

Why comprehensions are used?
mainly to write clean and effcient code

Different types of comp:
List compre
Set compre
Dictinary compre
Generator

"""

menu=[
    "masala",
    "green",
    "iced tea",
    "ginger",
    "ice coffee"
]

#[expression for item in iterable if condition]
cold_tea= [cold for cold in menu if "ice" in cold]
print(cold_tea)