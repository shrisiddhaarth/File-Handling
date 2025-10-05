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


file = open("sample.txt", "r")
print("\nUsing Read Method here :")
text = file.read()
print(text)
file.close()

file = open("sample.txt" , "r")
print("\nUsing Readline Method here:")
line1 = file.readline()
line2 = file.readline()
print(line1)
print(line2)
file.close()

file = open("sample.txt", "r")
print("\nUsing Readlines Method here:")
lines = file.readlines()
print(lines)

file = open("sample.txt", "r")
print("\nUsing Readlines Method here:")
lines = file.readlines()
count = 1
for i in lines:
    print(f"{count}) {i}")
    count += 1

file.close()

# With open syntax

with open("sample.txt", "r") as file:
    print("\nReading on ly part of the line(10 charecters)")
    print(file.read(10))
    
with open("sample.txt", "r") as file:
    print("\nReading one single line:")
    print(file.readline())

with open("sample.txt", "r") as file:
    print("\nReading first three lines")
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open("sample.txt" , "r") as file:
    print("\nReading all the lines as a list")
    print(file.readlines())

with open("sample.txt", "r") as file:
    print("\nLooping through file lines")
    for line in file:
        print(line.strip())


