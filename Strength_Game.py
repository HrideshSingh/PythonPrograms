'''
Krishna and Balarama are playing a game of strength. There are n walls arranged in a linear fashion and each wall has a strength value associated with it (the value is guaranteed to be distinct for each wall). The strength value indicates the amount of strength required to break a wall. The breaking of walls must be done only from the ends and any intermediate wall cannot be broken. The first one to break both the walls - one having the least value and the other with the highest value wins the game. Balarama, using his brute force, decides to knock off the walls one by one in a random fashion as he knows they would tumble down easily to his sheer strength. Krishna, on the other hand, decides to calculate the least number of walls to be knocked to achieve a win. Can you help Krishna to compute the minimum number of walls to be knocked?

For example,

If n = 6, with strength values : 1 4 5 3 6 2

It requires a minimum 3 knocks to achieve a win.

(One knock from the left end and two knocks from the right end)


Input Format

The first line contains an integer t indicating the number of test cases.

Next t test cases follow.

The first line of each test case contains one integer n — the number of walls.

The second line of test case contains n distinct integers a1, a2, . . ., an (indicating the strength value for each wall)

Constraints

1 ≤ t ≤ 100

2 ≤ n ≤ 100

 

Output Format

For each test case, output the minimum number of walls to be knocked to win the game.

Example:

Input:

3

5

1 3 4 5 2

8

12 11 13 14 15 16 18 17

4

3 2 4 1

Output:

3

4

2
'''
for t in range(int(input())):
    n = int(input())
    a = [int(i1) for i1 in input().split()]
    mn,mnidx,mx,mxidx=a[0],0,a[0],0
    for i in range(0,n):
        if a[i]<mn:
            mn=a[i]
            mnidx=i
        if a[i]>mx:
            mx=a[i]
            mxidx=i
    val1 = max(mnidx,mxidx)
    val2 = min(mnidx,mxidx)
    print(min([val2-val1+1+n,val1+1,n-val2]))