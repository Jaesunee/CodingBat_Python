#URL: https://codingbat.com/prob/p118406

def make_bricks(small, big, goal):
  if small * 1 + big * 5 < goal:
    return False
  if (goal - (big * 5)) > small:
    return False
  if (goal % 5) > small:
    return False
  if (goal / 5) < big and (goal % 5) < small:
    return True
  if small * 1 + big * 5 >= goal:
    return True
  return False
