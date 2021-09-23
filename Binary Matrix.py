"""
Given a matrix with M rows and N columns,  you are required to check if the matrix is a Zero-One Matrix. A Zero-One or a Binary matrix is a matrix in which all the elements are either 0 or 1.

Input Format

The first line of the input contains two space separated integers M and N  which  represents  the  number  of  rows  and  the  number  of  columns  respectively.  

Next M lines represent the elements in M rows with each line containing N space separated integers.

Output Format

Print Yes or No
"""

p = ['0','1']
flag = 0
l, s = map(int,input().split())
for i in range(l):
  t = input().split()
  for item in t:
    if item not in p:
      flag = 1
if(flag):
    print('No',end='')
else:
    print('Yes',end='')
