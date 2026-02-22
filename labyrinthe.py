#POO ici

import random
import time
import copy
from collections import deque

#Le noeud : la question, ses options et sa réponse correcte
class Noeud : # noeud de l'arbre
    def __init__(self, donnees_question):
        self.question = donnees_question["question"]
        self.options = donnees_question["options"]
        self.reponse = donnees_question["reponse"]
        self.droite = None # chemin B
        self.gauche = None # chemin A
        self.parent = None # la question d'avant

#L'arbre : la structure en elle-même du graphe avec les différents noeuds
class Arbre:
    def __init__(self, type_questions, profondeur_max):
        self.type_questions = type_questions.copy()
        self.profondeur_max = profondeur_max
        self.racine = self.creer_arbre(1)

    def creer_arbre(self, profondeur_actuelle):
        if self.profondeur_max < profondeur_actuelle :
            return None

        donnees_question = random.choice(self.type_questions)
        self.type_questions = [d for d in self.type_questions if d != donnees_question]
        noeud = Noeud(donnees_question)

        noeud.gauche = self.creer_arbre(profondeur_actuelle + 1)
        noeud.droite = self.creer_arbre(profondeur_actuelle + 1)

        if noeud.gauche is not None :
            noeud.gauche.parent = noeud
        if noeud.droite is not None :
            noeud.droite.parent = noeud
        return noeud


#Labrytinthe : l'arbre de jeu et le jeu en lui-même
class Labyrinthe:
    def __init__(self, difficulte, donnees, profondeur_max):
        self.arbre = Arbre(donnees, profondeur_max)
        self.noeud_courant = self.arbre.racine
        self.profondeur_courante = 1
        self.temps_depart = time.time()
        self.difficulte = difficulte
        self.noeuds_erreurs = []
        self.chemin = [] # PILE

    def options_possibles(self):
        " cette fonction retourne la liste des options possibles mélangées avec un chemin associé"
        options = [self.noeud_courant.options[0], self.noeud_courant.options[1]]
        random.shuffle(options) #pour éviter que la 1e réponse soit toujours la bonne réponse
        return [(options[0], "A"), (options[1], "B")]

    def reponse_valide(self, reponse, options):
        "cette fonction permet de vérifier que la réponse à la question est correcte"
        #la réponse est A ou B
        # les options = options possibles [(option 1 ou 2, A), (option 1 ou 2, B)]
        if options[0][0] == self.noeud_courant.reponse : #si l'option A est la bonne réponse
            if reponse == "A":
                if self.noeud_courant in self.noeuds_erreurs :
                    self.noeuds_erreurs.remove(self.noeud_courant)
                return True
            else:
                if self.noeud_courant not in self.noeuds_erreurs :
                    self.noeuds_erreurs.append(self.noeud_courant)
                return False
        else:
            if reponse == "B":
                if self.noeud_courant in self.noeuds_erreurs :
                    self.noeuds_erreurs.remove(self.noeud_courant)
                return True
            else:
                if self.noeud_courant not in self.noeuds_erreurs:
                    self.noeuds_erreurs.append(self.noeud_courant)
                return False

    def peut_jouer(self):
        "la seule limite pour continuer de jouer c'est le temps"
        if (self.difficulte)*60 > (time.time() - self.temps_depart):
            return True
        else :
            return False

    def afficher_question(self, donnees):
        print(f"\nQUESTION {self.profondeur_courante}")
        print(f"Temps restants : {(self.difficulte)*60 + self.temps_depart - time.time() }")
        print(self.noeud_courant.question)

    #provisoire
    def victoire(self):
        return "\nBravo !! vous avez gagné"


