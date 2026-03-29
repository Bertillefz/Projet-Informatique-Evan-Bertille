import pygame
import random
from questions import questions_geographie
import time

# 1 les murs
# 0 le chemins
# 2 les intersections entre des chemins : où on pose la questions

# amelioration !!!!!!!
laby = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, "F"],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 5, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 5, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 5, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 5, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 5, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
        ["D", 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

# amelioration !!!!!!!
# coordonées x, y (colonne, ligne) (x et y commencent à 0)
intersections = {
    (3,27): {"profondeur" : 1,
             "bonne_reponse" : (4,27),
             "mauvaise_reponse" : (3,26),
             "enfants" : [(16,27), (1,4)]},
    (16,27): {"profondeur" : 2,
             "bonne_reponse" : (16,26),
             "mauvaise_reponse" : (17,27),
              "enfants" : [(38,24), (33,21)]},
    (1,4): {"profondeur" : 2,
             "bonne_reponse" : (1,3),
             "mauvaise_reponse" : (2,4),
            "enfants" : [(8,6),(22,6)]},
    (8,6): {"profondeur" : 3,
             "bonne_reponse" : (7,6),
             "mauvaise_reponse" : (8,7)},
    (22,6): {"profondeur" : 3,
             "bonne_reponse" : (23,6),
             "mauvaise_reponse" : (22,5)},
    (38,24): {"profondeur" : 3,
             "bonne_reponse" : (37,24),
             "mauvaise_reponse" : (38,23)},
    (33,21): {"profondeur" : 3,
             "bonne_reponse" : (34,21),
             "mauvaise_reponse" : (32,21)}
}


class Carte :

    def __init__(self):
        self.ecran = pygame.display.get_surface()

    def afficher(self):
        fond_couleur = (0, 0, 0)
        mur_couleur = (0, 0, 255)
        self.ecran.fill(fond_couleur)
        for i, ligne in enumerate(laby):
            for j, case in enumerate(ligne):
                rect = pygame.Rect(j * 20, i * 20, 20, 20) # amelioration !!!!!!!
                if case == 1:
                    pygame.draw.rect(self.ecran, mur_couleur, rect)
                elif case == 2:
                    question = pygame.image.load("images/icones/question.png")
                    question = pygame.transform.scale(question, (20, 20))
                    self.ecran.blit(question, (j * 20, i * 20))
                elif case == "D" or case == "F":
                    question = pygame.image.load("images/icones/drapeau.png")
                    question = pygame.transform.scale(question, (20, 20))
                    self.ecran.blit(question, (j * 20, i * 20))
                elif case == 5:
                    question = pygame.image.load("images/icones/retour.png")
                    question = pygame.transform.scale(question, (20, 20))
                    self.ecran.blit(question, (j * 20, i * 20))


class Question:
    def __init__(self, coordonnees, donnees_intersection, donnee_question):
        self.coordonnees = coordonnees
        self.profondeur = donnees_intersection["profondeur"]
        self.bon_chemin = donnees_intersection["bonne_reponse"]
        self.mauvais_chemin = donnees_intersection["mauvaise_reponse"]
        self.choixA = None
        self.choixB = None
        self.bonne_touche = None
        self.question = donnee_question["question"]
        self.enfants = []

    def melange_choix(self, donnees_question):
        choix = [donnees_question["options"][0], donnees_question["options"][1]]
        random.shuffle(choix)
        self.choixA = choix[0]
        self.choixB = choix[1]
        if self.choixA == donnees_question["reponse"]:
            self.bonne_touche = pygame.K_a
        else:
            self.bonne_touche = pygame.K_b

class Arbre:
    def __init__(self, coordonnee_racine, type_question):
        self.type_question = type_question.copy()
        self.noeuds = {}
        self.racine = self.creer_arbre(coordonnee_racine)


    def creer_arbre(self, coordonnee):
        if coordonnee not in intersections :
            return None

        donnees_question = random.choice(self.type_question)
        self.type_question = [d for d in self.type_question if d != donnees_question]
        noeud = Question(coordonnee, intersections[coordonnee], donnees_question)

        noeud.melange_choix(donnees_question)
        self.noeuds[coordonnee] = noeud

        if "enfants" in intersections[coordonnee]:
            for coordonnee_enfant in intersections[coordonnee]["enfants"]:
                enfant = self.creer_arbre(coordonnee_enfant)
                noeud.enfants.append(enfant)
        return noeud


#les affichages des messages

def afficher_question(surface, noeud, longueur, largeur):
    rect = pygame.Rect(0, (largeur // 2 - 150), longueur, 300)
    pygame.draw.rect(surface, (0, 0, 0), rect)
    pygame.draw.rect(surface, (0, 0, 255), rect, 20)

    police = pygame.font.SysFont("Consolas", 18, True)

    surf_q = police.render(noeud.question, True, (255, 255, 255))
    rect_q = surf_q.get_rect(center=(rect.centerx, rect.centery - 60))
    surface.blit(surf_q, rect_q)

    surf_a = police.render(f"A : {noeud.choixA}", True, (230, 206, 242))
    rect_a = surf_a.get_rect(center=(rect.centerx, rect.centery + 20))
    surface.blit(surf_a, rect_a)
    surf_b = police.render(f"B : {noeud.choixB}", True, (230, 206, 242))
    rect_a = surf_a.get_rect(center=(rect.centerx, rect.centery + 70))
    surface.blit(surf_b, rect_a)


def afficher_retour(surface, longueur,largeur):
    rect = pygame.Rect(0, (largeur // 2 - 100), longueur, 200)
    pygame.draw.rect(surface, (0, 0, 0), rect)
    pygame.draw.rect(surface, (255, 0, 0), rect, 20)

    police = pygame.font.SysFont("Consolas", 18, True)
    surface_annonce = police.render("Oups cul-de-sac : vous êtes de retour à la dernière intersection", True, (255, 255, 255))
    rect_annonce = surface_annonce.get_rect(center=(rect.centerx, rect.centery - 40))
    surface.blit(surface_annonce, rect_annonce)

    surface_question_1 = police.render("Souhaites-tu y rester (1)", True, (230, 206, 242))
    rect_question_1 = surface_question_1.get_rect(center=(rect.centerx, rect.centery + 20))
    surface.blit(surface_question_1, rect_question_1)

    surface_question_2 = police.render("ou remonter encore à la question précédente (2) ?", True, (230, 206, 242))
    rect_question_2 = surface_question_2.get_rect(center=(rect.centerx, rect.centery + 40))
    surface.blit(surface_question_2, rect_question_2)

def afficher_regles(surface, longueur, largeur):
    surface.fill((0, 0, 0))
    regles = pygame.image.load("images/regles.png")
    regles = pygame.transform.scale(regles, (min(longueur, largeur), min(longueur, largeur)))
    surface.blit(regles, (longueur // 2 - min(longueur, largeur) // 2, largeur // 2 - min(longueur, largeur) // 2))


class Monstre:

    def __init__(self):
        self.points = 3000

    def attaque(self):
        #s'il recoit des billes : -500 de points pour lui
        pass

    def deplacement(self):
        pass

# VOIR https://github.com/formazione/pygame_quiz/tree/main

class Joueur:

    def __init__(self):
        self.pacmans = []
        self.x_perso = 0
        self.y_perso = 27
        for pacman_image in ["images/pacmans/pacman_droite.png", "images/pacmans/pacman_gauche.png", "images/pacmans/pacman_haut.png", "images/pacmans/pacman_bas.png"]:
            pacman = pygame.image.load(pacman_image)
            pacman = pygame.transform.scale(pacman, (20, 20))
            self.pacmans.append(pacman)
        self.pacman = self.pacmans[0]
        self.vies = 3

    def afficher(self, surface):
        surface.blit(self.pacman, (self.x_perso * 20, self.y_perso * 20))

    def victoire(self, surface, longueur, largeur):
        surface.fill((0,0,0))
        victoire = pygame.image.load("images/victoire.png")
        victoire = pygame.transform.scale(victoire, (min(longueur, largeur), min(longueur, largeur)))
        surface.blit(victoire, (longueur // 2 - min(longueur, largeur) // 2, largeur // 2 - min(longueur, largeur) // 2))

    def defaite(self, surface, longueur, largeur):
        surface.fill((0,0,0))
        defaite = pygame.image.load("images/defaite.png")
        defaite = pygame.transform.scale(defaite, (min(longueur,largeur), min(longueur,largeur)))
        surface.blit(defaite, (longueur // 2 - min(longueur, largeur) // 2, largeur // 2 - min(longueur, largeur) // 2))

    def attaque(self):
        # si collision avec monstres : perd 1 vie
        # si perd ses 3 vies : defaite
        pass




class Game:
    def __init__(self):
        pygame.init()
        self.longueur = len(laby[0]) * 20
        self.largeur = len(laby) * 20
        self.ecran = pygame.display.set_mode((self.longueur, self.largeur))
        pygame.display.set_caption("Labyrinthe")

        self.carte = Carte()
        self.joueur = Joueur()
        self.running = True

        self.arbre=Arbre((3,27), questions_geographie) # amelioration !!!!!!!
        self.temps_debut = time.time()

        self.affiche_question = False
        self.affiche_retour = False
        self.affiche_acceuil = True
        self.coordonnees_question = None
        self.jeu_en_cours = True
        self.noeud = None # où le joueur se trouve
        self.chemin = []

    def masque(self):
        masque = pygame.Surface((self.longueur, self.largeur), pygame.SRCALPHA)
        rayon = 100
        masque.fill((0, 0, 0, 255))
        centre_pacman = (self.joueur.x_perso * 20 + 10, self.joueur.y_perso * 20 + 10)
        pygame.draw.circle(masque, (0, 0, 0, 0), centre_pacman, rayon)
        self.ecran.blit(masque, (0, 0))

    def run(self):
        while self.running:
            if self.affiche_acceuil :
                afficher_regles(self.ecran, self.longueur, self.largeur)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_RETURN:
                            self.affiche_acceuil = False
                            self.temps_debut = time.time()
                continue

            if (60 + self.temps_debut - time.time()) < 0:
                self.jeu_en_cours = False
                self.joueur.defaite(self.ecran, self.longueur, self.largeur)

            x = self.joueur.x_perso
            y = self.joueur.y_perso
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    # les questions
                    if self.affiche_question and self.noeud is not None:
                        if event.key in [pygame.K_a,pygame.K_b]:
                            if event.key == self.noeud.bonne_touche :
                                x, y = self.noeud.bon_chemin
                                reponse_correcte = True
                            else:
                                x, y = self.noeud.mauvais_chemin
                                reponse_correcte = False
                            self.joueur.x_perso, self.joueur.y_perso = x, y
                            self.chemin.append((self.noeud.coordonnees, reponse_correcte))
                            self.affiche_question = False
                    # le retour : on tape soit 1 soit 2
                    elif self.affiche_retour :
                        if event.key in [pygame.K_1, pygame.K_KP1]:
                            self.affiche_retour = False
                            self.affiche_question = True
                        elif event.key in [pygame.K_2, pygame.K_KP2] :
                            if len(self.chemin) > 0:
                                derniere_coordonnee, reponse = self.chemin.pop()
                                self.joueur.x_perso, self.joueur.y_perso = derniere_coordonnee
                                self.coordonnees_question = derniere_coordonnee
                                self.noeud = self.arbre.noeuds[derniere_coordonnee]
                            else :
                                self.affiche_retour = False
                                self.affiche_question = True
                    else :
                        if event.key == pygame.K_DOWN:
                            y += 1
                            self.joueur.pacman = self.joueur.pacmans[3]
                        if event.key == pygame.K_UP:
                            y -= 1
                            self.joueur.pacman = self.joueur.pacmans[2]
                        if event.key == pygame.K_LEFT:
                            x -= 1
                            self.joueur.pacman = self.joueur.pacmans[1]
                        if event.key == pygame.K_RIGHT:
                            x += 1
                            self.joueur.pacman = self.joueur.pacmans[0]
                        if 0 <= y < self.largeur and 0 <= x < self.longueur :
                            if laby[y][x] != 1:
                                self.joueur.x_perso, self.joueur.y_perso = x, y
                            if laby[y][x] == 2:
                                self.coordonnees_question = (x,y)
                                self.noeud = self.arbre.noeuds[(x,y)]
                                self.affiche_question = True
                            elif laby[y][x] == 5 :
                                derniere_coordonnee, reponse = self.chemin.pop()
                                self.joueur.x_perso, self.joueur.y_perso = derniere_coordonnee
                                self.coordonnees_question = derniere_coordonnee
                                self.noeud = self.arbre.noeuds[derniere_coordonnee]
                                self.affiche_retour = True
                            elif laby[y][x] == "F":
                                self.jeu_en_cours = False
                                self.joueur.victoire(self.ecran, self.longueur, self.largeur)

            if self.jeu_en_cours :
                self.carte.afficher()
                self.joueur.afficher(self.ecran)
                self.masque()
                #afficher les monstres au dessus du masque

                if self.affiche_question :
                    afficher_question(self.ecran, self.noeud, self.longueur, self.largeur)
                if self.affiche_retour :
                    afficher_retour(self.ecran, self.longueur, self.largeur)

            pygame.display.flip()

        pygame.quit()

game = Game()
game.run()




