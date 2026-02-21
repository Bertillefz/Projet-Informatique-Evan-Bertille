from questions import *
from labyrinthe import *

def choix_difficulte():
    print(f"\nCHOIX DE LA DIFFICULTE")
    print("Difficultés disponibles :")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    while True:
        try:
            type_choix = int(input("Choisissez le type (1 ou 2 ou 3) : "))
            if type_choix == 1:
                return 10
            elif type_choix == 2:
                return 5
            elif type_choix == 3:
                return 3
            else:
                print("Choix invalide. Veuillez entrer 1 ou 2 ou 3.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")




def main():
    print("Bienvenue à Labyrinthe !!")
    choix = input("\nEntrez R pour visualiser les règles du jeu... ")
    if choix == "R":
        print(f"\nREGLES DU JEU")
        print("Vous êtes dans un labyrinthe")

    print(f"\nCHOIX DU TYPE DE QUESTIONS ")
    print("Voici les choix possibles :")
    print("G - Questions sur la géographie ")
    print("T - Tests ")
    while True:
        choix_jeu = input("Saisissez une de ces 3 options : G ou T ").strip().upper()
        if choix_jeu in ("G","T"):
                break
        print("Veuillez faire un choix valide : G ou T...")

    if choix_jeu == "G":
        print("\nVous avez choisi des questions de géographie")
        difficulte = choix_difficulte()
        input("\nAppuyez sur Entrée pour commencer le jeu...")
        labyrinthe = Labyrinthe(difficulte, questions_geographie, profondeur_max = 5)
        jeu(labyrinthe)
    elif choix_jeu == "T":
        print("\nVous avez choisi de faire un test")
        difficulte = choix_difficulte()
        input("\nAppuyez sur Entrée pour commencer le jeu... ")
        labyrinthe = Labyrinthe(difficulte, questions_tests, profondeur_max = 2)
        jeu(labyrinthe)

    while True:
        choix_fin= input("\nVoulez vous relancer une partie? (Oui/Non)").strip().upper()
        if choix_fin in ("OUI","NON"):
            break
        print("\nVeuillez choisir svp (Oui/Non)")

    if choix_fin == "OUI":
        main()
    elif choix_fin == "NON":
        print("\nNous vous remercions d'avoir joué à Labyrinthe !!")

if __name__ == "__main__":
    main()

