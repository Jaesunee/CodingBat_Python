#URL: https://codingbat.com/prob/p153599

def front_back(str):
  if len(str) == 1:
      return str
  else:
    return str[len(str)-1:] + str[1: len(str)-1] + str[:1]