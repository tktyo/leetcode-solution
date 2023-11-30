# intersection of Two Arrays
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        table = [-1] * 1001
        result = []
        for i in nums1:
            table[i] = 1
        for i in nums2:
            if table[i] == 1:
                table[i] += 1
                if table[i] == 2:
                    result.append(i)
        return result

        # method 2
        # return list(set(nums1)&set(nums2))
