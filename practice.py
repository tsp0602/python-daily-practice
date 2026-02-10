
# # Write a python program to read three numbers and if any two 
# # variables are equal, print that number

# # a=int(input("enter first number"))
# # b=int(input("enter second number"))
# # c=int(input("enter third number"))

# # if a==b or a==c:
# #     print(a)
# # elif b==c :
# #     print(b)
# # else:
# #     print("No two numbers are same ")


# # -------------------------------------------------------------------------------------------



# # 2. Write a python program to read two numbers and find the smallest among them using ternary operator

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# small = a if a < b else b
# print("Smallest number:", small)

# # -------------------------------------------------------------------------------------------

# # 3. Write a python program to read three numbers and find the largest among them without ternary operator

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# if a >= b and a >= c:
#     print("Largest:", a)
# elif b >= a and b >= c:
#     print("Largest:", b)
# else:
#     print("Largest:", c)



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
    
