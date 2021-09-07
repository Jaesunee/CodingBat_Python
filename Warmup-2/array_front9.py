#URL: https://codingbat.com/prob/p110166

def array_front9(nums):
  result = False
  for i, x in enumerate(nums):
    if i < 4:
      if x == 9:
        result = True
  return result

