#URL: https://codingbat.com/prob/p145834

def last2(str):
  count = 0
  for x in range(len(str)-2):
    last2 = str[-2:]
    if str[x:x+2] == last2: 
      count += 1
  return count

