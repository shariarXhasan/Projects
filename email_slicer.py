email = input("Enter your mail address: ")

index = email.index("@")

username = email[:index]
domain = email[index:]

print(f"Your user name is {username} and your domain is {domain}")