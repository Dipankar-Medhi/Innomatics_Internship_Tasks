"""There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.

Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] """


class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        # initializing an empty array for storing the solution
        result = []

        # iterating through the given array and checking if the element is greater than or equal to the greatest element.
        for i in range(len(candies)):

            # if the element is greatest than or equal to the greatest element then we append true to the result array.
            if candies[i] + extraCandies >= self.greatestNoOfCandies(candies):
                result.append(True)

        # else we append false.
            else:
                result.append(False)
        return result

# function for finding the greatest element in the given array.
    def greatestNoOfCandies(self, candies):
        greatest = candies[0]
        for i in range(len(candies)):
            if greatest < candies[i]:
                greatest = candies[i]
        return greatest


print(Solution().kidsWithCandies([4, 2, 1, 1, 2], 1))
