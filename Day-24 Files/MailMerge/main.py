PLACEHOLDER = "[name]"  #string to be replaced by name


with open("./Input/names.txt") as names_file:
    names = names_file.readlines() #Creates a list from the names file
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        #write to new file
        with open(f"./Output/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)

