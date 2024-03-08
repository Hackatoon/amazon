class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []

        hmap = {}

        for i in range(len(nums)):
        
            f = target - nums[i]
            
            if f in hmap:
                return [i, hmap.get(f)]

            hmap[nums[i]] = i