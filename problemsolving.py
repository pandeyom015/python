#Example 3: Python program to calculate the sum of all numbers from 1 to a given number.

# n=int(input("Enter your Number= "))
# fact=0
# for i in range(1,n+1):
#     if(n==0 or n==1):
#         print(1)
#     else:
#         fact+=i

#Example 4: Python program to calculate the sum of all the odd numbers within the given range.

# n=int(input("Enter your Number= "))
# sum=0
# for i in range(n+1):
#     if i%2!=0:
#         sum+=i
# print(sum)

#Example 5: Python program to print a multiplication table of a given number

# n=int(input("Enter Number= "))
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")

#Example 6: Python program to display numbers from a list using a for loop.

# n=["Harsh","Shashank","Anand","Prakhar","Umang"]
# for i in n:
#     print(i)

#Example 7: Python program to count the total number of digits in a number.

# def natural(n):
 
#     if (n== 1):
#         return 1
#     else:
#         return (n*(n+1))/2
# print(natural(5))

#factorial

# def natural(n):

#    if (n == 1 or n==0):
#         return 1
#    else:
#        return natural(n-1)*n
# print(natural(5))

# def circle():
#     # r=int(input("Enter Radius= "))
#     # area=3.14*r*r
#     # print("area of circle is ",area,"cm")
#     d=int(input("Enter Diameter= "))
#     area=3.14*d/2*d/2
#     print("Area of circle is ",area,"cm")
# circle()
# # from lib2to3.btm_utils import reduce_tree


#Plaindrome
# def palindrome():
#     w=input("Enter your word= ")
#     if w==w[::-1]:
#         print("palindrome")
#     else:
#         print("not a palindrome")
# palindrome()


# def list(num):
#     add=0
#     for i in num:
#         if i%2==0:
#             add=add+i
#     return add
# List=list([12,23,34,45,56,67])
# print(List)

#Count and print number of vowels
# def count():
#     vo=input("Enter your words= ")
#     for i in vo:
#         if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#             print(i)
#             return vo.count(i)
# C=count()
# print(C)

#Prime number
# def prime():
#     n=int(input("Enter your number= "))
#     for i in range(2,n):
#         if n%i==0:
#             print("not a prime")
#             break
#     else:
#         print("prime")
# print(prime())

# def average():
#     a=int(input("enter a= "))
#     b=int(input("enter b= "))
#     c=int(input("enter c= "))
#
#     avg=(a+b+c)/3
#     print(avg)
#     return "Okay"
# a=average()
# print(a)


# def arg(name,end):
#     print(name +" See you "+end)
#     return"done"
# a=arg("Harsh","Thank you")
# print(a)

# def fact(a):
#     if(a==0 or a==1):
#         return 1
#     return a* fact(a-1)
# a=int(input("Enter number for the factorial= "))
# print(fact(a))

#Measure the temperature
# def temp():
#     t=int(input("Enter the temperature= "))
#     c=5*(t-32)/9
#     print(f"Your temperature is {round(c)}")
# temp()

#recursive function to calculate the sum of first n natural numbers
# def natural(n):
#     if(n==1):
#         return 1
#     return n+ natural(n-1)
# n=int(input("Enter the number= "))
# print(natural(n))

# ***
# **
# *
# def pattern(n):
#     if(n==5):
#         return ("")
#     print("*"*n)
#     pattern(n+1)
# n=int(input("Enter number of stars= "))
# print(pattern(n))

#Project 1
#1 for snake,-1 for water,0 for gun
# import random
# computer=random.choice([-1,0,1])
# youstr=input("Enter your choice: ")
# youdict={"s":1,"w":-1,"g":0}
# revdict={1:"Snake",-1:"Water",0:"Gun"}
# you=youdict[youstr]
# print(f"You choose {revdict[you]}\nComputer choow"
#       f"se {revdict[computer]}")
# if(computer ==-1 and you == 1):
#     print("You Win!")
# elif(computer==1 and you==0):
#     print("You Win!")
# elif (computer == -1 and you == 0):
#     print("Computer Win!")
# elif(computer==1 and you==-1):
#     print("Computer Win!")
# elif(computer==0 and you==1):
#     print("Computer Win!")
# elif(computer == you):
#     print("Draw")
# elif (computer == 0 and you == -1):
#     print("Computer Win!")
# else:
#     print("Something went wrong")

