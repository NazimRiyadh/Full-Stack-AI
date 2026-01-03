for x in range(1,10):
    print(x)

name=["riyadh","tamim", "ridoy"]
for order in name:
    print(order)

for index,order in enumerate(name, start=0):
    print(f"merit: {index} -> {order}")

temp=10
while(temp>0):
    print(temp)
    temp-=1