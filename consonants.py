

CONS = 'bcdfhjklmnpqrstvwxz'
text = 'In the Englishqrqrqrqr phrase it is necessary to calculate a unique number of consonant letters'
unique_consonants = []

# Фильтрация только соглассных букв
for char in text:
  if char in CONS or char in CONS.upper() and unique_consonants.index(char)+1:
    unique_consonants.append(char)
  
# Удаление не уникальных букв
for char in unique_consonants:
  while unique_consonants.count(char) > 1:
    unique_consonants.remove(char)


print(unique_consonants)