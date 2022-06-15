nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
  complete = {}
  for i, value in enumerate(nums):
    rest = target - nums[i]
    if rest in complete:
      return [i, complete[rest]]
    complete[value] = i

twoSum(nums=nums, target=target)
