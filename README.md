# PyLibs
> A Python implementation of MadLibs

![Made with Python](https://img.shields.io/badge/Made%20With-%20Python%20🐍%20-red?style=flat-square)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

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
```
My dog's name is __dog/1__, and I __verb__ him. __dog/1__ was born in the year __year__.
```

**Blanks**:
- `__verb__`
- `__year__`

**ID-ed blanks**
- `__dog/1__`

Here is an example of the possible **fills**:
- `__verb__`: "love"
- `__year__`: "2017"
- `__dog/1__`: "Scruffy"

With the above fills, the output will be:
```
My dog's name is Scruffy, and I love him. Scruffy was born in the year 2017.
```

## How it works

### 1. Reading the text file
All files in `texts/` are valid texts with **blanks**.