foods = []
prices = []
total = 0


while True:

    food = input("Enter your food name, if you done then press 'q': ")
    if food == 'q':
        break

    else:
        price = float(input(f"Enter your price of {food}: "))
        foods.append(food)
        prices.append(price)



print("---Your cart box----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nYour total is {total}")
