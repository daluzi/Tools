# 动态数组
def rob(nums) -> int:
    if not nums:
        return 0
    size = len(nums)
    if size == 1:
        return nums[0]
    first, second = nums[0], max(nums[0], nums[1])
    for i in range(2, size):
        first, second = second, max(first + nums[i], second)
    return max(first, second)

nums1 = [1, 2, 3, 1]
nums2 = [2, 7, 9, 3, 1]
nums3 = [2, 1, 1, 2]
rob(nums3)