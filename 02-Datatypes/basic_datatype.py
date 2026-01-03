#immutable-- dont judge mutablity using value but using identity
import numbers
from pickle import ADDITEMS


milage=10
print(f"milage id before: {id(milage)}")
milage=100
print(f"milage id after: {id(milage)}")
print(milage)

#mytable
#id doesn't hang the same for mutable objects
company=set()
company.add("Google")
print(f"company id: {id(company)}")
company.add("Amazon")
print(f"company id: {id(company)}")


#int
first=43
second=20
print(f"addtion: {first+second}")
print(f"power: {first ** second}")
print(f"remainder: {first%second}")
print(f"floor: {first//second}")

num=1_00_00_000 #readablity is great in python
print(num)


from ast import Not


wait=False
riyadh=True
time=5
print(wait+time)#upcasting (thinks true as 1, false is 0)
print(wait-time)

print(wait and riyadh)
print(wait or riyadh)
print(not(riyadh))


import sys


ideal=94.5
map=94.4

print(ideal-map)
print(sys.float_info)

method= "Zettel_kasten"
tool= "Obsidian"
print(f"{tool} tool uses {method} method")

print(f"first cut: {method[:7]}")
print(f"second cut: {method[7:]}")
print(f"reversing: {method[:-1]}")

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")








