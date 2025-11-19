print("Deviner le mot mystère !")
deviner = input("Entrez le mot mystère :")
mot_mystere = "caca"
longueur = len(mot_mystere)
vie = 2 
if deviner == mot_mystere :
    print("Bien joué !, le mot était :",mot_mystere)
else :
    print("T trompé")
    vie -= 1
    print("Il te reste",vie,"vie(s)")

while vie > 0 :
    deviner = input("Réessaie :")
    if deviner == mot_mystere :
        print("Bien joué !, le mot était :",mot_mystere)
        break
    else :
        vie -= 1
        if vie > 0 :
            print("T trompé")
            print("Il te reste",vie,"vie(s)")
        else :
            print("Perdu ! Le mot était :",mot_mystere)