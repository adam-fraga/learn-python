# ************************************************************************************** #
#                                                                                        #
#                                                    :::     :::::::::    :::   :::      #
#    main.py                                        :+: :+:   :+:    :+:  :+:+: :+:+:    #
#                                                 +:+   +:+  +:+    +:+ +:+ +:+:+ +:+    #
#    By: adamfraga <adam.fraga@live.fr>         +#++:++#++: +#+    +:+ +#+  +:+  +#+     #
#                                              +#+     +#+ +#+    +#+ +#+       +#+      #
#    Created: 2021/09/28 13:47:13 by adam     #+#     #+# #+#    #+# #+#       #+#       #
#    Updated: 2021/09/28 18:27:13 by adam    ###     ### #########  ###       ###i       #
#                                                                                        #
# ************************************************************************************** #

cols = input("Entrer la largeur de votre rectangle")
rows = input("Entrer la hauteur de votre rectangle")
cols = int(cols)
rows = int(rows)


def print_rectangle(cols, rows):
    for y in range(rows):
        if y:
            print(end="")
        for x in range(cols):
            if x == 0:
                print("|", end="")
            elif x == cols - 1:
                print("|")
            elif y == 0 or y == rows - 1:
                print("-", end="")
            else:
                print(" ", end="")


print_rectangle(cols, rows)
