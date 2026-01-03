users=[
    {"name": "riyadh", "total": 250, "coupon":"D"},
    {"name": "tamim", "total": 300, "coupon":"B"},
    {"name": "ridoy", "total": 180, "coupon":"C"},
    {"name": "oni", "total": 120, "coupon":"A"}
]

discount={
    "A":(0.2, 0),
    "B":(0, 20),
    "C":(0, 30),
    "D":(0.1, 0)
}

for user in users:
    percent, fixed=discount.get(user["coupon"], (0,0))
    print(f"{user["name"]} got {percent} % & flat {fixed} tk discount, pay: {user["total"]-(user["total"]*percent)-fixed} tk!")