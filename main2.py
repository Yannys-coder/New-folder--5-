file = open("Codingal.txt", "r")
print(file.read())
file.close()

file = open("Codingal.txt", "r")
print(file.read(5))
file.close()

file = open("Codingal.txt", "a")
file.write("Hi I'm yannys and i am 16 years old")
file.close()