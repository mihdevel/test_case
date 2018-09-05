def func1(number):
  return 2 if number == 1 else 1


def func2(number):
  l = [1, 2]
  try:
    l[number]
    return 2
  except IndexError: return 1


for x in [1, 2]:
  print(func1(x))
  print(func2(x))