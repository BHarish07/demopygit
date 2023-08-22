#---------------average of N numbers ------
'''
num=int(input("Enter how many numbers : "))
total_sum=0
for i in range(num):
    numbers=float(input("Enter a number: "))
    total_sum+=numbers
avg=total_sum/num

print("Average is : ",avg)

'''
import math

'''
rows=int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
'''
'''
num=int(input("Enter number of rows : "))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("*",end="")
    k=k+2
    print()
'''
# Program to convert weight in kg or lbs
'''
weight=int(input("Enter your Weight: "))
unit=input("(K)g or (L)bs: ")

if unit.upper()=='K':
    converted=weight/0.45
    print(" Your weight in Lbs : ",converted)
else:
    converted=weight*0.45
    print("Your weight in Kg: ",converted)


'''
'''
name="bro code!"
#if(name[0].islower()):
#    name=name.capitalize()
first_name=name[:3].upper()
last_name=name[4:].lower()
last_character=name[-1]

print(first_name)
print(last_name)
print(last_character)

'''
#function=block of code which execute only when it is called
'''
def hello(name,age,last_name):
    print("Hi "+name+"Your age is : ",age,"your name is : "+last_name)
        
hello("Dude",22,"Code") #positional arguments 

hello(last_name="code",name="Dude',age=22)#--keyword arguments


'''

#nested function calls ---function calls inside other function calls

#num=input("Enter a value : ")
#print(round(abs(float(num))))


# Variables -----global, local
#global variables can be accessed anywhere(inside and outside of the function )
#local variables are accessed only inside of a defined function
'''
name="bro" #-global variable

def dislay_name():
    name="Dude"  #--local variable
    print(name)
dislay_name()
print(name)

'''

#   *args= it is parameter that will pack all arguments into tuple
#          it is useful so that a function can accept a Varying amount of arguments
# we can use anything instead of args
'''
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(1,2,3,4,5,6,7))

'''

# **kwargs -----it is a parameter that will pack all arguments into a dictionary.
          #-----it is useful so that a function can accept varying amount of Keyword arguments

'''
def hello(**kwargs):
    print("Hello")
    print("Hello "+kwargs['first_name']+" "+kwargs['last_name'])

    for key,value in kwargs.items():
        print(value,end=" ")
        
hello(title="Mr.", first_name="Bro",middle_name="Dude",last_name="code")


'''
#-------------------loops---------
'''
i=1
while i<=5:
    print("Telusko", end=" ")
    j=1
    while j<=4 :
        print("Rocks", end=" ")
        j+=1
    i+=1
    print()

'''
'''
i=1
while i<5:
    print("# ",end="")
    j=1
    while j<4:
        print("# ",end="")
        j+=1
    i+=1
    print()
'''
'''
for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()

'''

'''
# prime number  using for -else
import math as m
num=int(input("Enter a Number : "))
#for i in range(2,num):
#for i in range(2,int(m.sqrt(num))+1):
for i in range(2,int(num/2)):
    if num%i==0:
        print("Not a Prime number")
        break
else:
    print("Prime number ")

'''
# -----------------------------------Bitwise Operators--------------------------------------

# ~ tilde
#print(~12) #output: -13

# Bitwise AND
#print(12&13) #o/p: 12

#Bitwise OR
#print(12|13)#o/p: 13

# X^OR
#print(12^13) #o/p: 1

#LeftShift operator
#print(10<<2) #o/p: 40

#RighttShift operator
#print(10>>2) #o/p: 2
'''
# Math function

import math
print(math.sqrt(25)) #o/p: 5.0
print(math.floor(3.55)) #o/p: 3
print(math.ceil(3.55)) #o/p : 4
print(math.pow(24,3)) # o/p: 13824
print(math.pi) #o/p: 3.141592653589793
print(math.e) #o/p: 2.718281828459045

'''
# Evalute the expression

#result=eval(input("Enter the expression : ")) # expression: 2+6-7
#print(result) # o/p: 1


