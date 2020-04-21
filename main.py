from collections import Counter
from random import shuffle


text = open('texts/example.md', 'r').read()

blanks_dict = {}
blanks_counter = Counter()

for word in text.split(" "):
  # find if it's a blank
  if "__" in word:
    # find the blank type
    blank_type = word.split("__")[1]

    # check if it's an IDed blank
    if "/" in blank_type:
      blanks_dict[blank_type] = ""
    else:
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
  # first check if it's an IDed blank
  if "/" in blank:
    fill = input(f"{blank}: ")
    # since there is only one possible fill for Ided, no array here
    blanks_dict[blank] = fill
  else:
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
  suffix = ""  # this is punctuation (if any)
  
  if "__" in word:
    blank_type = word.split("__")[1]

    # checking if there's a punctuation
    try: suffix = word.split("__")[2]
    except: pass

    if "/" in blank_type:
      word = blanks_dict[blank_type]
    else:
      word = blanks_dict[blank_type].pop()
  new_text += f"{word}{suffix} "

print(new_text)
