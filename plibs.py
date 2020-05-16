import streamlit as st
from collections import Counter
import random
import nltk
import string

nltk.download('punkt')

abbrs = {
  "verb-ing": "verb ending in ing"
}

def main():
  """
  # Plibs

  A python implementation of MadLibs with Streamlit
  """

  text_selection_list = ("Example", "Short", "IDed", "Be Kind", "Letter from camp", "Sick note", "Simple letter")

  # let users choose a text
  "## Choose a text"

  text_selection = st.selectbox("text",text_selection_list)

  file = text_selection.replace(" ", "-").lower() + ".md"
  text = open(f'texts/{file}', 'r').read()


  "## Fill in the blanks"

  # Create dictionaries
  blanks_dict, blanks_counter = get_blanks(text)

  blanks_dict

  # create text inputs
  keys = list(blanks_dict.keys())
  keys = shuffle_list(keys)


  for blank in keys:
    if "/" in blank:
      # remove the ID number
      label = blank.split("/")[0]
      # convert the _ to a space
      label = label.replace("_", " ")
      blanks_dict[blank] = st.text_input(get_label(label), key=blank)
      # blank

    else:
      no_required = blanks_counter[blank]

      for i in range(0, no_required):
        # convert the _ to a space
        label = blank.replace("_", " ")
        blanks_dict[blank].append(
            st.text_input(get_label(label), key=f'blank{no_required}{i}')
        )


  if st.button("Done"):
    blanks_dict
    new_text = fill_blanks(text, blanks_dict)
    new_text


@st.cache
def shuffle_list(lst):
  return random.sample(lst, len(lst))

def get_label(strng):
  # see if label exists
  try: label = abbrs[strng]
  except: label = strng

  label = label.replace("-p", " (plural)")

  return label

def get_blanks(text):
  blanks_dict = {}
  blanks_counter = Counter()
  for word in nltk.word_tokenize(text):
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
  
  return blanks_dict, blanks_counter


def fill_blanks(text, blanks_dict):
  # filling in the blanks with what the user entered
  new_text = ""

  # for word in text.split(" "):
  for paragraph in text.split("\n"):
    # paragraph

    previous_word = ""
    for word in nltk.word_tokenize(paragraph):
      prefix = ""
      suffix = ""  # this is punctuation (if any)

      if "__" in word:
        blank_type = word.split("__")[1]

        # checking if there's a punctuation
        try: suffix = word.split("__")[2]
        except: pass

        # also check for prefix (this is most likely markdown formatting)
        # ex: **__verb__**
        try: prefix = word.split("__")[0]
        except: pass
        

        if "/" in blank_type:
          word = blanks_dict[blank_type]
        else:
          word = blanks_dict[blank_type].pop()

      # if punctuation, don't add space
      if word in string.punctuation:
        # replace final space with punctiation
        new_text = new_text[:-1] + f'{word} '
      else:
        # check if it's the sentence start
        if previous_word == "." or previous_word == "\n" or previous_word == "":
          # and capitalize if so
          word = word.capitalize()
        new_text += f"{prefix}{word}{suffix} "
      
      previous_word = word

    # add new paragraph
    new_text += "\n"
  # add line breaks
  new_text = new_text.replace("\\", "\n")

  return new_text

if __name__ == '__main__':
  main()