#zip used to print to combine two diif list at one list to print

from traceback import print_tb


name=["riaydh", "tamim", "ridoy"]
color=["beige", "black", "blue"]

for name, color in zip(name, color):
    print(f"{name} -> {color}")