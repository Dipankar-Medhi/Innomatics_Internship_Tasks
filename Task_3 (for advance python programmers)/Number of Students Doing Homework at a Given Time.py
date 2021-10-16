"""
Given two integer arrays startTime and endTime and given an integer queryTime.
The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

 
Example 1:
Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
"""


class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        result = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                result += 1

        return result


print(Solution().busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 4))
