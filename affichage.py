import pygame
import random
from questions import questions_geographie
import time

# 1 les murs
# 0 le chemins
# 2 les intersections entre des chemins : où on pose la questions
# 5 les culs-de-sac
# D la case de début
# F la case de fin

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

'Carte : pour dessiner le labyrinthe avec les petits icones à l interieur'
class Carte :

    def __init__(self):
        self.ecran = pygame.display.get_surface()
        self.affiche_question = False
        self.affiche_retour = False

    # affichage du labyrinthe en lui-meme
    def afficher(self):
        fond_couleur = (0, 0, 0)
        mur_couleur = (0, 0, 255)
        self.ecran.fill(fond_couleur)
        for i, ligne in enumerate(laby):
            for j, case in enumerate(ligne):
                rect = pygame.Rect(j * 20, i * 20, 20, 20)
                if case == 1:
                    pygame.draw.rect(self.ecran, mur_couleur, rect)
                elif case == 2:
                    image = pygame.image.load("images/icones/question.png")
                    question = pygame.transform.scale(image, (20, 20))
                    self.ecran.blit(question, (j * 20, i * 20))
                elif case == "D" or case == "F":
                    image = pygame.image.load("images/icones/drapeau.png")
                    drapeau = pygame.transform.scale(image, (20, 20))
                    self.ecran.blit(drapeau, (j * 20, i * 20))
                elif case == 5:
                    image = pygame.image.load("images/icones/retour.png")
                    retour = pygame.transform.scale(image, (20, 20))
                    self.ecran.blit(retour, (j * 20, i * 20))

    # affichage message : questions avec les deux possibilitées
    def afficher_question(self, surface, noeud, longueur, largeur):
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

    # affichage retour : retour avec les deux options
    def afficher_retour(self, surface, longueur, largeur):
        rect = pygame.Rect(0, (largeur // 2 - 100), longueur, 200)
        pygame.draw.rect(surface, (0, 0, 0), rect)
        pygame.draw.rect(surface, (255, 0, 0), rect, 20)

        police = pygame.font.SysFont("Consolas", 18, True)
        surface_annonce = police.render("Oups cul-de-sac : vous êtes de retour à la dernière intersection", True,(255, 255, 255))
        rect_annonce = surface_annonce.get_rect(center=(rect.centerx, rect.centery - 40))
        surface.blit(surface_annonce, rect_annonce)

        surface_question_1 = police.render("Souhaites-tu y rester (1)", True, (230, 206, 242))
        rect_question_1 = surface_question_1.get_rect(center=(rect.centerx, rect.centery + 20))
        surface.blit(surface_question_1, rect_question_1)

        surface_question_2 = police.render("ou remonter encore à la question précédente (2) ?", True, (230, 206, 242))
        rect_question_2 = surface_question_2.get_rect(center=(rect.centerx, rect.centery + 40))
        surface.blit(surface_question_2, rect_question_2)


'Question : permet de mélanger les réponses possibles'
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


'Arbre : construit l arbre des questions avec les coordonnées associées à la question'
class Arbre:
    def __init__(self, coordonnee_racine, type_question):
        self.type_question = type_question.copy()
        self.noeuds = {}
        self.racine = self.creer_arbre(coordonnee_racine)


    def creer_arbre(self, coordonnee):
        if coordonnee not in intersections : #fin du parcours
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


class Menu :

    def __init__(self):
        self.etape = 1
        self.affiche_acceuil = True

    #etape 1 de l'accueil
    def afficher_regles(self, surface, longueur, largeur):
        surface.fill((0, 0, 0))
        regles = pygame.image.load("images/regles.png")
        regles = pygame.transform.scale(regles, (min(longueur, largeur), min(longueur, largeur)))
        surface.blit(regles, (longueur // 2 - min(longueur, largeur) // 2, largeur // 2 - min(longueur, largeur) // 2))

    # etape 2 de l'accueil
    def afficher_indications(self, surface, longueur, largeur):
        surface.fill((0, 0, 0))
        image = pygame.image.load("images/indications.png")
        ind = pygame.transform.scale(image, (min(longueur, largeur), min(longueur, largeur)))
        surface.blit(ind, (longueur // 2 - min(longueur, largeur) // 2, largeur // 2 - min(longueur, largeur) // 2))

    #méthode principale
    def afficher(self, surface, longueur, largeur):
        if self.etape == 1 :
            self.afficher_regles(surface, longueur, largeur)
        elif self.etape ==2 :
            self.afficher_indications(surface, longueur, largeur)


'Monstre : se déplace automatiquement et fait subir des dégats au joueur '
class Monstre:

    def __init__(self):
        self.points = 2000 # monstre meurt au bout de 4 tirs

        coordonnees_possibles = [(10, 11), (16,11), (36,15)]
        coordonnees=random.choice(coordonnees_possibles)
        self.x = coordonnees[0]
        self.y = coordonnees[1]

        self.en_vie = True
        # en haut / bas / droite / gauche
        self.directions = [ (0, -1), (0, 1), (1,0), (-1,0)]
        self.direction = random.choice(self.directions)
        self.enregistrement_temps = time.time()
        self.monstres = ["images/monstres/monstre_rouge_droite.png", "images/monstres/monstre_rose_gauche.png", "images/monstres/monstre_turquoise_droite.png"]
        self.monstre = random.choice(self.monstres)

    def subir_attaque(self):
        self.points -= 500
        if self.points <=0:
            self.en_vie = False

    # choix de la direction aléatoire à prendre parmi les possibilités
    def choix_deplacement(self):
        directions_possibles = []
        for x, y in self.directions :
            if laby[self.y + y ][self.x + x] != 1 :
                if 0 <= self.x + x < len(laby[0]) and 0 <= self.y + y < len(laby) :
                    directions_possibles.append((x,y))
        self.direction = random.choice(directions_possibles)

    # fonction de déplacement principale du monstre
    def deplacement(self):
        temps = time.time()
        if temps - self.enregistrement_temps > 1: #intervalle de 1 seconde
            # s'il n'y a pas de mur il continue d'avancer dans la meme direction
            if laby[self.y + self.direction[1]][self.x + self.direction[0]] !=1:
                if 0 <= self.y + self.direction[1] < len(laby) and 0 <= self.x + self.direction[0] < len(laby[0]):
                    self.y += self.direction[1]
                    self.x += self.direction[0]
            else : # sinon il prend une autre direction
                self.choix_deplacement()
                if 0 <= self.y + self.direction[1] < len(laby) and 0 <= self.x + self.direction[0] < len(laby[0]) :
                    if laby[self.y + self.direction[1]][self.x + self.direction[0]] != 1:
                        self.y += self.direction[1]
                        self.x += self.direction[0]
            self.enregistrement_temps = time.time()

    def afficher(self, surface):
        if self.en_vie :
            monstre = pygame.image.load(self.monstre)
            monstre = pygame.transform.scale(monstre, (20, 20))
            surface.blit(monstre, (self.x * 20, self.y * 20))
            self.deplacement()

'Bille Attaque : arme du joueur et fait subir des dégats au monstre'
class BilleAttaque:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0,0
        self.attaque = False
        self.enregistrement_temps = time.time()

    # lancer de bille : direction selon l'orientation du pacman (donc de son indice)
    def lancer(self, surface, x_pacman, y_pacman, indice):
        self.x = x_pacman
        self.y = y_pacman
        if not self.attaque:
            if indice == 0:
                self.direction = 1, 0
            elif indice == 1:
                self.direction = -1, 0
            elif indice == 2:
                self.direction = 0, -1
            elif indice == 3:
                self.direction = 0, 1
            self.attaque = True
            self.enregistrement_temps = time.time()

    # mouvement de la bille : suite de la méthode lancer
    def deplacement(self, monstres):
        if self.attaque :
            temps = time.time()
            if temps - self.enregistrement_temps > 0.1 : # bille se déplace toutes les 0.1 sec
                if laby[self.y + self.direction[1]][self.x + self.direction[0]] == 1 :
                    self.attaque = False # s'il y a un mur : il y a plus de bille
                else:
                    self.y += self.direction[1]
                    self.x += self.direction[0]
                for monstre in monstres :
                    if monstre.en_vie :
                        if self.x == monstre.x and self.y == monstre.y:
                            monstre.subir_attaque()
                            self.attaque = False
                self.enregistrement_temps = time.time()


    def afficher(self, surface):
        if self.attaque :
            bille = pygame.image.load("images/bille_attaque.png")
            bille = pygame.transform.scale(bille, (20, 20))
            surface.blit(bille, (self.x * 20, self.y * 20))

'Joueur (pacman) : se déplace dans le labyrinthe'
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
        self.indice = 0 # position vers la droite
        self.vies = 1
        self.bille = BilleAttaque()
        self.attaque_monstre_enregistrement = 0

    def afficher(self, surface):
        surface.blit(self.pacman, (self.x_perso * 20, self.y_perso * 20))
        self.bille.afficher(surface)

    def subir_attaque(self):
        temps = time.time()
        if temps - self.attaque_monstre_enregistrement > 2 :
            self.vies -=1
            self.attaque_monstre_enregistrement = temps

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

'Jeu : gère les touches, et tous les affichages'
class Game:
    def __init__(self):
        pygame.init()
        self.longueur = len(laby[0]) * 20
        self.largeur = len(laby) * 20
        self.ecran = pygame.display.set_mode((self.longueur, self.largeur))
        pygame.display.set_caption("Labyrinthe")
        self.running = True

        self.carte = Carte()
        self.joueur = Joueur()
        self.monstres = [Monstre(), Monstre(), Monstre()]

        self.arbre=Arbre((3,27), questions_geographie)
        self.temps_debut = time.time()

        self.accueil = Menu()
        self.coordonnees_question = None
        self.jeu_en_cours = True
        self.noeud = None
        self.chemin = []

    # masque : on fait un trou dans un écran noir pour voir le personnage
    def masque(self):
        masque = pygame.Surface((self.longueur, self.largeur), pygame.SRCALPHA)
        rayon = 100
        masque.fill((0, 0, 0, 255))
        centre_pacman = (self.joueur.x_perso * 20 + 10, self.joueur.y_perso * 20 + 10)
        pygame.draw.circle(masque, (0, 0, 0, 0), centre_pacman, rayon)
        self.ecran.blit(masque, (0, 0))

    def run(self):
        while self.running:

            'Gestion du temps'
            if (120 + self.temps_debut - time.time()) < 0:
                self.jeu_en_cours = False
                self.joueur.defaite(self.ecran, self.longueur, self.largeur)

            'Les actions sur le clavier'

            x = self.joueur.x_perso
            y = self.joueur.y_perso
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    # les questions
                    if self.carte.affiche_question and self.noeud is not None:
                        if event.key in [pygame.K_a,pygame.K_b]:
                            if event.key == self.noeud.bonne_touche :
                                x, y = self.noeud.bon_chemin
                                reponse_correcte = True
                            else:
                                x, y = self.noeud.mauvais_chemin
                                reponse_correcte = False
                            self.joueur.x_perso, self.joueur.y_perso = x, y
                            self.chemin.append((self.noeud.coordonnees, reponse_correcte))
                            self.carte.affiche_question = False
                    # le retour : on tape soit 1 soit 2
                    elif self.carte.affiche_retour :
                        if event.key in [pygame.K_1, pygame.K_KP1]:
                            self.carte.affiche_retour = False
                            self.carte.affiche_question = True
                        elif event.key in [pygame.K_2, pygame.K_KP2] :
                            if len(self.chemin) > 0:
                                derniere_coordonnee, reponse = self.chemin.pop()
                                self.joueur.x_perso, self.joueur.y_perso = derniere_coordonnee
                                self.coordonnees_question = derniere_coordonnee
                                self.noeud = self.arbre.noeuds[derniere_coordonnee]
                            else :
                                self.carte.affiche_retour = False
                                self.carte.affiche_question = True
                    # déplacement : en bas en haut à gauche à droite
                    else :
                        if event.key == pygame.K_DOWN:
                            y += 1
                            self.joueur.indice = 3
                            self.joueur.pacman = self.joueur.pacmans[3]
                        if event.key == pygame.K_UP:
                            y -= 1
                            self.joueur.indice =2
                            self.joueur.pacman = self.joueur.pacmans[2]
                        if event.key == pygame.K_LEFT:
                            x -= 1
                            self.joueur.indice = 1
                            self.joueur.pacman = self.joueur.pacmans[1]
                        if event.key == pygame.K_RIGHT:
                            x += 1
                            self.joueur.indice = 0
                            self.joueur.pacman = self.joueur.pacmans[0]

                        if event.key == pygame.K_SPACE: # attaque
                            self.joueur.bille.lancer(self.ecran, self.joueur.x_perso, self.joueur.y_perso, self.joueur.indice)

                        if 0 <= y < self.largeur and 0 <= x < self.longueur :
                            if laby[y][x] != 1: # pas un mur
                                self.joueur.x_perso, self.joueur.y_perso = x, y
                            if laby[y][x] == 2: # une question
                                self.coordonnees_question = (x,y)
                                self.noeud = self.arbre.noeuds[(x,y)]
                                self.carte.affiche_question = True
                            elif laby[y][x] == 5 : # un cul de sac
                                derniere_coordonnee, reponse = self.chemin.pop()
                                self.joueur.x_perso, self.joueur.y_perso = derniere_coordonnee
                                self.coordonnees_question = derniere_coordonnee
                                self.noeud = self.arbre.noeuds[derniere_coordonnee]
                                self.carte.affiche_retour = True
                            elif laby[y][x] == "F": # la fin
                                self.jeu_en_cours = False
                                self.joueur.victoire(self.ecran, self.longueur, self.largeur)

            'Affichage'

            # affichage accueil
            if self.accueil.affiche_acceuil:
                self.accueil.afficher(self.ecran, self.longueur, self.largeur)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if self.accueil.etape == 1:
                                self.accueil.etape = 2
                            else:
                                self.accueil.affiche_acceuil = False
                                self.temps_debut = time.time()
                continue

            #affichage jeu
            if self.jeu_en_cours :
                self.carte.afficher()
                self.joueur.afficher(self.ecran)
                self.masque()
                self.joueur.bille.deplacement(self.monstres)

                for monstre in self.monstres :
                    monstre.afficher(self.ecran)

                for monstre in self.monstres :
                    if monstre.en_vie :
                        if self.joueur.x_perso == monstre.x and self.joueur.y_perso ==monstre.y :
                            self.joueur.subir_attaque()
                if self.joueur.vies <=0 :
                    self.jeu_en_cours = False
                    self.joueur.defaite(self.ecran, self.longueur, self.largeur)

                #affichage des messages : question et retour
                if self.carte.affiche_question :
                    self.carte.afficher_question(self.ecran, self.noeud, self.longueur, self.largeur)
                if self.carte.affiche_retour :
                    self.carte.afficher_retour(self.ecran, self.longueur, self.largeur)

                #affichage du temps
                temps = int(120 + self.temps_debut - time.time())
                police = pygame.font.SysFont("Consolas", 18, True)
                chronometre = police.render(f"{temps} s", True, (255,255,255))
                self.ecran.blit(chronometre, (10,10))

            pygame.display.flip()

        pygame.quit()

game = Game()
game.run()