def tour_jeu(labyrinthe, question):
    labyrinthe.afficher_question(question)
    labyrinthe.chemin.append(question) # on ajoute à la PILE
    options_melangees = labyrinthe.options_possibles()
    print(f"Choix possibles: {options_melangees[0][0]} (chemin A), {options_melangees[1][0]} (chemin B)")
    saisie = input("Veuillez indiquer le chemin que vous souhaitez prendre (A ou B) : ").strip().upper()
    if labyrinthe.reponse_valide(saisie, options_melangees) :
        nouvelle_question = question.gauche
        labyrinthe.noeud_courant = nouvelle_question
        labyrinthe.profondeur_courante +=1
        return nouvelle_question
    else :
        nouvelle_question = question.droite
        labyrinthe.noeud_courant = nouvelle_question
        labyrinthe.profondeur_courante += 1
        return nouvelle_question

def cul_de_sac(labyrinthe, question):
    print("\nCUL DE SAC")
    print("Vous êtes arrivé dans un cul de sac :/")
    input("\nAppuyez sur Entrée pour pouvoir revenir au question précédente... ")
    question = question.parent
    labyrinthe.afficher_question(question)
    saisie = input("Remonter à la question précédente encore (oui/non) : ")
    while saisie == "oui" and len(labyrinthe.chemin) >= 1 :
        question = labyrinthe.chemin.pop() # il y a des piles ici aussi
        labyrinthe.noeud_courant = question
        labyrinthe.afficher_question(question)
        labyrinthe.profondeur_courante -= 1
        if labyrinthe.profondeur_courante == 1 :
            print("Vous ne pouvez pas plus remonter : vous êtes au point de départ")
            break # on sort de cul de sac
        else :
            saisie = input("Remonter à la question précédente encore (oui/non) : ")

def jeu(labyrinthe):
    question = labyrinthe.noeud_courant #racine
    while labyrinthe.peut_jouer() :
        while labyrinthe.peut_jouer() and labyrinthe.profondeur_courante != labyrinthe.arbre.profondeur_max + 1 :
            question = tour_jeu(labyrinthe, question)
        if len(labyrinthe.noeuds_erreurs) == 0 and labyrinthe.profondeur_courante == labyrinthe.arbre.profondeur_max + 1 :
            print(labyrinthe.victoire())
            break # on sort du jeu
        elif len(labyrinthe.noeuds_erreurs) != 0 and labyrinthe.peut_jouer() and labyrinthe.profondeur_courante == labyrinthe.arbre.profondeur_max + 1:
            cul_de_sac(labyrinthe, question)
        else :
            print("Défaire :( temps écoulé ")


"""    while nouvelle_question is None:
        try:
            saisie = input("Veuillez indiquer le chemin que vous souhaitez prendre (A ou B) : ").strip().upper()
            if saisie == "A":
                nouvelle_question = None
                labyrinthe.profondeur_courante += 1
                return nouvelle_question
            elif saisie == "B" :

            else:
                print(f"Ce n'est pas dans les options possibles ")
        except ValueError:
            print("Veuillez utiliser la notation du type : A, B")"""


"""    if labyrinthe.peut_jouer(): #si on est dans les temps
        if labyrinthe.arbre.profondeur_max == labyrinthe.profondeur_courante : # si on est sur les feuilles
            if labyrinthe.question == labyrinthe.arbre.solution :
                print("\nVous avez gagné !!!")
                print("Voici vos 10 millions d'euros")
            else :
                print("\nVous êtes dans un cul de sac :/ essayer d'en sortir ")

        else : #si on est dans les questions
            print(f"\nQUESTION {labyrinthe.profondeur_courante}")
    else:
        print("\nVous avez perdu :( vous avez dépassé le temps")"""


"""    def __str__(self):
        if self.peut_jouer():
            retour = "QUESTION " + self.profondeur_courante
            retour += "Temps restants : " + ((self.difficulte)*60 - time.time() - self.temps_depart)
            retour += self.noeud_courant.question
            retour += "Choix possibles: " +  + " (chemin A) " + self.options_possibles()[1] + " (chemin B)"
            return retour
        else:
            retour = "DEFAITE :("
            retour += "Vous n'avez pas trouvé la sortie à temps ..."
            return retour
"""


"""    def descente(self):
        self.profondeur_courante +=1

    def remonter(self):
        question = self.noeud_courant.parent.question
        self.profondeur_courante -=1
        return question"""



