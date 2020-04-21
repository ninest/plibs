from collections import Counter
from random import shuffle


text = open('texts/short.md', 'r').read()

blanks_dict = {}
blanks_counter = Counter()

for word in text.split(" "):
  # find if it's a blank
  if "__" in word:
    # find the blank type
    blank_type = word.split("__")[1]

    blanks_dict[blank_type] = []
    blanks_counter[blank_type] += 1

print(blanks_dict)
print(blanks_counter)

# inputting words
# shuffle to randomize order
keys = list(blanks_dict.keys())
shuffle(keys)
print(keys)

for blank in keys:
  # no of the blanks required
  no_required = blanks_counter[blank]

  print(blank, no_required)
  for i in range(0, no_required):
    # asking user to fill the blank
    fill = input(f"{blank}: ")
    blanks_dict[blank].append(fill)
  
print(blanks_dict)


# filling in the blanks with what the user entered
new_text = ""
for word in text.split(" "):
  if "__" in word:
    blank_type = word.split("__")[1]
    word = blanks_dict[blank_type].pop()
  new_text += f"{word} "

print(new_text)