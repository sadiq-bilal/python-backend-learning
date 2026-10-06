# Example 1 — First program

print("Hello, World!")



# Example 2 — Variables and print together

city = "Hyderabad"
year = 2026
print("City:", city)      
print("Year:", year)
print(city, year)



# Example 3 — Dynamic typing in action

value = 10
print(value, type(value))     # 10 <class 'int'>
value = "ten"                  # allowed: the name now points to a string
print(value, type(value))     # ten <class 'str'>



# Example 4 — Swapping values

first = "React"
second = "Python"
first, second = second, first
print(first, second)          # Python React



# Example 5 — Reading input

name = input("What is your name? ")
print("Nice to meet you,", name)
print("Your name has", len(name), "letters")



# Example 6 — Realistic data: a user record
# Data a backend might receive when someone registers

username = "sadiq_dev"
email = "sadiq@example.com"
age = 24
is_active = True
last_login = None            # user has never logged in yet
print("Username:", username)
print("Email:", email)
print("Age:", age)
print("Active:", is_active)
print("Last login:", last_login)
