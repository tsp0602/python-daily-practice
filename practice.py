
# # Write a python program to read three numbers and if any two 
# # variables are equal, print that number

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

if a==b or a==c:
    print(a)
elif b==c :
    print(b)
else:
    print("No two numbers are same ")


# # -------------------------------------------------------------------------------------------



# # 2. Write a python program to read two numbers and find the smallest among them using ternary operator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

small = a if a < b else b
print("Smallest number:", small)

# # -------------------------------------------------------------------------------------------

# # 3. Write a python program to read three numbers and find the largest among them without ternary operator

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)



# -------------------------------------------------------------------------------------------


# problem :Write a program that takes a list of integers and prints the element(s) with the highest frequency.


# This implementation focuses on clarity and logic building.
# Optimization and pythonic approaches are intentionally avoided.


l1 = list(map(int,input("Enter a list of numbers : ").split()))

dictionary ={i:0 for i in l1}


for i in l1:
    dictionary[i] = dictionary[i]+1

max_freq = 0
for k,v in dictionary.items():
    if v > max_freq:
        max_freq = v

for k,v in dictionary.items():
    if v == max_freq:

        print(f'{k} is the element with highest frequency : {v}')
    

# -------------------------------------------------------------------------------------------

#Question 1 — Sort by Last Digit 
nums = [23, 45, 12, 39, 27]
nums.sort(key = lambda x : x%10)
print(nums)


# -------------------------------------------------------------------------------------------

# Question 2 — Sort by String Length
words = ["python", "sql", "data", "ai"]
words.sort(key= len )
print(words)

# -------------------------------------------------------------------------------------------
# Question 3 — Sort by Distance from 50

def func(n):
    return abs(n-50)

nums = [100, 50, 65, 82, 23]
nums.sort(key=func)
print(nums)

# -------------------------------------------------------------------------------------------

# Question 4 — Sort Tuples by Second Value
students = [("Tejas", 85), ("Rahul", 70), ("Amit", 95)]
students.sort(key= lambda x :x[1])
print(students)


# -------------------------------------------------------------------------------------------

# Question 5 — Sort Dictionary List by Age
people = [
    {"name": "Tejas", "age": 22},
    {"name": "Rahul", "age": 25},
    {"name": "Amit", "age": 20}
]
people.sort(key= lambda x:x["age"])
print(people)



# -------------------------------------------------------------------------------------------

# Question 6 — Case-Insensitive Sorting
names = ["Tejas", "rahul", "Amit", "deepak"]
names.sort(key=str.lower)
print(names)

# -------------------------------------------------------------------------------------------

# Question 7 — Multiple Key Sorting
students = [("Tejas", 85), ("Rahul", 85), ("Amit", 90)]
students.sort(key= lambda x: (x[1],x[0]))
print(students)