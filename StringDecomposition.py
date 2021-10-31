'''
Given a large string and a set of small strings, determine if it is possible to exactly

decompose the given large string into the set of small strings. (Assume that all the strings

are given in lowercase)

Input Format

The first line of the input contains a large string

The second line of the input contains space separated small strings

Output Format

Display Yes or No (no newline after the output)

Example:

Input:

abdefgbadklm

dab bad elmf kg

Output:

Yes

Input:

abdgefmnorst

frost badge lm

Output:

No

Explanation:

In the first case it is possible to construct the set of small strings by using exactly all the characters given in the original string. 

In the second case it is not possible.
'''

s=input()
a=input().split()
b=""
for i in a:
  b+=i
if(set(s)==set(b) and len(s)==len(b)):
  print("Yes",end="")
else:
  print("No",end="")