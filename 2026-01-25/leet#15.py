class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    for k in range(len(nums)):
                        if k == i or k == j:
                            continue
                        else:
                            if nums[i] + nums[j] + nums[k] == 0:
                                triplet = sorted([nums[i], nums[j], nums[k]])
                                if triplet not in result:
                                    self.result.append(triplet)
        return triplet
    