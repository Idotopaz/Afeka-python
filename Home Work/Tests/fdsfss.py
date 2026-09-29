import math
def is_rolling_list(l1):
    counter = 0
    check = False
    if counter == len(l1):
        return True
    if len(l1) <= 1:
        return False

    sfarot = int(1 + math.log10(l1[counter + 1]))
    print(counter)
    if l1[counter] % 10 != l1[counter + 1] // (10 ^ (sfarot - 1)):
        return False
    else:
        counter += 1
        return counter + is_rolling_list(l1)

print(is_rolling_list([123,345,564,478]))