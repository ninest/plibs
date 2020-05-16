import streamlit as st
from collections import Counter
from random import shuffle

"""
# Plibs

MadLibs in Python
"""

text_selection_list =  ("Example", "Short", "IDed")

# let users choose a text
"## Choose a text"

text_selection = st.selectbox(
    "text",
    text_selection_list
)

file = text_selection.lower() + ".md"
text = open(f'texts/{file}', 'r').read()


"## Fill in the blanks"

# Create dictionaries
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

# create text inputs
keys = list(blanks_dict.keys())

@st.cache
def shuffle_keys():
  shuffle(keys)
shuffle_keys()


for blank in keys:
  if "/" in blank:
    # remove the ID number
    label = blank.split("/")[0]
    # convert the _ to a space
    label = label.replace("_", " ")
    blanks_dict[blank] = st.text_input(label, key=blank)
    # blank

  else:
    no_required = blanks_counter[blank]
    counter = 0
    for i in range(0, no_required):
      # convert the _ to a space
      label = blank.replace("_", " ")
      blanks_dict[blank].append(
        st.text_input(label, key=f'blank{no_required}{counter}')
      )
      # f'blank{no_required}{counter}'
      counter += 1
  

if st.button("Done"):
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
  
  # Leave a line to add some breathing space
  ""
  new_text

