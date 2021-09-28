# ************************************************************************************** #
#                                                                                        #
#                                                    :::     :::::::::    :::   :::      #
#    main.py                                        :+: :+:   :+:    :+:  :+:+: :+:+:    #
#                                                 +:+   +:+  +:+    +:+ +:+ +:+:+ +:+    #
#    By: adamfraga <adam.fraga@live.fr>         +#++:++#++: +#+    +:+ +#+  +:+  +#+     #
#                                              +#+     +#+ +#+    +#+ +#+       +#+      #
#    Created: 2021/09/28 23:25:53 by adam     #+#     #+# #+#    #+# #+#       #+#       #
#    Updated: 2021/09/29 00:31:06 by adam    ###     ### #########  ###       ###i       #
#                                                                                        #
# ************************************************************************************** #

# Pseudo code////
# Note de 0 a 100
# si etudiant note entre 0 et 40 test KO
# sinon si etudiant note > 40 test OK
# si (note + un des 3 index suivant) % 5 == 0 alors note = note + 3

def calcul_notes(student_notes):
    print(student_notes)
    note_list = []
    new_notes = []
    i = 0

    while i < 100:
            note_list.append(i)
            i += 1

    for student_note in student_notes:
        student_note = int(student_note)
        j = 0
        # Vérifie si les 3 indexes suivant la note sont ou non multiple de 5
        for j in note_list:
             if student_note == note_list[j]:
                 if (note_list[j] + 1) % 5 == 0:
                     new_notes.append(student_note + 1)
                     break
                 elif (note_list[j] + 2) % 5 == 0:
                     new_notes.append(student_note + 2)
                     student_note = student_note + 2
                     break
                 elif(note_list[j] + 3) % 5 == 0:
                     new_notes.append(student_note + 3)
                     student_note = student_note + 3
                     break
                 else:
                     new_notes.append(student_note)
                     break
             j += 1

    return(new_notes)
        
nb_students = input("Combien de notes souhaitez vous entrer? \n")

i = 0
notes = []
while i < int(nb_students):
    note = input("Entrer la note de l'élève numero " + str(i + 1) + "\n")
    notes.append(note)
    i += 1

calcul_notes(notes)
