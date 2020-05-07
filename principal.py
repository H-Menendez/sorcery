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

