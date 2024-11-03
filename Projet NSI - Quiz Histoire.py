import random

def stockage(points):
    try:
         with open("score.txt", "a") as fichier:
            fichier.write("\n")
            fichier.write(str(points))
    except FileNotFoundError:
         print("Le fichier contenant les réponses du quiz est introuvable. Contactez le développeur afin d'obtenir de l'aide.")

def tableau():
    # Récupère les scores depuis le fichier score.txt
    liste_scores = list(open('score.txt'))

    print("---------------------------")

    # Affiche l'ensemble des scores enregistrés
    for i, score in enumerate(liste_scores):
        index = str(i + 1)
        print(f"| Score partie {index.rjust(3)} | {score.strip().rjust(4)} |")

    print("---------------------------")

def Quiz(niveau):
    print("\nPendant Le quiz, écrivez 7700 (code de détresse aviaiton) à tous moments pour arreter la partie.")
    points = 0

    for i in range(niveau):

        try:
            with open('questions.txt', 'r', encoding='utf-8') as fichier:
                lignes = fichier.readlines()
                rang_question = random.randint(1, len(lignes) - 1)
                question = lignes[rang_question].strip()
        except FileNotFoundError:
            print("Le fichier contenant les réponses du quiz est introuvable. Contactez le développeur afin d'obtenir de l'aide.")

        try:
            with open("reponses.txt", "r", encoding='utf-8') as fichier:
                lignes = fichier.readlines()
                reponse = lignes[rang_question].strip()
        except FileNotFoundError:
            print("Le fichier contenant les réponses du quiz est introuvable. Contactez le développeur afin d'obtenir de l'aide.")

        essais = 1

        while True:

            while True:
                try:
                    rep_user = int(input(question))
                    assert type(rep_user) == int
                    break
                except ValueError:
                    print("Attention ! Veuillez entrer une année en nombre, pas de phrase.")

            if rep_user == 7700:
                print("Les point de la partie ont bien été enregistrés.")
                stockage(points)
                Menu()
                break

            else:
                if rep_user == int(reponse) or rep_user == 0000: # PENSER A MODIFIER LE CHEAT CODE

                    print(f"Bravo, tu as répondu à la question : {question} en {essais} essais, tu as donc {1 / essais:.2f} point")
                    points += 1 / essais
                    break

                else:

                    if essais == 5:
                        print("Tu as échouer à cette question.")
                        break

                    else:

                        if rep_user > int(reponse):
                            print("La date est inférieur à votre réponse")
                            essais += 1

                        if rep_user < int(reponse):
                            print("La date est supérieur à votre réponse")
                            essais += 1


    print(f"Félicitation, tu viens de finir la partie!! Tu as au total {points} points")
    stockage(points)

    Menu()

def Jeu():

    while True:
        try:
            chx = str(input(f"Voulez vous faire un niveau: \n Facile : Une partie avec 5 questions. \n Moyen : Une partie avec 10 questions \n Difficile: Une partie avec 20 question"))

            assert chx == "Facile" or chx == "Moyen" or chx == "Difficile"
            break
        except AssertionError:
            print("Veuillez rentrer une sélection valide (Facile, Moyen, Difficile")

    if chx == "Facile":
        Quiz(5)
        return 5

    if chx == "Moyen":
        Quiz(10)
        return 10

    if chx == "Difficile":
        Quiz(20)
        return 20

def AddQ():
    try:
        with open('questions.txt', 'a', encoding='utf-8') as fichier:
            question = str(input("Entrez votre nouvelle question :"))
            fichier.write("\n")
            fichier.write(question)
    except FileNotFoundError:
        print("Le fichier contenant les réponses du quiz est introuvable. Contactez le développeur afin d'obtenir de l'aide.")
    try:
        with open('reponses.txt', 'a', encoding='utf8') as fichier:
            reponse = str(input("Entrez la réponse à cette question :"))
            fichier.write("\n")
            fichier.write(reponse)
    except FileNotFoundError:
        print("Le fichier contenant les réponses du quiz est introuvable. Contactez le développeur afin d'obtenir de l'aide.")

def Menu():

    print("Bienvenue dans le Quiz d'hsitoire !")

    while True:
        try:
            chx = str(input(f"Voulez vous accerder au :\n1: Quiz \n2: Tableau des scores (tapez Scores) \n3: Ajouter vos propres questions (AddQ)"))

            assert chx == "Quiz" or chx == "Scores" or chx == "AddQ"
            break
        except AssertionError:
            print("Veuillez rentrer une sélection valide (Quiz, Scores, AddQ)")

    if chx == "Quiz":
        Jeu()

    if chx == "AddQ":
        AddQ()

    if chx == "Scores":
        tableau()
        Menu()

Menu()
