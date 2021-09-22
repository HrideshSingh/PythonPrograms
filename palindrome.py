"""
Given a string as input, determine if it is a palindrome or not. (Ignore the spaces, case and any punctuation or special characters present in the string). 
Note: A palindromes is a string which has characters in the same order when read forward or backwards.

Input Format

First line of the input contains a string 

Output Format

Print 'Yes' if the given string is a palindrome, 'No' otherwise.

Example:

Input:

Malayalam

Output:

Yes

Input:

Python

Output:

No
"""

name=list(input())
a=""
for i in name:
  if i.isupper():
    a+=i.lower()
  elif i.islower():
    a+=i
if a==a[::-1]:
  print("Yes",end="")
else:
  print("No",end="")

