def calculate_trip_cost(kilometers_to_drive, liters_per_kilometer, price_per_liter):
   
    total_liters = kilometers_to_drive * liters_per_kilometer
    
   
    total_cost = total_liters * price_per_liter
    
   
    print(f"The total cost of the trip is: ${total_cost:.2f}")


kilometers_to_drive = float(input("Enter the kilometers to drive: "))
liters_per_kilometer = float(input("Enter the car's fuel consumption (liters per kilometer): "))
price_per_liter = float(input("Enter the price per liter of fuel: "))


calculate_trip_cost(kilometers_to_drive, liters_per_kilometer, price_per_liter)

