# Analyse

## TAD : Types Abstraits de Données

### Arbres

L'**arbre** permet de modéliser le labyrinthe. Chaque intersection (noeud) correspond à une question qui mène vers deux arretes. Ces dernières dépendent du choix fait pas la joueur. Une seule branche permet de sortir du labyrinthe : c'est celle qui est associé aux bonnes réponses.

### Piles, dictionnaires et listes

Une **pile** est utilisée pour mémoriser l'historique des questions et des positions du joueur. Lorsqu'il arrive dans un cul-de-sac, on dépile (pop) pour le ramener à l'état précédent.

La **matrice** permet de réprésenter les murs du labyrinthe et ses éléments. Chaque entier représente un état.
- 0 = chemin
- 1 = mur
- 2 = question
- 5 = retour
- D = début
- F = fin

<div align="center">
  <img src="images/illustrationsMD/matriceLaby.png" alt="laby" width="50%" />
</div>

Les **dictionnaires** nous sont très utiles. Nous les utilisions pour la base de données des questions ainsi que pour lier les coordonnées du labyrinthe à la logique d'arbre de notre jeu.

<div align="center">
  <img src="images/illustrationsMD/questions.png" alt="questions" width="50%" />
</div>

Nous utilisons aussi des listes.

---

## POO : Progammation Orientée Objet

### Type de données : Game

- Attributs : 

- Méthodes :

### Type de données : Joueur

- Attributs : 

- Méthodes :

### Type de données : Monstre

- Attributs : 

- Méthodes :

### Type de données : BilleAttaque

- Attributs : 

- Méthodes :

### Type de données : Arbre

- Attributs : 

- Méthodes :

### Type de données : Question

- Attributs : 

- Méthodes :

### Type de données : Carte

- Attributs : 

- Méthodes :