class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
         
        while i < len(nums)-2 :
            if nums[i] == nums[i+1]:
                temp = nums[i]
                count = i+1
                while count < len(nums)-1:
                    nums[count] = nums[count+1]
                    count = count +1
                nums[count] = temp    

        count = 0 
        while count < len(nums)-1: 
            if nums[count] > nums[count+1]:
                return count
            count = count + 1

        return len(nums)    
            
                