


# 217 Contains Duplicate


# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

List = [1,2,3,4,4,1]

class Solution:

    # Solution 1
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums)) != len(nums)
        # Compare the length of array with the length of set of (array)
		# Converting into set will automatically remove all the duplicates.
		# That means if the length doesn't match each other, it implies there is duplicate.
        
    
    # Solution 2
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Convert list into dictionary then check if there are more than "two" in values of dictionary.
        # T: O(N)
        # S: O(N)
        
        d = {}
        
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for k, v in d.items():
            if v >= 2:
                return True
            
        return False
    
    # Solution 3
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Convert list into dictionary by using Python library
        # T: O(N)
        # S: O(N)
        
        d = Counter(nums)
        
        for k,v in d.items():
            if v >= 2:
                return True
            
        return False


    # 
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Bitwise operation gives 0 if there is duplicates. 
        # For example, 1 ^ 1 will give you 0.
		# 2 ^ 2 = 0
		# 3 ^ 3 = 0
		# 1 XOR 1 equals 0
		# 1 XOR 0 equals 1
        # T: O(n log n)
        # S: O(1)
        
        if len(nums) == 0:
            return False
        
        # In-place sort.
        # Ex) [1,2,3,1] to [1,1,2,3]
        nums.sort()
        
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i]^curr == 0:
                return True
            curr = nums[i]
        return False


#   Given an integer array nums and two integers k and t, 
#       return true if there are two distinct indices i and j in the array 
#       such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k  

