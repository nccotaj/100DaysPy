import pandas

nato_DF = pandas.read_csv("nato_phonetic_alphabet.csv")

#Creates phoentic dictionary
nato_dict = {row.letter:row.code for (index,row) in nato_DF.iterrows()}

def generate_phonetic():
    try:
        word = input('Enter word: ').upper()
        output_list = [nato_dict[letter] for letter in word]
    except:
        print("Letters Only")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()