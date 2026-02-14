# class Employee: #This is the base class
#     company="Reliance"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
# #this is inherited class
# class Programmer(Employee):
#     company="Reliance Infotech"
#     def language(self):
#         print(f"The name is {self.name} and the language is {self.lang}")
# a=Employee()
# b=Programmer()
# print(a.company,b.company)  

#Multiple Inheritance
# class Employee: 
#     company = "Reliance"
#     name = "default name"
    
#     def show(self):
#         print(f"The name is {self.name} and the name of the company is {self.company}")

# class Coder:
#     language = "Python"
    
#     def lang(self):
#         print(f"The language that is compulsory for this company is {self.language}")

# class Programmer(Employee, Coder):
#     company = "Reliance Infotech"
    
#     def show_language(self):
#         print(f"The company is {self.company} and the language is {self.language}")

# b = Programmer()
# b.show()
# b.lang()
# b.show_language()

#Multilevel Inheritance
# class Emp:
#     a=1
# class Pro(Emp):
#     b=2
# class Manager(Pro):
#     c=3
# o=Manager()
# print(o.a,o.b) 

#Super Method
# class Emp:
#     def __init__(self):
       
#        print("Constructor of Emp")
#     a=1
# class Pro(Emp): 
#     def __init__(self):
#        super().__init__()
#        print("Constructor of Programmer")
#     b=2
# class Manager(Pro):
#     def __init__(self):
       
#        print("Constructor of Manager") 
#     c=3
# o=Emp()
# print(o.a) 

# class TwoDvector:
#     def __init__(self, i , j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f"The 2Dvector is {self.i} and {self.j}")
# class ThreeDvector(TwoDvector):
#     def __init__(self, i,j, k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(f"The 3Dvector is {self.i} and {self.j} and {self.k}")
# a=TwoDvector(3,4)
# a.show()
# b=ThreeDvector(2,3,4)
# b.show()

# class Emp:
#     sal=234
#     incre=20
#     @property
#     def salaftincre(self):
#         return (self.sal + self.sal * (self.incre/100))
#     @salaftincre.setter
#     def salaftincre(self,sal):
#         self.incre=((sal/self.sal)-1)*100
# a=Emp()
# a.salaftincre=280.8
# print(a.incre)

# class vector:
#     def __init__(self, a, b):
#         self.a=a
#         self.b=b
#     def __add__(self, other):
#         result= vector(self.a+other.a, self.b+other.b)
#         return result
#     def __mul__(self,other):
#         result=self.a*other.a + self.b*other.b
#         return result
#     def __str__(self):
#         return f"Vector ({self.a},{self.b})"
# v1=vector(2,3)
# v2=vector(4,5)
# print(v1+v2)
# print(v1*v2) 

# class vector:
#     def __init__(self, list):
#         self.list=list
#     def __len__(self):
#         return 3
# v1=vector([2,3])
# print(len(v1))

#The perfect Guess
# import random
# n=random.randint(1,100)
# a =-1 #n -1 kabhi nhi hoga jo ki true rahega
# guesses=0
# while(a!=n):
#     guesses+=1
#     a=int(input("Guess the number= "))
#     if(a==n):
#         print("You are right")
#     elif(a>n):
#         print("Lower Number Please")
#     else:
#         print("Higher Number Please")
# print(f"You have guessed the right answer in {guesses} attempts")

#