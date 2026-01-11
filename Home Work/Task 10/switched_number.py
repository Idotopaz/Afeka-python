def is_switched_number(number):
    if number < 10:
        return True
    if (number % 10) % 2 != (number // 10 % 10) % 2:
        return is_switched_number(number // 10)
    return False

def main():
    print(is_switched_number(123456788))

if __name__=="__main__":
    main()