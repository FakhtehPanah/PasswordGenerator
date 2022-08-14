import random
from secrets import choice

print("Let`s start a game :)\n")

chars = input("Enter some random characters ... \n")

length = input("Enter length of a passwrd\n")
length = int(length)

print("this is your Password")
     
#password = ""
for i in range(length):
    password += random.choice(chars)

print(password)
