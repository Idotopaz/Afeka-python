# Created on iPad.
#תרגול כמה לשלם למונית
fareRate=10.2
farePerK=1.30
baggageFare=2

range=float(input("how many kilometers will you be driving today?"))
bag=int(input("how many suitcases will you bring?"))
 
sum=float(fareRate+(range*farePerK)+(bag*baggageFare))

print(f"you ride will cost you {sum} $")
