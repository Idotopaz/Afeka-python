three_room_apartment = 120
four_room_apartment = 150
five_room_apartment = 180
five_room_duplex = 200

num_of_rooms = int(input("how many rooms do you have? "))

if num_of_rooms >5:
    print("invalid input no apartments with more then 5 rooms")
elif num_of_rooms<3:
    print("invalid input no apartments with less then 3 rooms")

elif num_of_rooms == 3:
    price = three_room_apartment
elif num_of_rooms == 4:
    price = four_room_apartment
elif num_of_rooms == 5:
    duplex = input("do you have a duplex? (yes/no)")
    if duplex == "no":
        price = five_room_apartment
    else:
        price = five_room_duplex

print(f"Please pay {price} ILS")





