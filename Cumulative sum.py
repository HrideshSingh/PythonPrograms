"""
Given a list of n integers, print a new list such that every element in the new list represents the cumulative sum of all the elements until that position.

Input Format:

Single line of input contains a list of space separated integers 

Output Format:

Print the cumulative list

Example:

Input:

1 2 3 4 5

Output:

1 3 6 10 15
"""

n=input().split()
ans=[]
a=0
for i in n:
  a+=int(i)
  ans.append(a)
print(*ans,end="")