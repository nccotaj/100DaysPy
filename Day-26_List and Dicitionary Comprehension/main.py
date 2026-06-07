import pandas

nato_DF = pandas.read_csv("nato_phonetic_alphabet.csv")

#Creates phoentic dictionary
nato_dict = {row.letter:row.code for (index,row) in nato_DF.iterrows()}

word = input('Enter word: ').upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)