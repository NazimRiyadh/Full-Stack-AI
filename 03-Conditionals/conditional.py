from ast import MatchAs, match_case


cgpa=3.96
min_grade=3.5

eligible= True if cgpa>3.75 & min_grade>3.5 else False

if cgpa>3.75 & min_grade>3.5: 
    print("You are eligible for the scholarship")

coektype= input("Enter the type of coke: ")

match coektype:
    case "Coke":
        print("Coke is 10 SAR")
    case "Pepsi":
        print("Pepsi is 10 SAR")
    case "Sprite":
        print("Sprite is 10 SAR")
    case _:
        print("Invalid coke type")

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")

