import random

text = "I'm a __noun__, here my friend, also a __noun__. Every day, we __verb__ the cows, very __adverb__."

blanks_dict = {
  "noun": ["boy", "boy2"],
  "verb": ["eat"],
  "adverb": ["nicely"]
}

completed = ""

for word in text.split(" "):
  # checking if it's a blank
  if ("__" in word):
    blank_type = word.split("__")[1]
    print("Blank type: ", blank_type)

    # pick a random blank from the dict
    fill = random.choice(blanks_dict[blank_type])
    print("Filling with: ", fill)

    # remove that blank from the dict
    blanks_dict[blank_type].remove(fill)

    # finally, replace the __blank_type__ with the "fill"
    word = word.replace(f"__{blank_type}__", fill)


    print("\n")



  completed += f"{word} "

print(completed)