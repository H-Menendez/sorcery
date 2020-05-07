import random as ra

def DeSix(n):
    resultat=int()
    for i in range (n) :
        resultat+=ra.randint(1,6)
    return resultat


def paragraphe_301():
    texte=["A votre gauche, du côté ouest du passage, il y a une porte de bois brut",
           "grossièrement taillé. Vous tendez l'oreille et vous percevez un bruit qui",
           "pourrait être le ronflement d'une quelconque créature."]
    
    for loop in range(len(texte)):
        print(texte[loop])

    print("Désirez-vous ouvrir cette porte ou continuer vers le nord?")
    
    choix=input("Entrez votre choix porte ou nord :")

    if choix=="porte":
        paragraphe_82()
    elif choix=="nord":
        paragraphe_208()
        

def paragraphe_208():
    texte=["Un peu plus loin dans le passage qui longe le mur ouest, vous trouvez",
           "une autre porte. Vous collez votre oreille contre le panneau, mais vous",
           "n'entendez rien."]
    
    for loop in range(len(texte)):
        print(texte[loop])

    print("Désirez-vous ouvrir cette porte ou poursuivre votre chemin?")
    
    choix=input("Entrez votre choix porte ou poursuivre :")

    if choix=="porte":
        paragraphe_397()
    elif choix=="poursuivre":
        paragraphe_363()

def combat(endE,habE,endH,habH):
    while True :
       FAE=DeSix(2)+habE
       FAH=DeSix(2)+habH
       print("La force d'attaque de votre ennemi est de",FAE,", votre force d'attaque est de",FAH,".")
       if FAE < FAH :
           endE=endE-2
           print("L'ennemi perd 2 points d'ENDURANCE, il lui en reste",endE,".\n")
           if endE<=0 :
               break
       elif FAE > FAH :
           endH=endH-2
           print("Vous perdez 2 points d'ENDURANCE, il vous en reste",endH,".\n")
           if endH<=0 :
               break
    if endE<=0 :
        print("\nFélicitations, vous avez vaincu votre adversaire!")
        print("Il vous reste",endH,"points d'endurance.")
    else :
        print("Vous avez été vaincu!")
        print("Vous devez recommencer l'histoire au paragraphe 1.")

