class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        major={}
        n = len(nums)
        for i in nums:
            if i not in major:
                major[i] = 0
            major[i] += 1
            if major[i] > n//2:
                return i

        # candidate = None
        # count = 0
        # for num in nums:
        #     if count == 0:
        #         candidate = num

        #     count += 1 if num == candidate else -1
        # return candidate

