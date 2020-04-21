from collections import Counter



text = open('texts/example.md', 'r').read()

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