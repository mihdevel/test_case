import random

my_dict = { x : random.randrange(1, 1000) for x in range(20) }
inverting_dict = dict(zip(my_dict.values(), my_dict.keys()))

print(my_dict)
print(inverting_dict)