toast_price=12
cheap_topping_price=2
expensive_topping_price=3

num_cheap_toppings=int(input("how many cheap toppings would you like? "))
num_expensive_toppings=int(input("how many expensive toppings would you like? "))

total_price=float(toast_price+(num_cheap_toppings*cheap_topping_price)+(num_expensive_toppings*expensive_topping_price))

print(f"Please pay {total_price} ILS")
