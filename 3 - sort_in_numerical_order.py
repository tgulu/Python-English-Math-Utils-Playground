"""
Sort the words in order of their numeric value
"""
string1 = 'zero five two three eight seven four one six nine'
string2 = 'twenty-one twenty-two thirteen seven six ten nineteen nine four fourteen'
string3 = 'thirteen one four twenty thirty-four eight fifteen three thirty-five six thirty-six ten twenty-seven twenty-four thirty-one forty-seven thirty thirty-nine thirty-seven twenty-three forty-two two thirty-three thirty-eight twenty-five eleven seventeen twenty-one forty-nine forty-four zero forty-three twenty-six twelve twenty-nine seven twenty-eight eighteen five fourteen forty-six nine twenty-two forty-one sixteen forty-eight forty thirty-two forty-five nineteen'

# define the mapping of words to numbers
number_mapping = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
    'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
    'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
    'seventy': 70, 'eighty': 80, 'ninety': 90
}

# define a function to convert a string of words to a list of numbers
def words_to_numbers(string):
    words = string.split()
    numbers = []
    for word in words:
        if '-' in word:
            # handle words with hyphens (e.g. "twenty-two")
            parts = word.split('-')
            number = number_mapping[parts[0]] + number_mapping[parts[1]]
        else:
            number = number_mapping[word]
        numbers.append(number)
    return numbers

# sort the words based on their numeric value
string1_sorted = ' '.join(sorted(string1.split(), key=lambda x: words_to_numbers(x)))
string2_sorted = ' '.join(sorted(string2.split(), key=lambda x: words_to_numbers(x)))
string3_sorted = ' '.join(sorted(string3.split(), key=lambda x: words_to_numbers(x)))

print(string1_sorted)
print(string2_sorted)
print(string3_sorted)
