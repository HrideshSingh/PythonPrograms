'''
Given an integer input 'n', print a number triangle of n lines as shown in the example.
Private Test cases used for evaluation	Input	Expected Output	Actual Output	Status
Test Case 1	
1
 1
1
Passed
Test Case 2	
4
 1\n
22\n
333\n
4444
1\n
22\n
333\n
4444
Passed
'''
n=int(input())
for i in range(1,n+1):
  for j in range(1,i+1):
    print(i,end="")
  if i!=n:
    print("")
  else:
    print("",end="")