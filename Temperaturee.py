temp = float(input("Inter your temperature..."))
unit = input("Inter your needed temperature...( C or K)")

if unit == 'C':
    temp = ((9 * temp) / 5+ 32)
    unit = ("Calcious")
elif unit == 'Farentheight':
    temp = ((temp - 32) * 5 / 9)
else:
    print('Void')
print(f"The temperature {temp} {unit}")