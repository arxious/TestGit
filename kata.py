class Solution:
    def twoSum(self, nums, target: int):
        seen = {}
        complement = None
        for i, x in enumerate(nums):
            complement = target - x
            if seen.get(complement):
                print(i)
                seen[x] = i  # This stores the index (important)
            else:
                complement = [i, seen.get(complement)]

        return complement

sol = Solution()

my_arr = [1,2,3,4,5]

print(sol.twoSum(my_arr, 9))




