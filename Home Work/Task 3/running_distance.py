rest_pulse = int(input("Enter your resting heart rate: "))
weeks_trained = float(input("how many weeks have you been training for? "))

if rest_pulse>70 or weeks_trained<3:
    run = 3
elif 3<=weeks_trained<=4:
    run = 5
elif weeks_trained>=5 and 60<=rest_pulse<=70:
    run = 8
else:
    run = 10
print(f"you should run {run} KM")