# Command line arguments ---agrv=argument values
'''
import  sys
#argv[0]--file name
x=int(sys.argv[1])
y=int(sys.argv[2])
print(x+y)

# CLI: python Examples.py 14 23  #o/p: 37

'''


# ------------------------------------------Arrays:
'''
import array as arr
v=arr.array('i',[1,2,-5,6,9])
print(v)

from array import  *
val=array('i',[2,4,5,-3])
print(val)                                              #address        size
print(val.buffer_info()) # will give size of the array -(3078409109920, 4)
print(val.typecode) #will give type of code--- int -i
#reverse of the array
val.reverse()
print(val) #array('i', [23, -54, 4, 2])
print(val[1]) # -54

for i in range(len(val)):
    print(val[i])
#for dynamic
for e in val:
    print(e)

i =0
while i<len(val):
    print(val[i])
    i+=1

#for creating/copying a Newarray

#newArr=array(val.typecode,(a*a for a in val))
#print(newArr)

neWArr=array(val.typecode, (a*a for a in val))
i=0
while i<len(neWArr):
    print(neWArr[i])
    i+=1
'''

'''
#----------------- Array values from user
#from array import *
import array as ar
arr=ar.array('i',[])
n=int(input("Enter the length of the array : "))
for i in range(n):
    x=int(input("Enter the value: "))
    arr.append(x)

print(arr)

#to print the index of the value entered by user

val=int(input("Enter the value to find the index : "))
k=0
for e in arr:
    if e==val:
        print("The index of the value is : ",k)
        break
    k+=1
else:
    print("You've entered incorrect value which is not present in the array ")

'''
#------------------------------- for multi dimensional array --use numpy
'''
from numpy import *
arr=array([[1,2,3,5],[4,6,46,7]])
print(arr)
'''
'''
# ways of creating arrays in numpy
# array(), logspace(), linespace(),arange(),zeros(),ones()
from numpy import *
arr=array([1,5,1,5])
arr=arange(1,10,2)
arr=linspace(1,10,5)
arr=logspace(1,40,3)
arr=zeros(5)
arr=ones(7)
#print('%.2f'%arr[1])-for logspace

print(arr)
'''

#-------------------------------------copying array
'''
from numpy import *
arr1=array([1,5,4,6,7]) # arr1=array([1,5,4,6,7],int)
arr2=arr1

arr3=arr1+arr2
arr3=arr1*arr2
print(concatenate([arr1,arr2]))

arr4=arr1.view() #shallow copy
arr5=arr1.copy()  #deep copy
arr1[2]=8

print(arr1.dtype)
print(sin(arr1))
print(sqrt(arr1))
print(pow(arr1,2))
print(log(arr1))
print(exp(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)

print(id(arr1))
print(id(arr2))
print(id(arr4))
print(id(arr5))

'''
#--------------Multi dimensional array----
'''
from numpy import *
arr=array([[1,2,3,4,5,6],[4,5,6,7,8,9]])

print(arr.ndim) # will give dimension
print(arr.flatten())
print(arr.size)
print(arr.shape) # share of array-(2, 3)
print(arr.reshape(3,4)) # will give 2d array
print((arr.reshape(2,2,3))) # will give 3d array 
'''
# ---------------Matrices-------------

'''
from numpy import *
m1=matrix('1,2,3;4,5,6;7,8,9')
m2=matrix('1,2,3;4,7,5;8,9,6')
print(m1*m2)
print(m1+m2)
print(m1.diagonal())
print(m1.min())
print(m1.max()
      
'''

#--------------------------Functions--------------------
'''
def greet():
    print("Hello")
    print("Good morning")
greet()

def add(x,y):
    c=x+y
    print(c)
add(5,4)

def add(x,y):
    c=x+y
    return c
result=add(3,5)
print(result)

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(5,6)
print(result1, result2)


def add(a,*b): #the values will be added as tuple
    c=a
    for i in b:
        c+=i

    print(c)
add(2,5,3,5,6)

def add(*b):
    c=0
    for i in b:
        c+=i
    print(c)
add(2,45,32,2)
'''
# --Keyword variable lenth argumensts **kwargs
'''
def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
person('navin',age=28,city='Mumbai',phone=9215325692)
'''

 #--------------------global variables----
