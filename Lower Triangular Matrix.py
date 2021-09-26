"""
Given a N X N square matrix, transform the Matrix into a Lower Triangular Matrix by setting all the elements except the lower triangle as zero.

​​A Lower triangular matrix is a square matrix (where the number of rows and columns are equal) where all the elements above the diagonal are zero.

Input Format:

The first line of the input contains an integer N which represents the number of rows and the number of columns.

Next N lines represent the elements of the matrix.

Output Format:

Print the Lower Triangular form of the Matrix

Example:

Input:

3

1 -2 3

-2 3 1

3 1 2

Output:

1 0 0

-2 3 0

3 1 2
"""

n=int(input())
q=[]
a=[]
for i in range(n):
  q.append(input().split())
for i in range(n):
  for j in range(0,i+1):
    a.append(q[i][j])
  for j in range(i+1,n):
    a.append("0")
s=0
for i in range(n):
  for j in range(n):
    if j!=n-1:
      print(a[s],"",end="")
    else:
       print(a[s],end="")
    s+=1
  if i!=n-1:
    print("")
