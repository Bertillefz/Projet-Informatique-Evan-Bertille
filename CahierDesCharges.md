# Cahier des charges

Quiz de questions : le joueur se retrouve dans un labyrinthe et doit utiliser ses connaissances pour trouver son chemin.

---

## Objectifs

Le joueur doit trouver la sortie du labyrinthe dans un temps imparti (500 secondes) tout en survivant aux attaques des monstres qui se baladent dans le labyrinthe.

---

## Règles du jeu

Le joueur se déplace dans les couloirs et rencontre des intersections.

À chaque intersection, une question s'affiche. Le joueur doit répondre par A ou B pour avancer. 

Une bonne réponse mène vers la sortie, une mauvaise mène forcèment vers un cul-de-sac.

En cas de cul-de-sac, le joueur peut utiliser une option de retour pour revenir à l'intersection précédente. 

Le joueur possède 3 vies. Entrer en contact avec un monstre fait perdre une vie.

La partie est perdue si le compteur de temps tombe à zéro ou si les 3 vies sont perdues.

---

## Personnages

Le joueur (Pacman) : 
- Se déplace (Haut, Bas, Gauche, Droite)
- répond aux questions pour avancer
- peut faire demi-tour 
- peut tirer des billes d'attaque pour se défendre

Le monstre : 
- Se déplace aléatoirement dans le labyrinthe toutes les secondes
- Il inflige des dégâts au contact

---

## Actions possibles

Se déplacer sur le labyrinthe (à l'aide des flèches du clavier : haut / bas / gauche / droite)

Répondre aux questions (à l'aide des touches du clavier A et B)

<div align="center">
  <img src="images/illustrationsMD/touchesImpasse.png" alt="touches" width="50%" />
</div>

Attaquer les monstres avec des billes (avec la barre espace)

Gérer les culs-de-sac 
- touche 1 pour rester
- touche 2 pour remonter à la question précédente

<div align="center">
  <img src="images/illustrationsMD/touchesQuestion.png" alt="touches" width="50%" />
</div>



