
# # # Write a python program to read three numbers and if any two 
# # # variables are equal, print that number

# a=int(input("enter first number"))
# b=int(input("enter second number"))
# c=int(input("enter third number"))

# if a==b or a==c:
#     print(a)
# elif b==c :
#     print(b)
# else:
#     print("No two numbers are same ")


# # # -------------------------------------------------------------------------------------------



# # # 2. Write a python program to read two numbers and find the smallest among them using ternary operator

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# small = a if a < b else b
# print("Smallest number:", small)

# # # -------------------------------------------------------------------------------------------

# # # 3. Write a python program to read three numbers and find the largest among them without ternary operator

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# if a >= b and a >= c:
#     print("Largest:", a)
# elif b >= a and b >= c:
#     print("Largest:", b)
# else:
#     print("Largest:", c)



# # -------------------------------------------------------------------------------------------


# # problem :Write a program that takes a list of integers and prints the element(s) with the highest frequency.


# # This implementation focuses on clarity and logic building.
# # Optimization and pythonic approaches are intentionally avoided.


# l1 = list(map(int,input("Enter a list of numbers : ").split()))

# dictionary ={i:0 for i in l1}


# for i in l1:
#     dictionary[i] = dictionary[i]+1

# max_freq = 0
# for k,v in dictionary.items():
#     if v > max_freq:
#         max_freq = v

# for k,v in dictionary.items():
#     if v == max_freq:

#         print(f'{k} is the element with highest frequency : {v}')
    

# # -------------------------------------------------------------------------------------------

# #Question 1 — Sort by Last Digit 
# nums = [23, 45, 12, 39, 27]
# nums.sort(key = lambda x : x%10)
# print(nums)


# # -------------------------------------------------------------------------------------------

# # Question 2 — Sort by String Length
# words = ["python", "sql", "data", "ai"]
# words.sort(key= len )
# print(words)

# # -------------------------------------------------------------------------------------------
# # Question 3 — Sort by Distance from 50

# def func(n):
#     return abs(n-50)

# nums = [100, 50, 65, 82, 23]
# nums.sort(key=func)
# print(nums)

# # -------------------------------------------------------------------------------------------

# # Question 4 — Sort Tuples by Second Value
# students = [("Tejas", 85), ("Rahul", 70), ("Amit", 95)]
# students.sort(key= lambda x :x[1])
# print(students)


# # -------------------------------------------------------------------------------------------

# # Question 5 — Sort Dictionary List by Age
# people = [
#     {"name": "Tejas", "age": 22},
#     {"name": "Rahul", "age": 25},
#     {"name": "Amit", "age": 20}
# ]
# people.sort(key= lambda x:x["age"])
# print(people)



# # -------------------------------------------------------------------------------------------

# # Question 6 — Case-Insensitive Sorting
# names = ["Tejas", "rahul", "Amit", "deepak"]
# names.sort(key=str.lower)
# print(names)

# # -------------------------------------------------------------------------------------------

# # Question 7 — Multiple Key Sorting
# students = [("Tejas", 85), ("Rahul", 85), ("Amit", 90)]
# students.sort(key= lambda x: (x[1],x[0]))
# print(students)

# -------------------------------------------------------------------------------------------


# 1️⃣ Count words in a string (without using .split())

 
# Input: "I love python programming"
# Output: 4


# string1 = "I love python programming"
# cnt = list(string1.split(" "))
# print(len(cnt))


 # -------------------------------------------------------------------------------------------
# 2️⃣ Remove all spaces from string (without replace)
# Input: "hello world"
# Output: "helloworld"

# inpt="hello world"
# print(inpt.replace(" ",""))



 # -------------------------------------------------------------------------------------------
# 3️⃣ Find second largest element in list (without sort)
# [10, 5, 8, 20, 15]
# Output → 15

# l1= [10, 5, 8, 20, 15]
# max1=max(l1)
# max2=0
# for i in l1:
#     if i > max2 and i < max1:
#         max2=i

# print(max2)
    

# -------------------------------------------------------------------------------------------
# 4️⃣ Check if string is palindrome (without slicing [::-1])
# "madam" → True

# inpt=input("Enter a string : ")
# rev=[]
# for i in range(1, len(inpt)+1):
#     rev.append(inpt[-i])
#     #   print(inpt[-i])
#     # print(str(rev))
# if inpt == str(rev):
#     print("True")
# else:
#     print("False")



# # -------------------------------------------------------------------------------------------
# # hollow square

# n=int(input('Enter a number of line : '))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==1 or i==n or j==n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()





# # -------------------------------------------------------------------------------------------
# # hollow triangle 
# n=int(input("Enter number of lines : "))
# for i in range (1,n+1):
#     for j in range(1,n+1):
#         if i==n:
#             print("*",end="")
#         else:
#             print(" ",end="")




# -------------------------------------------------------------------------------------------
# Armstrong number 

inpt=int(input())
ActualNum=inpt
addition=0
num=0

while inpt>0:
    num=inpt%10
    addition+=num **3
    inpt=inpt//10

print(addition==ActualNum)




# -------------------------------------------------------------------------------------------





# -------------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------------



 # -------------------------------------------------------------------------------------------