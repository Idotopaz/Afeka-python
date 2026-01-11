def has_switched_couple(number):

    if number < 10:
        return False
    if (number % 10) % 2 != (number // 10 % 10) % 2:
        return True
    return has_switched_couple(number // 10)

def main():
    print(has_switched_couple(99999999998))

if __name__ == "__main__":
    main()