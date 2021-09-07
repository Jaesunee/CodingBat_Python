#URL: https://codingbat.com/prob/p118366

def string_splosion(str):
  string = ""
  for x in range(len(str)+1):
     string += str[0:x]
  return string

