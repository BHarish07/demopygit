'''
name=input("What is your name : ")
age=int(input("Enter your age : "))
print("Hello "+ name+" your age is "+str(age))


import math

pi=-3.43
num=81

print(math.ceil(pi))
print(math.floor(pi))
print(math.sqrt(num))
print(round(pi))
print(abs(pi))
print(pow(pi,2))
'''
import time

# Slicing
'''
name=" Bro Code"
first_name=name[:3]
last_name=name[4:]
funky_name=name[::2]
print(first_name,last_name,funky_name)

# Reversing a string
reverse_string=name[::-1]
print(reverse_string)


website1="http://google.com"
website2="http://youtube.com"

slice=slice(7,-4)
print(website1[slice])
print(website2[slice])
'''

#for seconds in range(10,0,-1):
#   print(seconds)
#    time.sleep(1)
#print("Happy new year!")
#for i in range(10,0,-1):
 #   print(i)

#name=""
#while len(name)==0:
 #   name=input("Enter your Name: ")
#print("Your name is : "+name)
'''
rows=int(input("How many rows?: "))
columns=int(input("How many columns?: "))
symbol=input("Enter a symbol to use : ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()

'''
#--------------Break---------
'''
while True:
     name=input("Enter your name: ")
     if name!="":
         break
print("Hello " +name)

'''

#---------------------Continue-----------
'''
phone_number="123-456-789"
for i in phone_number:
    if i=="-":
        continue
    print(i,end="")
'''

#---------Pass-------

'''
for i in range(1,21):
    if i==13:
        continue
    else:
        print(i)
'''
#----------list----------
'''

food=["hot dog","ice cream","pudding","pizza"]

food.append("Banana")
food.pop()
food.insert(2,"burger")
food.remove("ice cream")
food.sort()
print(food)

for x in food:
    print(x)


dessert=["Ice cream","cake",]
drinks=["Coke","soda","tea"]
dinner=["Hot dog","hamburger","pizza"]

food=[dessert,drinks,dinner]
print(food)
print(food[1][2])   
'''

#-----Tuple---
'''
student=("Harish",21,"male","male")
print(student.index("male"))
print(student.count("Harish"))
'''
#--------Set-----unordered, unindexed,no duplicate values
'''
dishes={"bowl","cup","plate","knife"}
utensils={"fork","spoon","knife"}
print(dishes.difference(utensils))

'''
#-------------Dictionaries---------changeble, unordered,unique key:value pair
'''
capitals={'India':'New Delhi','USA':'Washington DC','Germany':'Berlin'}
capitals.
print(capitals)

'''




