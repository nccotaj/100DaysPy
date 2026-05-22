# file = open("myfile.txt")


# contents = file.read() #outputs file contents as a string
# print(contents)
# file.close() #make sure you close the files so that you dont waste resources



#alternative way using "with"

# with open("myfile.txt", mode = "r") as file:  #with keyword closes the file after we are done with it 
#     contents = file.read()
#     print(contents)


#write
# with open("myfile.txt", mode="w") as file:
#     file.write("My name is ")

with open("myfile.txt", mode="a") as file:
    file.write("Nicholas Cotaj ")

with open("newfile.txt", mode="w") as file:
    file.write("New File")


    

