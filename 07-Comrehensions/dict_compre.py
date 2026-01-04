tea_prices_tk = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_usd={
    tea:price/120 for tea, price in tea_prices_tk.items() 
}

print(tea_usd)
