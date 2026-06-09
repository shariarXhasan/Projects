weight = float(input("Enter you body weight: "))
unit = input("Enter your weight (K & L):")

if unit == "K":
    weight = weight * 2.20462
    unit = 'lbs'
elif unit == 'L':
    weight = weight / 2.20462
    unit = 'kgs'
else:
    print('Invalid')

print(f"Your weight is {weight} {unit}")