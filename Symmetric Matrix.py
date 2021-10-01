"""
Given a N X N square matrix, determine if it is a Symmetric Matrix.

Input Format:

The first line of the input contains an integer N which represents the number of rows and the number of columns.

Next N lines represent the elements of the matrix.

Output Format:

Print Yes or No

Example:

Input:

3

1 -2 3

-2 3 1

3 1 2

Output:

Yes
"""

n=int(input())
mat=[]
f=0
for i in range(n):
  mat.append(input().split())
#print(mat)
for a in range(len(mat)):
  for b in range(n):
    if mat[a][b]!=mat[b][a]:
      f=1
if f==0:
  print("Yes",end="")
else:
  print("No",end="")