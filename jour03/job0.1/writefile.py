user_string = input("Renseigner une chaine de caractère")

if(user_string):
    user_file = open("output.txt","w")
    user_file.write(user_string + "\n")
    user_file.close()

 
