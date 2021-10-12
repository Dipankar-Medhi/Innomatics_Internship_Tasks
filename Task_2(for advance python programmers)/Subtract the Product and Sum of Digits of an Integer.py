"""Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
Example 1:
Input: n = 234
Output: 15"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summation = 0
        num_str = str(n)
        for i in range(len(str(n))):
            product = int(num_str[i])*product
            summation = int(num_str[i])+summation
            result = product - summation

        return result


print(Solution().subtractProductAndSum(114))
