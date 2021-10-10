'''
Given a string and width, write a program to convert the given string into different strings of given width separated by newline.


Input Format

The first line contains a string.
The second line contains the width.

Output Format

Print the text wrapped paragraph.

Sample Input 0:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ 
'''
n = input()
m=int(input())
a=0
b=m
for i in range(len(n)//m+1):
  print(n[a:b])
  a+=m
  b+=m