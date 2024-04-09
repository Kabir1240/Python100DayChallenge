import pandas
PATH = "nato_phonetic_alphabet.csv"


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
df = pandas.read_csv(PATH)
new_dict = {row.letter:row.code for (index, row) in df.iterrows()}

user_input = input("Enter a word: \n")
result = [new_dict[char.upper()] for char in user_input]
print(result)