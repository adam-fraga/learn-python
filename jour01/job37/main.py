# ************************************************************************************** #
#                                                                                        #
#                                                    :::     :::::::::    :::   :::      #
#    main.py                                        :+: :+:   :+:    :+:  :+:+: :+:+:    #
#                                                 +:+   +:+  +:+    +:+ +:+ +:+:+ +:+    #
#    By: adamfraga <adam.fraga@live.fr>         +#++:++#++: +#+    +:+ +#+  +:+  +#+     #
#                                              +#+     +#+ +#+    +#+ +#+       +#+      #
#    Created: 2021/09/29 00:33:15 by adam     #+#     #+# #+#    #+# #+#       #+#       #
#    Updated: 2021/09/29 02:07:19 by adam    ###     ### #########  ###       ###i       #
#                                                                                        #
# ************************************************************************************** #


# Pseudo code

#Note ascii 97 a 122 z OK
# Prend str  en parametre OK
# check si param str & lowercase OK
# check alphabet minuscule (table ascii) OK
#Itereration -- sur str[i] tester si str[i] > a str[i]-1 osef (table ascii)
#Sinon intervertir str[i] et str[i]-1
#Si chaine immuable voir pour réorganisation nouvelle liste ou autre methode
# chaque caractere = valeur numerique , trier caractere par valeur croissante,
#parser le tableau et inserer une valeur de sorte à obtenir le mot suivant le plus proche
#Voir avec syntaxe [x:x] et remplissage d'une nouvelle chaine

def too_late_for_cry(string):
    i = 0
    ascii_list = []
    first_value = 97

    # set tableau de 97 a 122 pour comp ascii table
    while i < 26:
        ascii_list.append(first_value)
        first_value += 1
        i +=1
    
    #check parametre entré correspond à consigne
    if str(string):
        i = 0
        while i < len(string):
          char_ascii = ord(string[i])
          if char_ascii < ascii_list[0] or char_ascii > ascii_list[25]:
              print("Toujours pas...")
              exit()
          i += 1
    else:
        print("Sans accents et chaque caractère doit être entre a et z siou'plait :)")
        exit()

   #Itèration inversé sur string
    i = 0
    for i in reversed(string):
        print(ord(i))

string = input("Entrez une chaine de caractère en miniscule")
too_late_for_cry(string)


#Memo Table ascii minuscule de 97 pour a à 122 pour z

