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



def tour_jeu(labyrinthe, question):
    labyrinthe.afficher_question(question)
    labyrinthe.chemin.append(question) # on ajoute à la PILE
    options_melangees = labyrinthe.options_possibles()
    print(f"Choix possibles: {options_melangees[0][0]} (chemin A), {options_melangees[1][0]} (chemin B)")

    saisie = None
    while saisie not in ["A", "B"]:
        saisie = input("Veuillez indiquer le chemin que vous souhaitez prendre (A ou B) : ").strip().upper()

    if labyrinthe.reponse_valide(saisie, options_melangees) :
        nouvelle_question = question.gauche
    else :
        nouvelle_question = question.droite
    labyrinthe.noeud_courant = nouvelle_question
    labyrinthe.profondeur_courante += 1
    return nouvelle_question

def cul_de_sac(labyrinthe):
    print("\nCUL DE SAC")
    print("Vous êtes arrivé dans un cul de sac :/")
    input("\nAppuyez sur Entrée pour pouvoir revenir au question précédente... ")

    if len(labyrinthe.chemin) >=1 :
        question = labyrinthe.chemin.pop()
        labyrinthe.noeud_courant = question
        labyrinthe.profondeur_courante -=1
        if labyrinthe.noeud_courant in labyrinthe.noeuds_erreurs:
            labyrinthe.noeuds_erreurs.remove(labyrinthe.noeud_courant)
    else :
        return
    labyrinthe.afficher_question(question)

    while labyrinthe.profondeur_courante >= 1 and len(labyrinthe.chemin) >= 1 :
        saisie = input("Remonter à la question précédente encore (oui/non) : ")
        if saisie == "oui":
            question = labyrinthe.chemin.pop()  # il y a des piles ici aussi
            labyrinthe.noeud_courant = question
            labyrinthe.profondeur_courante -= 1
            labyrinthe.afficher_question(question)
            if labyrinthe.noeud_courant in labyrinthe.noeuds_erreurs:
                labyrinthe.noeuds_erreurs.remove(labyrinthe.noeud_courant)
        else :
            break  # on sort de cul de sac




def jeu(labyrinthe):
    while labyrinthe.peut_jouer() :
        while labyrinthe.peut_jouer() and labyrinthe.profondeur_courante != labyrinthe.arbre.profondeur_max + 1 :
            labyrinthe.noeud_courant = tour_jeu(labyrinthe, labyrinthe.noeud_courant)
        if len(labyrinthe.noeuds_erreurs) == 0 and labyrinthe.profondeur_courante == labyrinthe.arbre.profondeur_max + 1 :
            print(labyrinthe.victoire())
            break # on sort du jeu
        elif len(labyrinthe.noeuds_erreurs) != 0 and labyrinthe.peut_jouer() and labyrinthe.profondeur_courante == labyrinthe.arbre.profondeur_max + 1:
            cul_de_sac(labyrinthe)
        else :
            print("Défaite :( temps écoulé ")
            break



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


"hello"
