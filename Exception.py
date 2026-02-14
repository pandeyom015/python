# try:
#     a=int(input("Enter the number= "))
#     print(a)
# except Exception as e:
#     print("Invalid Syntaxhas")

# a=int(input("enter a number= "))
# b=int(input("Enter second number= "))
# if(b==0):
#     raise ZeroDivisionError("Numbers cannot be divided by zero")
# else:
#     print(f"The dvn of a/b is {a/b}")

#Try with finally

# def func():
#     try:
#         a=int(input("Enter the number= "))
#         print(a)
#         return
#     except Exception as e:
#         print(e)
#         return
#     finally    
#         print("I am inside else")
# func()

#if __name__=="__main__"
# from walrus import myfunc

#enumerate function
# l=[12,345,21,4312]
# for index,item in enumerate(l):
#     print(f"The item number of index {index} is {item}")

# l=[12,345,21,4312]
# sqauredlist=[i*i for i  in l]
# print(sqauredlist)

#practise set1 
# try:
#     with( open("1.txt","r") as t, 
#          open("2.txt","r") as t,
#          open("3.txt","r") as t):
#          print(t.read())
# except Exception as e:
#      print("Invalid")

#practise set 2
# l=[12,34,23,42,45,60]
# for index,item in enumerate(l):
#     if index == 2 or index == 5 or index == 1:
#         print(f"The value of index {index} {item}")

#practise set 3
# n=int(input("Enter your number= "))
# table=[i*n for i in range(1,11)]
# print(table)

#PS 4
# try:
#     a=int(input("Enter your number= "))
#     b=int(input("Enter your number= "))
#     print(a/b)
# # if(b==0):
# #     print("Infinite")
# #     raise ZeroDivisionError("Cannot possible")
    
# # else:
# #     print(a/b)
# #     print("Why not you stupid! Bastard")
# except ZeroDivisionError as v:
#     print("Infinite")

#PS5
# n=int(input("Enter your number= "))
# table=[i*n for i in range(1,11)]
# with open("tables.txt","a") as f:
#     f.write(str(table))
