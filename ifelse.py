#Different types of operator for biconditionals:
#LOgical operator i.e, and, or , not other operator is relational operator such as, <= , >= , != , == ,


# a= int(input("Enter your time: "))
# if (a<=12 and a>0):
#     print("Good morning Sir")
# elif(a<24):
#     print("Good Night Sir")
# else:
#     print("Invalid Time Input")

#Real-time Generator
# import time
# timestamp = time.strftime('%H,%M,%S')
# print(timestamp)
# timestamp=int(time.strftime('%H'))
# print(timestamp)
# timestamp=int(time.strftime('%M'))
# print(timestamp)
# timestamp=int(time.strftime('%S'))
# print(timestamp)


# practise set of if-else

#find a program to find the greatest of four numbers
# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# c=int(input("Enter the third number: "))
# d=int(input("Enter the fourth number: "))
# if(a>b and a>c and a>d):
#     print("The value of A is greater in all of them")
# elif(a<b and b>c and b>d):
#     print("The value of b is greater in all")
# elif(c>a and b<c and c>d):
#     print("The value of C is greater in all")
# else:
#     print("D is greater in all")

#2-find whether student is passed or fail if it requires a total 40 and 33% is necessary to pass in  each subject assume three subjects
# a=int(input("Enter the Marks of English= "))
# b=int(input("Enter the Marks of Maths= "))
# c=int(input("Enter the Marks of Hindi= "))

# #check total percentage
# total_per=(a+b+c)/3
# #Check percentage of each sub:

# if (total_per>40 and a>33 and b>33 and c>33):
#     print("You are Passed with aggregrated marks of ",total_per)
# else:
#     print("You failed! ",total_per)

#3spam comment as a text containing following keywords:
#"Make a lot of money","buy now","Subscribe this","click this"
# a="Make a lot of money"
# b="buy now"
# c="Subscribe this"
# d="click this"
# msg=input("Enter your string= ")
# if (a in msg or b in msg or c in msg or d in msg):
#     print("Spam")
# else:
#     print("No spam")

#4 Find whether a given username contains less than 10 characters or not
# a=input("Enter the username=")
# if(len(a)<10):
#     print("Go on")
# else:
#     print("wait")

#5 find out whether given name is in the list or not
# a=["Harsh","2001","Birthdate"]
# b=input("Enter the name= ")
# if(b in a):
#     print("Gotcha")
# else:
#     print("Bad luck")

#Post talking about or not
# p=input("Enter your  post ")
# if("Harsh" in p.lower()):
#     print("I am good")
# else:
#     print("No denied")
