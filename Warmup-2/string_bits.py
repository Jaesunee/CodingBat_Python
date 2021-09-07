#URL: https://codingbat.com/prob/p113152

def string_bits(str):
  string = ""
  for i, x in enumerate(str):
    if i % 2 == 0:
      string += x
  return string