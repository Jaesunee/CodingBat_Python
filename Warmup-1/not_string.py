#URL: https://codingbat.com/prob/p189441

def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not " + str