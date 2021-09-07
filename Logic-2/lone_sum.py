#URL: https://codingbat.com/prob/p143951

def lone_sum(a, b, c):
  sum = 0
  if a == b and c == b:
    return sum
  if a == b:
    return c
  if a == c:
    return b
  if b == c:
    return a
  return a + b + c
