# This is class
# class Employee:
#     name="Harsh"
#     language="python"
#     salary=1200000 
# harsh=Employee()
# print(harsh.name)
# print(harsh.language,harsh.salary)

#this is instance attribute
# class Employee:
#     Language="Python"
#     Salary=120000
# harsh=Employee()
# harsh.name="Harsh"
# print(harsh.Language,harsh.Salary,harsh.name) here instances are used
# Ashmit=Employee()
#ashmit.Salary=1400000
# Ashmit.name="Ashmit"
# print(Ashmit.Salary,Ashmit.name)

#Use of self
# class Employee:
#     Salary=1200000
#     Language="Python"
#     def getinfo(self):
#         print(f"The salary is {self.Salary}, The language is {self.Language}")
# harsh=Employee()
# harsh.Language="Javascript"
# harsh.getinfo()

#use of static method
# class Employee:
#     Salary=1200000
#     Language="Python"
#     def getinfo(self):
#         print(f"The salary is {self.Salary}, The language is {self.Language}")
#     @staticmethod
#     def greet():
#         print("Good Morning")
# harsh=Employee()
# harsh.Language="Javascript"
# harsh.getinfo()
# harsh.greet()

#init constructor
# class emp:
#     def __init__(self,name, sal, lang):
#         self.name=name
#         self.sal=sal
#         self.lang=lang
#         print("Hey wassup!")
# harsh=emp("Yash",122000,"Javascript")
# print(harsh.name,harsh.sal,harsh.lang)


#Practice set
# class Programmer:
#     Company="Microsoft"
#     def __init__(self,name,salary,pincode):
#         self.name=name
#         self.salary=salary
#         self.pincode=pincode
# print("Name   |Salary |Pincode ")
# getinfo=Programmer("Advik  ",2000000,221007 )
# print(getinfo.name,getinfo.salary,getinfo.pincode, getinfo.Company)
# getinfo=Programmer("Devika ",2000000,198002)
# print(getinfo.name,getinfo.salary,getinfo.pincode,getinfo.Company)
# getinfo=Programmer("Adarsh ",2000000,200101)
# print(getinfo.name,getinfo.salary,getinfo.pincode,getinfo.Company)
# getinfo=Programmer("Harshit",2000000,100201)
# print(getinfo.name,getinfo.salary,getinfo.pincode,getinfo.Company)
# getinfo=Programmer("Jetha  ",2000000,201206)
# print(getinfo.name,getinfo.salary,getinfo.pincode,getinfo.Company)

# class Calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"Your square is {self.n*self.n}")
#     def cube(self):
#         print(f"Your square is {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"Your square is {self.n**1/2}")
#     @staticmethod
#     def greet():
#         print("hello")
# a=Calculator(4)
# a.square()
# a.greet()
# a.cube()
# a.greet()
# a.squareroot()
# a.greet()

# from random import randint
# class train:
#     def __init__(self,trainNo):
#         self.trainNo=trainNo
#     def book(self,fro,to):
#         print(f"Your ticket is booked in {self.trainNo} from {fro} to {to}")
#     def getstatus(self):
#         print(f"Your train {self.trainNo} is running on time")
#     def getfare(self,fro,to):
#         print(f"The fare in trainNo: {self.trainNo} \n which is from {fro} to {to} is: \n {randint(200,5555)}")
# t=train(12339)
# t.book("Varanasi","New Delhi")
# t.getstatus()
# t.getfare("Varanasi","New Delhi")


        
        