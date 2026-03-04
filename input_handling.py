



# [ 12,  7,89  ,   5 ]


# arr=input()
# arr=arr[1:-1]
# arr=list(map(int,arr.replace(","," ").split()))


# print(sum(arr))


# ==========================================================================================


# ### ⭐ Coding Question — Mixed Separator Number Count (Easy → Moderate → Difficult Input Handling)

# #### **1. Problem Statement**

# You are given a single line containing numbers enclosed in curly braces `{ }`.
# The numbers may be separated using:

# * Commas `,`
# * Semicolons `;`
# * Spaces
# * Or written continuously together

# Your task is to:

# * Extract all valid integers from the input.
# * Print the **count of even numbers** among them.

# The main challenge is correctly handling the irregular and mixed separators.

# ---

# #### **2. Exact Input Format**

# * A single line containing numbers inside curly braces `{ }`.
# * The input may contain:

#   * Extra spaces anywhere
#   * Mixed separators (`,` or `;` or spaces)
#   * Multiple separators together
#   * Continuous digits forming a single number
# * Only non-negative integers are present.

# **Rules:**

# * Ignore `{` and `}`.
# * Continuous digits represent one number.
# * Treat comma, semicolon, and spaces as separators.

# ---

# #### **3. Output Format**

# * Print a single integer — the count of even numbers extracted from the input.

# ---

# #### **4. Sample Input**

# ```
# { 12,7;  45  8;;23,  100 }
# ```

# ---

# #### **5. Sample Output**

# ```
# 3
# ```

# ---

# #### **6. Explanation of Sample**

# From the input:

# * Extracted numbers → `12`, `7`, `45`, `8`, `23`, `100`
# * Even numbers → `12`, `8`, `100`
# * Count of even numbers → `3`


# { 12,7;  45  8;;23,  100 }
# import re
# s=input()
# s=s[1:-1]
# s=re.sub(r"[,;]"," ",s)
# s=list(map(int,s.split()))
# counter=0
# for i in s:
#     if i%2==0:
#         counter+=1
# print(counter)







# ==========================================================================================
# ⭐ Coding Question — Multi-Line Encoded Number Sum

# Sample Input
# 3
# (12# 7##45)
# (  89  #23 )
# ( )


# n=int(input())
# arr=[]

# for _ in range(n):
#     x=input()
#     x=x[1:-1]
#     x=list(map(int,x.replace("#",' ').split()))
#     arr.append(x)


# large=0
# for i in arr:
#     for j in i :
#         if j>large:
#             large=j

# print(large)




