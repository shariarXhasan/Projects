principal = 0
rate = 0
time = 0

while principal <=0:
    principal = float(input("Enter the principal: "))
    if principal <=0:
        print("Principal can't be less than 0")

while rate <=0:
    rate = float(input("Enter the rate of your interest:"))
    if rate <= 0:
        print("Rate can't be the less than the 0..")

while time <=0:
    time = float(input("Enter the time period of your interest rate"))
    if time <= 0:
        print("This is impossible to be a time  less than 0...")


total = principal * pow((1+rate / 100), time)

print(f"New balace is after {time} : {total:2f}")