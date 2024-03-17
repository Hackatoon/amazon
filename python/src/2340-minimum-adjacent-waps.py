class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        res = 0
        low = math.inf
        high = 0
        #[1,1,1,1,1,2]
        hidx = 0 #rightmost index of high
        lidx = len(nums) #left most index of low

        #[1,1]
        for idx, i in enumerate(nums):
            if i >= high:
                high = i
                hidx = idx
            if i < low:
                low = i
                lidx = idx

        #if all the elements are same
        if high == low:
            return 0

        res += lidx - 0
        res += len(nums) -1 - hidx

        # print(lidx,hidx,res)
        if hidx < lidx:
            res -= 1

        return res

        