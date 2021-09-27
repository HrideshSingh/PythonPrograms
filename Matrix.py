"""
Given two integers r and c, indicating the number of rows and columns, print a two-dimensional matrix such that the elements of the matrix are in an increasing sequence from 1 to rXc, in a row-major order.

Input Format:

First line of the input contains two space separated integers indicating the rows and columns

Output Format:

Display r lines indicating the elements of the Matrix

Example:

Input:

3 3

Output:

1 2 3

4 5 6

7 8 9
"""

a,b=input().split()
a,b=int(a),int(b)
c=1
for i in range(1,a+1):
  for j in range(1,b+1):
    if j!=b:
      print(c,"",end="")
    else:
      print(c,end="")
    c+=1
  if i!=a:
    print("")
  else:
    print("",end="")
