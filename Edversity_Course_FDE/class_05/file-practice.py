#with open("notes.txt", "w") as file:
 #   file.write("This is the 5th class at Eversity \n 30/10/2026 there are")

with open("notes.txt", "r") as file:
    text = file.read()
print(text)  


with open("notes.txt", "w") as file:
    file.write("this is new part 4")