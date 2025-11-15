clouds=str(input("are there clouds today? (yes/no): "))
rain_percentage=float(input("what the rain percentage today? "))

should_take_umbrella = (clouds == "yes") and (rain_percentage>70)

print(f"Should I take umbrella today? {should_take_umbrella}")












