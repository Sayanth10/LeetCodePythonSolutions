class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = dict()
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in checked:
                return [index, checked[remainder]]
            checked[value] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = int(input("Please enter a number: "))
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)


