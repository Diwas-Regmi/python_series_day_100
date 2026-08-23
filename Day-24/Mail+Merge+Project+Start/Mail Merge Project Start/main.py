#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# i = 0
# While i <8:


with open("Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()
characters = [character.strip() for character in names]

for name in characters:
    with open("Input/Letters/starting_letter.txt", "r") as file:
        context = file.read()
    with open(f"Output/ReadyToSend/letter_for_{name}", "w") as new_content:
        context = context.replace("[name]", name)
        new_content.write(context)

