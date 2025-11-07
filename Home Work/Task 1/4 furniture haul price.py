price_per_km=5
price_per_floor=1
tip=0.1

furniture_price=float(input("what is the price of the furniture? "))
km_for_transport=float(input("how many kilometers for the transportation? "))
floors=int(input("how many floors? "))
furniture_weight=float(input("what is the weight of the furniture? "))

km_cost=price_per_km*km_for_transport
floor_cost=price_per_floor*floors*furniture_weight
tip_cost=tip*furniture_price

total_cost=float(furniture_price+km_cost+floor_cost+tip_cost)

print(f"Please pay {total_cost} ILS")


