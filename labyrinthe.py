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
    def __init__(self, difficulte,retour_facilite, donnees, profondeur_max):
        self.arbre = Arbre(donnees, profondeur_max)
        self.noeud_courant = self.arbre.racine
        self.profondeur_courante = 1
        self.temps_depart = time.time()
        self.difficulte = difficulte
        self.retour_facilite = retour_facilite # vrai ou faux
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
        temps = int((self.difficulte)*60 + self.temps_depart - time.time())
        minutes = temps // 60
        secondes = temps % 60
        print(f"\nQUESTION {self.profondeur_courante}")
        print(f"Temps restants : {minutes} min {secondes} sec")
        print(self.noeud_courant.question)

    def victoire(self):
        return "\nBravo !! vous avez gagné"


