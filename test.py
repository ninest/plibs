import re

"""
Noun: Persons, places, things, ideas, qualities
Pronouns: substitutes for nouns (I, you, he)
Verbs: words that express actions
Adjectives: words that modify nouns (small, big, smelly)
Adverbs: describe verbs, adjectives, adverbs
"""

noun1 = "boy"
verb = "helped"
noun2 = "cow"

text = "I was a good NOUN1. I always VERB the NOUN2s"

completed = ""
for word in text.split(" "):
  new = word

  if "NOUN1" in word:
    print("N1 found: ", word)
    new = word.replace("NOUN1", noun1)
  
  completed += f"{new} "

print(completed)
