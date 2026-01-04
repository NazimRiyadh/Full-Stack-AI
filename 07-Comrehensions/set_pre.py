fav_chai=[
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_tea={unq for unq in fav_chai}
print(unique_tea)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unq_spice={spice for ingred in recipes.values() for spice in ingred}
print(unq_spice)