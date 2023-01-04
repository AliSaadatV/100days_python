#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.read()

with open("Input/Names/invited_names.txt", "r") as file:
    names = [line.strip("\n") for line in file]

for name in names:
    letter = starting_letter.replace("[name]", name)
    path = "Output/ReadyToSend/" + name + ".txt"
    with open(path, mode="w") as file:
        file.write(letter)
