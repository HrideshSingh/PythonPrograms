'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        MIN=-2147483648
        MAX=2147483647
        
        if(x>=0):
            res=str(x)
            res=res[::-1]
            res=int(res)
        else:
            res=str(x)
            res=res[::-1]
            res=res.replace('-','')
            res='-'+res
            res=int(res)