attandance_precentage=float(input("Enter the student's attendance precentage: "))
handIn_precentage=float(input("Enter the student's hand in hw precentage: "))
exercise5=str(input("Has the student hand in assignment? (yes/no): "))

#print(exercise5=="yes"
yes_list = ["yes","Yes"," yes"," Yes"]

print(f"can take the test? {attandance_precentage>=80 and handIn_precentage>=70 and exercise5 in yes_list}")




