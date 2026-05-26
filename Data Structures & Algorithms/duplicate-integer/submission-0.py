class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        og=set()
        for num in nums:
            if num in og:
                return True
            else:
                og.add(num)
        return False
        
            
            
        