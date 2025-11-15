num = int(input("input a number that represents a date: "))

#5012025 = 5 01 2025
year = num%10000
#print(year)
month = num//10000%100
#print(month)
day= num//1000000
#print(day)

print(f"The date is {day}/{month}/{year}")
