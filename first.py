#Reading a file
file = open("Sample.txt", "r")
text = file.read()
print(text)
file.close()




file = open("sample.txt", "w")
file.write("Hello my name is siddhaarth.\nI play basketball")
file.close()
file = open("sample.txt","r")
print(file.read())
file.close()

