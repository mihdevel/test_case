import random

mass = [ random.randrange(1, 1000) for _ in range(20) ]

enter_number = 500
max_numbers =[]

for number in mass:
  if number > enter_number:
    max_numbers.append(number)
    if len(max_numbers) == 3: break

print(max_numbers)