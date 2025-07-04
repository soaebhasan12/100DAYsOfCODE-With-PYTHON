# Code Exercise Exception Handling in hte NATo Phonetic Alphabet Project.




# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/30 - Errors, Exceptions and JSON Data Improving the Password/00 PRACTICE CODE/006 NATO-Phonetic-Alphabet-for-the-Code-Exercise/nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()