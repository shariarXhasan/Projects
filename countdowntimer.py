import time

my_time = int(input("Enter your time: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int ((x / 60) % 60) % 60
    print (f"{hours:00}:{minutes:00}:{seconds:02}")
    time.sleep(1)



print("Timer up!")