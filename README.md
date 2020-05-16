# [PyLibs](https://plibs.herokuapp.com/)
> A Python implementation of MadLibs (that runs in the browser with Streamlit)

![Made with Python](https://img.shields.io/badge/Made%20With-%20Python%20🐍%20-red?style=flat-square)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Gallery
- To be added

## Demo
[https://plibs.herokuapp.com/](https://plibs.herokuapp.com/)

## Explanation

Before we start, it's important to understand what the following are:
1. **Blanks**: Anything that is meant to be filled by the user. In the texts, blanks are surrounded by two underscores.

    The following are blanks:
      - `__verb__`: meant to be filled by a **verb**
      - `__verb-ing__`: meant to be filled by a **verb** ending in __ing__.
      - `__noun__`: meant to be filled by a **noun**

    Blanks can contain anything, and they serve as a prompt to what the user should enter. The following are valid blanks:

      - `__occupation__`
      - `__animal__`

2. **ID-ed blanks**: Just like blanks, but when the text only has a single one of the blanks. All blanks with a slash followed by a number are ID-ed blanks

    A blank can be used for a name. For instance `__name/1__` and `__dog/1__` are valid ID-ed blanks.

    See the example of a text below.

3. **Fills**: These are what the user enters in a blank.

4. **Texts**: The entire text, which contains blanks and ID-ed blanks for the users to fill. 

Here is an example of a **text**:

### Example
> My dog's name is __dog/1__, and I __verb__ him. __dog/1__ was born in the year __year__. Him and I __verb__ around a lot.


**Blanks**:
- `__verb__` *2
- `__year__`

**ID-ed blanks**
- `__dog/1__`

Here is an example of the possible **fills**:
- `__verb__`: "love"
- `__verb__`: "play"
- `__year__`: "2017"
- `__dog/1__`: "Scruffy"

With the above fills, the output will be:


> My dog's name is Scruffy, and I love him. Scruffy was born in the year 2017. Him and I play around a lot.


## How it works

The below text will be used as the example input **text**:
```
My dog's name is __dog/1__, and I __verb__ him. __dog/1__ was born in the year __year__. Him and I __verb__ around a lot.
```

### 1. Reading the text file
All files in `texts/` are valid texts with **blanks** and **ID-ed blanks**. 

All words are gone through. A word is a **blank** or **ID-ed blank** if it has two underscores before or after ("__"). They are added to a dictionary (`blanks_dict`), where the blank is the key:

```
# blanks_dict
{
  'dog/1': '',
  'verb': [],
  'year': []
}
```

Note how the only **ID-ed blank** (`dog/1`) has the value of an empty string, while the other two have an empty list.

At the same time, `blanks_counter` is created, which stores the number of times each blank is in the text:

```
# blank_counter
Counter({'verb': 2, 'year': 1})
```

Note how the **ID-ed blank** (`dog/1`) is not in the counter. This is because it has only one value.

### 2. Filling the blanks

TO fill **blanks**, `blanks_dict`'s keys are looped, and the user is prompted to enter **fills** for the **blanks**.

For the **ID-ed blanks**, only one **fill** is required.

For the above example, the user is asked for:
- 3* `verb`s
- 1* `year`
- `dog/1`

So at the end of this step, `blanks_dict` could end up looking like this:

```
# blanks_dict
{
  'dog/1': 'Scruffy',
  'verb': ['play', 'love'],
  'year': ['1969']
}
```

Note that the list of keys (`blanks_dict.keys()`) are shuffled before asking for **fills**.


### 3. Creating the output text using the fills

This is probably the simplest. It only involves replacing the the **blanks** in the original text with **fills**, creating the new text. The only thing to look out for is ensuring that punctuation is added after words with blanks. The output for the example can be:

> My dog's name is **Scruffy**, and I **love** him. **Scruffy** was born in the year **1969**. Him and I **play** around a lot.