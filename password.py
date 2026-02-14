import random
import string
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789!@#$^&*()?"
length=int(input("The length of the password is= "))
password=""
for  i in range(length):
    password+=random.choice(a)
print(password)