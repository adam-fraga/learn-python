myfile = open("output.txt","w")
myfile.write("My sentence...\n")
myfile.close()

myfile = open("output.txt","r")
content = myfile.read()
print(content)

myfile.close()
