import pandas

# {new_key: new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
#  {"letter": "code", "letter": "code"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
word_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code
#  word from a word that the user inputs

user_word = input("Enter a word: ").upper()

output_list = [word_dict[letter] for letter in user_word]
print(output_list)
