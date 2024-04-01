class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        for startPointIndex in range(len(nums)-2):
            if startPointIndex >0 and nums[startPointIndex] == nums[startPointIndex+1]:
                startPointIndex +=1
            start = nums[startPointIndex]
            target = -start
            
            left_index = startPointIndex+1
            right_index = len(nums)-1
            
            self.twosum(left_index, right_index, target, nums, results) #need to call itself function using self.
        return results


    def twosum(self, left, right, target, nums, results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target,nums[left], nums[right]])
                left +=1
                right -=1
                
                
            if nums[left] + nums[right] < target:
                left +=1
            
            if nums[left] + nums[right] > target:
                right -=1
        
        

        