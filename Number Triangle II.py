"""
Given an integer input 'n', print a palindromic triangle of n lines as shown in the example.

Input Format:

The input contains a number n (n < 10)

Output Format:

Print n lines corresponding to the number triangle

Example:

Input:

5

Output:

1

121

12321

1234321

123454321
"""

n=int(input())
for i in range(1,n+1):
  for j in range(1,i+1):
      print(j,end="")
      if i==j:
        for k in range(i-1,0,-1):
            print(k,end="") 
  if i!=n:
    print("")
