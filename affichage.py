import pygame
import sys
import random
from questions import questions_tests, questions_geographie

# 1 les murs
# 0 le chemins
# 2 les intersections entre des chemins : où on pose la questions

laby = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
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
        question_couleur = (60, 179, 113)
        fond_couleur = (0, 0, 0)
        mur_couleur = (0, 0, 255)
        self.ecran.fill(fond_couleur)
        for i, ligne in enumerate(laby):
            for j, case in enumerate(ligne):
                rect = pygame.Rect(j * 20, i * 20, 20, 20)
                if case == 1:
                    pygame.draw.rect(self.ecran, mur_couleur, rect)
                elif case == 2:
                    question = pygame.image.load("images/question.png")
                    question = pygame.transform.scale(question, (20, 20))
                    self.ecran.blit(question, (j * 20, i * 20))
                elif case == "D" or case == "F":
                    question = pygame.image.load("images/drapeau.png")
                    question = pygame.transform.scale(question, (20, 20))
                    self.ecran.blit(question, (j * 20, i * 20))
                elif case == 5:
                    question = pygame.image.load("images/retour.png")
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


class AffichageQuestion :

    def __init__(self):
        self.longueur = len(laby[0]) * 20
        self.largeur = len(laby) * 20

    def afficher(self, surface, noeud):
        rect = pygame.Rect(0, (self.largeur // 2 - 150), self.longueur, 300)
        pygame.draw.rect(surface, (0, 0, 0), rect)
        pygame.draw.rect(surface, (0, 0, 255), rect, 20)  # Bordure

        police = pygame.font.SysFont("Consolas", 20, True)

        surf_q = police.render(noeud.question, True, (255, 255, 255))
        rect_q = surf_q.get_rect(center=(rect.centerx, rect.centery - 60))
        surface.blit(surf_q, rect_q)

        surf_a = police.render(f"A : {noeud.choixA}", True, (230, 206, 242))
        rect_a = surf_a.get_rect(center=(rect.centerx, rect.centery + 20))
        surface.blit(surf_a, rect_a)
        surf_b = police.render(f"B : {noeud.choixB}", True, (230, 206, 242))
        rect_a = surf_a.get_rect(center=(rect.centerx, rect.centery + 70))
        surface.blit(surf_b, rect_a)


# VOIR https://github.com/formazione/pygame_quiz/tree/main

class Joueur:

    def __init__(self):
        self.pacmans = []
        self.x_perso = 0
        self.y_perso = 27
        for pacman_image in ["images/pacman_droite.png", "images/pacman_gauche.png", "images/pacman_haut.png", "images/pacman_bas.png"]:
            pacman = pygame.image.load(pacman_image)
            pacman = pygame.transform.scale(pacman, (20, 20))
            self.pacmans.append(pacman)
        self.pacman = self.pacmans[0]

    def bloquer_joueur(self):
        pass

    def repondre(self):
        pass

    def afficher(self, surface):
        surface.blit(self.pacman, (self.x_perso * 20, self.y_perso * 20))




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

        self.arbre=Arbre((3,27), questions_geographie)

        self.affiche_question = False
        self.coordonnees_question = None
        self.interface = AffichageQuestion()
        self.noeud = None # où le joueur se trouve
        self.chemin = []

    def masque(self):
        masque = pygame.Surface((self.longueur, self.largeur), pygame.SRCALPHA)
        rayon = 150
        masque.fill((0, 0, 0, 255))
        centre_pacman = (self.joueur.x_perso * 20 + 10, self.joueur.y_perso * 20 + 10)
        pygame.draw.circle(masque, (0, 0, 0, 0), centre_pacman, rayon)
        self.ecran.blit(masque, (0, 0))

    def run(self):
        while self.running:
            x = self.joueur.x_perso
            y = self.joueur.y_perso
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if self.affiche_question and self.noeud is not None:
                        if event.key in [pygame.K_a,pygame.K_b]:
                            info = intersections[self.coordonnees_question]
                            if event.key == self.noeud.bonne_touche :
                                x, y = self.noeud.bon_chemin
                                reponse_correcte = True
                            else:
                                x, y = self.noeud.mauvais_chemin
                                reponse_correcte = False
                            self.joueur.x_perso, self.joueur.y_perso = x, y
                            self.chemin.append((self.noeud.coordonnees, reponse_correcte))
                            self.affiche_question = False
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

            self.carte.afficher()
            self.joueur.afficher(self.ecran)
            #self.masque()

            if self.affiche_question :
                self.interface.afficher(self.ecran, self.noeud)

            pygame.display.flip()

        pygame.quit()

game = Game()
game.run()




