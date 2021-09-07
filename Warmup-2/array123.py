#URL: https://codingbat.com/prob/p193604

def array123(nums):
  for i, x in enumerate(nums):
    if i <= (len(nums) -3):
      if x == 1:
        if nums[i+1] == 2:
          if nums[i+2] == 3:
            return True
  return False