B_average = float(input("what is your bagrut average: "))
P_average = int(input("what is your psicometry grade: "))


A=False
if B_average>=102:
    A=True
elif P_average>= 700:
    math_part = int(input("what is your math grade: "))
    english_part = int(input("what is your english grade: "))
    if math_part>=145 and english_part>120:
        A=True
elif ((P_average*0.8)+(B_average/1.2))>=600:
    #print(((P_average*0.8)+(B_average/1.2)))
    A=True

print(f"Can the student be accepted to lilput: {A}")

