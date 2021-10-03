"""
Given a list of integers and a value k, print the kth largest element in the list. (All the elements in the list are guaranteed to be distinct).

Input Format:

First line of the input contains a list of integers

Second line of the input contains a value k

Output Format:

Display the kth largest element in the list

Example:

Input:

5 3 6 10 2

3

Output:

5
"""

arr = [int(i) for i in input().split()]
k=int(input())


arr.sort(reverse=True)
print(arr[k-1],end="")