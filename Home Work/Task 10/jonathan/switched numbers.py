def is_switched_number(number):

    if number < 10 :
        return True

    if number % 10 % 2 != number // 10 % 10 % 2:
        return is_switched_number(number//100)
    elif number % 10 % 2 != 0 and number // 10 % 10 % 2 == 0:
        return is_switched_number(number//100)
    else:
        return False

print(is_switched_number(1634589))