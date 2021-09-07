#URL: https://codingbat.com/prob/p182414

def string_match(a, b):
  count = 0
  for i, x in enumerate(a):
      if i <= (len(a) - 2) and i <= (len(b) - 2):
        if b[i] == x:
          if a[i+1] == b[i+1]:
            count += 1
  return count