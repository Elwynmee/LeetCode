class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a dictionary
        complements = {}
        #iterate through the array
        for i, num in enumerate(nums):
            # check if the current number complement is in the dictionary
            complement  = target - num
            if complement in complements:
                return [complements[complement], i]
            
        # return the indices of the 2 numbers
        
        #store the current number and its index in the dictionary
            complements[num] = i
        #if no solution is found return
        return[]
  
