num=int(input("enter a 5 digit number: ")) #123

dig0=num%10 #5
dig1=num//10%10 #4
dig2=num//100%10 #3
dig3=num//1000%10
dig4=num//10000%10
# print(dig0,dig1,dig2,dig3,dig4)

avgP=(dig0+dig2+dig4)/3
#print(avgP)
avgN=(dig1+dig3)/2
#print(avgN)

print(avgP==avgN)








