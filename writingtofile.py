text = "sample text to save\nNew line!"
saveFile = open("exampleFile.txt", "w")
print("File named exampleText.txt created")
saveFile.write(text)
print("Text written to file")
saveFile.close()
print("File closed")
