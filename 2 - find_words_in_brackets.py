"""
Find all words in brackets
"""
text = 'one two (three) four (five) six'

text = 'one two (three) four (five) six'
open_bracket_index = -1
words_in_brackets = []

for i, char in enumerate(text):
    if char == '(':
        open_bracket_index = i
    elif char == ')':
        if open_bracket_index != -1:
            words_in_brackets.append(text[open_bracket_index+1:i])
            open_bracket_index = -1

print(words_in_brackets)

['three', 'five']