'''
a=10
print(id(a))

def something():
   # global a 
    a=15 # local variable
    x=globals()['a'] #
    print(id(x))
    print(id(a))
    print("in side ",a)
    globals()['a']=15 # to chage the value of the global variable
something()
print("out side",a)
print(id(a))

'''
#---to pass the values list in a function to pass the values list in a function
'''
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[12,23,14,65,25,66,7,26]
even,odd=count(lst)
print("Even : {} and  Odd : {}".format(even,odd))

'''
#-example: display no.of users whose name has more than 5 char---take input from user -10 names

'''


lst=[]
for i in range(10):
    names=input("Enter  user name : ")
    lst.append(names)

def users(lst):
    num_of_users = 0
    for i in lst:
        if len(i)>5:
            num_of_users+=1

    return num_of_users

print("Enter 10 user names")
print(lst)
num_of_users=users(lst)
print("User names who has more than 5 char: {}".format(num_of_users))
'''
#-----fibnocci series

'''
def fib(n):
    a=0
    b=1
    if n<1:
        print("Enter valid number")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(10)
'''
'''
num=int(input("How many number of fibnocci series you want: "))
n1,n2=0,1
sum=0
if num<=0:
    print("Enter number greater than zero")
for i in range(0,num):
    print(sum,end=" ")
    n1=n2
    n2=sum
    sum = n1 + n2

'''

#------------Factorial ----

'''
n=int(input("Enter a nnumber to find the factorial: "))
f=1
for i in range(1,n+1):
    f=f*i
print("The factorial of ",n,"is :",f)

'''
'''
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("Enter a number to find the factorial : "))
result=fact(n)
print("The factorial of given number is : ", result)

'''

#---------Recursion-----Funtion calling itself
'''
import sys
print(sys.getrecursionlimit()) # to know the limit of the recursion

# sys.getrecursionlimit(2000)#to change the value of the recursion limit

i=0
def recur():
    global i
    i+=1
    print("Hello",i)
    recur()
recur()

'''

#------Finding factorial using recursion
'''
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input("Enter a number to find the factorial: "))
result=fact(n)
print("The factorial of {} is {} ".format(n,result))

'''

#-----Lamda --Anonymous functions
'''
f=lambda a,b:a+b # we can use only one expression at a time with any number of arguments
#print(f(5,6))
result=f(5,6)
print(result)
'''

 #----------------filter(), map(), reduce()
'''
from functools import * # for the use of reduce()

nums=[1,3,42,21,6,24,66,7,8]
evens=list(filter(lambda n:n%2==0,nums)) # to filter te even numbers
doubles=list(map(lambda n:n*2,evens))
sum=reduce(lambda a,b:a+b,doubles)

print(evens)
print(doubles)
print(sum)

'''
# -----------Decorators----------
#TO change behavior of existing func before compilation
'''
def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
div(2,4)
'''

#---------Special variable     __name__
'''
def main():
    print("Hello")
    print("Welcome user")
if __name__=="__main__":
    main()
    
#--check helloworld.py for example- import Examples print("It's time to calculate ")
'''
# -----------OOPs-----------------

# class -object

'''
class Computer:
    def config(self):
        print("i5, 16GB, 1TB")

comp1=Computer() # comp1 is object
comp2=Computer() #Computer() is constructor 

comp1.config() # calling method using obj---
comp2.config()

Computer.config(comp1) 
Computer.config(comp2)

'''

