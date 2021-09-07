#URL: https://codingbat.com/prob/p160533

def close_far(a, b, c):
  if (abs(a - b) < 1 or abs(a - b) == 1) and (abs(a-c) > 2 or abs(a-c) == 2) and (abs(b-c) > 2 or abs(b-c) == 2):
    return True
  if (abs(a - c) < 1 or abs(a - c) == 1) and (abs(a-b) > 2 or abs(a-b) == 2) and (abs(c-b) > 2 or abs(c-b) == 2):
    return True
  else:
    return False
