close = 500
family = 1000
other = 250

years = 50
travel = 50

relationship = input("Enter relationship (family/close/other): ")

if relationship == "family":
    sum=family
else:
    if relationship == "close":
        sum=close
    elif relationship == "other":
        sum=other
    else:
        print("invalid syntax")
        exit()
    years_of_acquaintance = float(input("Enter years of acquaintance: "))
    travel_time = int(input("Enter travel time in hours: "))
    if years_of_acquaintance>3:
        sum+=years
    if travel_time>1:
        sum-=travel


print(f"Recommended gift amount:  NIS"+str(sum))


