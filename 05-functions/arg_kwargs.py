from token import MINEQUAL


chai=[1,2,3]
def update_chai(chai):
    chai[2]=4
update_chai(chai)
print(chai)

#args
def chai(type, sweet, milk):
    print(type, sweet, milk)
chai("ginger", "2tsp", "1tsp")

#kwargs ( in kwargs you pass the arguments with paramter name, so order doesn't bother)
chai(sweet='1ts',milk= "1tsp",type= "lemon")

#(*args, **kwargs)
def chaii(*arg, **kwargs):
    print(f"args: {arg}")
    print(f"kwargs: {kwargs}")
chaii("cinamon", "ginger", "lemon", type="liqpur", milk="more")
