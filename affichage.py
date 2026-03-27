import pygame
import sys

from questions import questions_tests, questions_geographie

# 1 les murs
# 0 le chemins
# 2 les intersections entre des chemins : où on pose la questions


laby = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

# coordonées x, y (colonne, ligne)
intersections = {
    (4,28): {"profondeur" : 1,
             "bonne_reponse" : (5,28),
             "mauvaise_reponse" : (4,27)},
    (17,28): {"profondeur" : 2,
             "bonne_reponse" : (17,27),
             "mauvaise_reponse" : (18,28)},
    (2,5): {"profondeur" : 2,
             "bonne_reponse" : (2,4),
             "mauvaise_reponse" : (3,5)},
    (9,7): {"profondeur" : 3,
             "bonne_reponse" : (8,7),
             "mauvaise_reponse" : (9,8)},
    (23,7): {"profondeur" : 3,
             "bonne_reponse" : (24,7),
             "mauvaise_reponse" : (23,6)},
    (39,25): {"profondeur" : 3,
             "bonne_reponse" : (38,25),
             "mauvaise_reponse" : (39,24)},
    (34,22): {"profondeur" : 3,
             "bonne_reponse" : (35,22),
             "mauvaise_reponse" : (33,22)}
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

import random
import questions
from labyrinthe import Arbre, Noeud, Labyrinthe

# VOIR https://github.com/formazione/pygame_quiz/tree/main

class Question:

    def __init__(self):
        self.longueur = len(laby[0]) * 20
        self.largeur = len(laby) * 20
        #self.coord = x, y
        #self.coord_bon = x_bonne_rep, y_bonne_rep
        #self.coord_mauvais = x_mauvaise, y_mauvaise
        #super().__init__(donnees_question)

    def afficher(self, surface):
        rect = pygame.Rect((self.longueur//2 - (self.longueur - 100)//2), (self.largeur//2 - (self.largeur - 100)//2), self.longueur - 100, self.largeur - 100)
        pygame.draw.rect(surface, (0, 0, 0), rect)



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
        self.question = Question()

    def masque(self):
        masque = pygame.Surface((self.longueur, self.largeur), pygame.SRCALPHA)
        rayon = 150
        masque.fill((0, 0, 0, 255))
        centre_pacman = (self.joueur.x_perso * 20 + 10, self.joueur.y_perso * 20 + 10)
        pygame.draw.circle(masque, (0, 0, 0, 0), centre_pacman, rayon)
        self.ecran.blit(masque, (0, 0))


    def run(self):
        afficher_question = False
        while self.running:
            x = self.joueur.x_perso
            y = self.joueur.y_perso
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
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
                            afficher_question = True


            self.carte.afficher()
            self.joueur.afficher(self.ecran)
            #self.masque()

            if afficher_question :
                self.question.afficher(self.ecran)

            pygame.display.flip()

        pygame.quit()

game = Game()
#game.run()



