"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3"""


class Solution(object):
    def numTeams(self, rating):
        result = 0
        for i in range(1, len(rating)-1):
            less, greater = [0]*2, [0]*2
            for j in range(len(rating)):
                if rating[i] > rating[j]:
                    less[i < j] += 1
                if rating[i] < rating[j]:
                    greater[i < j] += 1
            result += less[0]*greater[1] + greater[0]*less[1]
        return result


print(Solution().numTeams([2, 5, 3, 4, 1]))
