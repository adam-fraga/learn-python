# ************************************************************************************** #
#                                                                                        #
#                                                    :::     :::::::::    :::   :::      #
#    main.py                                        :+: :+:   :+:    :+:  :+:+: :+:+:    #
#                                                 +:+   +:+  +:+    +:+ +:+ +:+:+ +:+    #
#    By: adamfraga <adam.fraga@live.fr>         +#++:++#++: +#+    +:+ +#+  +:+  +#+     #
#                                              +#+     +#+ +#+    +#+ +#+       +#+      #
#    Created: 2021/09/28 13:37:22 by adam     #+#     #+# #+#    #+# #+#       #+#       #
#    Updated: 2021/09/28 15:55:31 by adam    ###     ### #########  ###       ###i       #
#                                                                                        #
# ************************************************************************************** #

# Écrire un programme qui itère les nombres entiers de 1 à 100. Pour les
# multiples de trois, afficher "Fizz" au lieu du nombre et pour les multiples de
# cinq afficher "Buzz". Pour les nombres qui sont des multiples de trois et
# cinq, afficher "FizzBuzz".

for i in range (100):
    if i % 3 and i % 5:
        print("FizzBuzz")
    elif i % 5:
        print("Buzz")
    elif i % 3:
        print("Fizz")
    