# -----Special method   __init__
'''
class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Config is ", self.cpu,self.ram)

comp1=Computer("i5", 16)
comp2=Computer("Ryzen 3",8)

comp1.config()
comp2.config()

'''
# -----constructor, self , comparing objects
'''
class Computer:
    def __init__(self):
        self.name="navin"
        self.age=28
    def config(self):
        print("Your name is",self.name, "and your age is ", self.age)
    def compare(self,c2):
        if c1.age==c2.age:
            return True
        else:
            return False
c1=Computer()
c2=Computer()
c1.name="Harish"
c1.age=30
if c1.compare(c2):
    print("They are same age")
else:
    print("They are not same age")

'''
# ----------Variables
# Class (Static) variables
# Instance variables
'''
class Car:
    wheels=4
    def __init__(self):
        self.com="BMW"
        self.mil=10
c1=Car()
c2=Car()
c1.mil=8
Car.wheels=6 # to change the class variable -it will effect for all obj
print(c1.mil, c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)
'''

# -----------------Types of Methods-----------
# Instance method --to work with instance variables
# Class method -------to work with class or static variables
# Static method------nothing do with instance or class variables
'''
class Student:
    school="Telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    #setters and getters

    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
        return self.m1

    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is Student class----in abc modules ")

s1=Student(42,65,88)
s2=Student(66,54,87)
print(s1.avg())
print(s2.avg())
print(Student.getSchool()) # To call the calss method
Student.info()  # To call the static method
'''
# -------------------------- Inner Class ---------------

# You can create object of inner class inside the outer class (OR)
# You can create object of inner class outside the outer class provided- use outer class name to call it

'''
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop() # obj is created inside class to access inner class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.ram=8
            self.cpu="i5"
        def show(self):
            print(self.brand, self.cpu,self.ram)

s1=Student("Navin",2)
s2=Student("Harish",3) 
s1.show()
#lap1=Student.Laptop() # obj is created outside class to access inner class
#lap1.show()

'''

# ------------Inheritance

# single level inheritance
# multi level inheritance
# multiple inheritance
'''
class A:  #Super class
    def feature1(self):
        print("Feature 1 is working ")
    def feature2(self):
        print("Feature 2 is working ")

class B:    #class B(A): single level inheritance
    def feature3(self):
        print("Feature 3 is working ")
    def feature4(self):
        print("Feature 4 is working ")
class C(A,B): # _multiple inheritance # class C(B): multi level inheritance
    def feature5(self):
        print("Feature 5 is working ")
a1=A()
b1=B()
c1=C()

'''
# --------super()--------------
# constructor in inheritance
'''
class A:  # Super class
    def __init__(self):
        print("Init A ")
    def feature1(self):
        print("Feature 1 is working ")
    def feature2(self):
        print("Feature 2 is working ")
class B:  # class B(A): single level inheritance
    def __init__(self):
        super().__init__()
        print("Init B ")
    def feature3(self):
        print("Feature 3 is working ")
    def feature4(self):
        print("Feature 4 is working ")
class C(A, B):  # _multiple inheritance # class C(B): multi level inheritance
    def __init__(self):
        super().__init__() #it will print init method of A --
        print("Init C ")
    def feature5(self):
        print("Feature 5 is working ")
a1 = C() 
'''
#-----------------------------Polymorphism-------------------
#---Duck Typing
'''
class Pycharm:
    def execute(self):
        print("Compiling ")
        print("Running")
class MyEditor:
    def execute(self):
        print("Spell Checking")
        print("Convention check")
        print("Compiling ")
        print("Running")
class Laptop:
    def code(self,ide):
        ide.execute()
ide=MyEditor()
lap1=Laptop()
lap1.code(ide)
'''

#------------Operator Overloading ----------------
'''
class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def __add__(self, other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        r3=self.m3+other.m3
        s3=Student(r1,r2,r3)
        return s3
    def __gt__(self, other):
        r1=self.m1+self.m2+self.m3
        r2=other.m1+other.m2+other.m3
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {} {}'.format(self.m1,self.m2,self.m3)
s1=Student(83,45,54)
s2=Student(43,54,66)
s3=s1+s2
print(s3.m1)
if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")
print(s1)
print(s2)
'''
#----------------------Method overloading and Method Overriding-----------

