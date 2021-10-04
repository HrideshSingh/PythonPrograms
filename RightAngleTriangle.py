'''
Write a program that takes 3 integers as input and checks whether they can form the sides of a right angled triangle or not. Print YES if they can form a right angled triangle. NO, otherwise.

Input Format:

Single line of input contains three numbers 

Output Format:

Print YES or NO

Example:

Input:

5 4 3

Output:

YES

Example:

Input:

10 20 30

Output:

NO
'''

a = [int(x) for x in input().split()[:3]]
a.sort()
if(a[2]*a[2]==a[0]*a[0]+a[1]*a[1]):
    print("Yes")
else:
    print("No")
