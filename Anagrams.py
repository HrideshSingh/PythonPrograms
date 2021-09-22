"""
Given two strings as input, determine if they are anagrams or not. (Ignore the spaces, case and any punctuation or special characters). 

Note: Anagrams are the strings which are made up of the same set of letters. For example : Mary and Army are anagrams.

Input Format

First line of the input contains the first string 

Second line of the input contains the second string

Output Format

Print 'Yes' if the given strings are anagrams, 'No' otherwise.

Example:

Input:

Tom Marvolo Riddle

I am Lord Voldemort!!!

Output:

Yes

Input:

Royal Challengers Bangalore

Rajasthan Royals

Output:

No
"""

name=list(input())
name2=list(input())
a=""
b=""
for i in name:
  if i.isupper():
    a+=i.lower()
  elif i.islower():
    a+=i
for i in name2:
  if i.isupper():
    b+=i.lower()
  elif i.islower():
    b+=i
if sorted(a)==sorted(b):
  print("Yes",end="")
else:
  print("No",end="")
