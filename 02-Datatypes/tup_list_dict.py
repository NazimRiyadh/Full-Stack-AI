#------------tuples------------
'''
siblings=("Rina", "Ridoy", "Rafi", "Riyan")
(ma, borovai,mejhovai, chotovai)= siblings
print(ma)
print(borovai)
#assigining two variable at once
first, second =1,2
print(f"ratio: {first/second}")

#membership test
if "Rina" in siblings:
    print("Rina is a sibling")


#------------lists------------

Company=["Google", "Amazon", "Microsoft", "Apple"]


Company.append("KTinformatik")
print(Company)
Company.remove("Amazon")
print(Company)
Company.pop()#removes from the end
print(Company)

Company.reverse()#reverses the list
print(Company)

Company.sort()#sorts the list
print(Company)

num=[1,2,3,4,5,6,7,8,9,10]
max=max(num)
print(f"max: {max}")
min=min(num)
print(f"min: {min}")


#operator overloading
riyadh=["C+","Java", "Python", "JavaScript", "SQL", "HTML", "CSS"]
abul=[".net", "PHP", "HTML", "CSS"]
all_skill=riyadh+abul
print(all_skill)
#riyadh_advantage=riyadh-abul   can't use that for lists

#---------set---------
set_num={1,2,3,4,5,6,7,8,9,10}
print(set_num)
set_num.add(11)
print(set_num)
set_num.remove(11)
print(set_num)
set_num.pop()
print(set_num)


# you can also use '|' '&' for the operations

'''
#------------dictionaries------------
student={"name": "Rina", "age": 20, "city": "Riyadh"}
print(student)

student["group"]="A"

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(f"{key}: {value}")












