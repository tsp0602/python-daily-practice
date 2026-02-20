
# -------------------------------------------------------------------------------------------
20-2-2026
⭐ Question 1 — Reverse a String
s = "python"
rev=s[::-1]
print(rev)



# -------------------------------------------------------------------------------------------

# ⭐ Question 2 — Count Vowels
s = input("Enter a string to count vowels : ")
count = sum(1 for c in s.lower() if c in "aeiou")
print(count)



# -------------------------------------------------------------------------------------------
# ⭐ Question 3 — Check Palindrome
s = input("Enter a string : ")
if s == s[::-1]:
    print("Given string is palindrome ")
else:
    print("Given string is not palindrome ")



# -------------------------------------------------------------------------------------------
# ⭐ Question 4 — Remove Duplicate Characters
s="programming"
ns=""
for c in s:
    if c not in ns:
        ns+=c
    else:
        pass
print(ns) 




# -------------------------------------------------------------------------------------------
# ⭐ Question 5 — Count Character Frequency
s="banana"
ns=""
for c in s :
    if c not in ns:
        ns+=c

for i in ns:
    print(f"{i} -> {s.count(i)} " )



# -------------------------------------------------------------------------------------------

# ⭐ Question 6 — Check Anagram
s1="silent"
s2="listen"
if sorted(s1) == sorted(s2):
    print("Anagram")
else :
    print("Not anagram ")




# -------------------------------------------------------------------------------------------
# ⭐ Question 7 — First Non-Repeating Character
s="aabbcde"
for c in s:
    if s.count(c) == 1:
        print(c)
        break
        


# -------------------------------------------------------------------------------------------

# ⭐ Question 8 — Replace Spaces with Hyphen
s="hello world python"
ns=s.replace(" ","-")
print(ns)



# -------------------------------------------------------------------------------------------
# ⭐ Question 9 — Longest Word in Sentence
s="I love learning python programming"
l1=s.split()
max_len=0
longest_word=""
for i in l1:
    if max_len < len(i):
        longest_word = i
        max_len = len(i)
print(longest_word)


# -------------------------------------------------------------------------------------------
# ⭐ Question 10 — Remove All Special Characters
s="hello@123#world!"
ns=''
for i in s:
    if i.isalnum():
        ns+=i
print(ns)