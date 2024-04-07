#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

template_path = "Input/Letters/starting_letter.txt"
names_path = "Input/Names/invited_names.txt"
output_path = "Output/ReadyToSend/"

with open(names_path, mode='r') as names:
    for name in names:
        new_letter = ""
        with open(template_path, mode='r') as template:
            for line in template:
                new_letter += line

            new_letter_path = output_path + name.strip("\n").lower() + "_letter.txt"
            print("Writing to: " + new_letter_path)
            with open(new_letter_path, mode='w') as output_file:
                output_file.write(new_letter.replace("[name]", name.strip("\n")))

