def calculate_total_expense(quantity, price_per_item):
    
    total_cost = quantity * price_per_item
    
    
    if quantity > 10:
        total_cost *= 0.9  
    
    
    print(f"The total expenses are: ${total_cost:.2f}")


quantity = int(input("Enter the quantity of items purchased: "))
price_per_item = float(input("Enter the price per item: "))


calculate_total_expense(quantity, price_per_item)

