
lib_card = input("Library card type (adult/kid): ")
books_at_home = int(input("how many books do you have at home: "))

if lib_card == "adult" and books_at_home<5 or lib_card == "kid" and books_at_home<3:
    rented_book_home_duration = input("do you have a book above 1 month at home (yes/no):  ")
    print(f"can rent another book: {rented_book_home_duration == "no"}")

else:
    print(f"can rent another book: {False}")
    