#method overloading is not supported in python --Methods having same but taking different no.of parameters
'''
class Student:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

sum=Student()
print(sum.add(5,8,3))
'''

#Method overriding is possible with inheritance -multiple methods having same name and taking same parameters
'''
class A:
    def show(self):
        print("init A")
class B(A):
    def show(self):
        print("init B")
a1=B()
a1.show()
'''

#-----------------Abstract method and Abstract class---------------
#abstract class will have atleast one abstract method
#ABC--abstract base class
'''
from abc import abstractmethod,ABC

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Running")
class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()
com1=Laptop()
#com1.process()
com2=Programmer()
com2.work(com1)
'''
#----------Iterator--------
'''
nums=[2,4,3,8,6]
it=iter(nums)
#print(it) # iter will give the object of the iterator
print(it.__next__()) # will give the next object
print(next(it))
'''
#To print the top10 values
'''
class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            value=self.num
            self.num+=1
            return value
        else:
            raise StopIteration

values=TopTen()
print(next(values))
for i in values:
    print(i)
'''
#----------Generators----
#generators will give iterators
'''
def topten():
    n=1
    while n<=10:
        sq=n*n #topten perfect square
        yield sq
        n+=1
values=topten()
for i in values:
    print(i)
'''
#-------Exception handling---------

'''
a=4
b=0
try:
    print("Resource open")
    print(a/b)
    k=int(input("Enter a number: "))
except ZeroDivisionError as e:
    print("You cannot enter the number by zero: ",e)
except ValueError as e:
    print("Invalid Input",e)
except Exception as e:
    print("Something went wrong......")
finally:
    print("Resource closed")
'''
'''
from threading import *
from time import sleep
class Hello(Thread):
    def run(self):  #funtion should be run -it is present in thread class
        for i in range(5):
            print("Hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t1=Hello()
t2=Hi()
t1.start() #start will directly call the run functn
sleep(0.2) 
t2.start()
t1.join() #join will used to join  the two threads then only main thread will run after t1 &t2 threads are  cpmpleted 
t2.join()

print("Bye")
'''
#-----File Handling-----------
'''
f=open("Myfile.txt",'r')
#f=open("C:\\Users\\LENVO\\Documents\\Locators.txt","r") # after providing path -we need to give the \\ for the path
#Eprint(f.read())
f2=open("C:\\Users\\LENVO\\Downloads\\wallpaperflare-cropped.jpg","rb") # for the image files -we need to use rb  for byte conversion

f3=open("C:\\Users\\LENVO\\Downloads\\feepayment.pdf","rb")
f1=open("abc2.txt","wb")
#print(f.read()) #readline will give the first line
for i in f3:
    f1.write(i)
'''

#-------------Linear serach------
'''
pos=-1
def search(list,n):
    for i in range(len(list)-1):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False
'''


''' i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1
    return False '''
'''
list=[2,4,7,6,9,5]
n=9
if search(list,n):
    print("Found at position ",pos+1)
else:
    print("Not Found")
'''
#----------Binary Search------
'''
pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list=[2,4,5,3,6,1254,978,84,654,7]
n=6
if search(list,n):
    print("Found value at position",pos+1)
else:
    print("Not Found")
'''
#--------------Bubble sort----------
'''
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):  #range(6)=0,1,2,3,4,5
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
nums=[2,5,4,7,8,3,1]
sort(nums)
print(nums)
'''

#--------Selection sort-----------
'''
def sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
        print(nums)
nums=[5,3,6,7,8,2]
sort(nums)
print(nums)
'''
#-------------Mysql database connect----------
#install mysqlconnector using cmd
# pip install mysql-connector-python

'''
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Harish@777",database="Harish")
mycursor=mydb.cursor()
mycursor.execute("select * from student")

for i in mycursor:
    print(i)
'''





