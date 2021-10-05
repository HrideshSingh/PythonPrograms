'''
Write a program that takes a number as input and prints its factorial as output.

Input Format:

Single line of input contains a number

Output Format:

Display the value of the factorial corresponding to the input

Example:

Input:

3

Output:

6
'''

a=int(input())
fact=1

for i in range(1,a+1):
    fact=fact*i
    
print(fact)
