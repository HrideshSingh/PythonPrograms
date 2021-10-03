"""
Given a list of integers and a value k, print the number in the list that appears exactly k times. (It is guaranteed that there’s exactly one integer that appears k times).

Input Format:

First line of the input contains a list of integers

Second line of the input contains a value k

Output Format:

Display the number that appears exactly k times

Example:

Input:

1 2 2 3 3 3

3

Output:

3
"""

n=input().split()
k=int(input())
for i in set(n):
  if n.count(i)==k:
    print(i,end="")