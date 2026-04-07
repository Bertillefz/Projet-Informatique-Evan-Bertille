# Analyse

## TAD : Types Abstraits de Données

### Arbres

L'**arbre** permet de modéliser le labyrinthe. Chaque intersection (noeud) correspond à une question qui mène vers deux arêtes. Ces dernières dépendent du choix fait par la joueur. Une seule branche permet de sortir du labyrinthe : c'est celle qui est associée aux bonnes réponses.

### Piles, dictionnaires et listes

Une **pile** est utilisée pour mémoriser l'historique des questions et des positions du joueur. Lorsqu'il arrive dans un cul-de-sac, on dépile pour le ramener à l'état précédent.

La **matrice** (pour la version graphique) permet de représenter les murs du labyrinthe et ses éléments. Chaque caractère représente un état.
- 0 = chemin
- 1 = mur
- 2 = question
- 5 = retour
- D = début
- F = fin

<div align="center">
  <img src="images/illustrationsMD/matriceLaby.png" alt="laby" width="50%" />
</div>

Les **dictionnaires** nous sont très utiles. Nous les utilisons pour la base de données des questions ainsi que pour lier les coordonnées du labyrinthe à la logique d'arbre de notre jeu.

<div align="center">
  <img src="images/illustrationsMD/questions.png" alt="questions" width="50%" />
</div>

Nous utilisons aussi des listes : gestion des monstres, deplacement joueur, directions, etc.

---

## POO : Programmation Orientée Objet

### Affichage graphique (`affichage.py`)

<div align="center">
  <img src="images/illustrationsMD/interactions.png" alt="laby" width="40%" />
</div>

#### Type de données : Game

- Attributs : longueur (int), largeur (int), ecran (Surface), running (bool), carte (Carte), joueur (Joueur), monstres (list), accueil (Menu), coordonnees_question (tuple), jeu_en_cours (bool), noeud (Question), chemin (list)

- Méthodes : masque(), run() (méthode principale du jeu)

#### Type de données : Joueur

- Attributs : pacmans (list), x_perso (int), y_perso (int), pacman (Surface), indice (int), vies (int), bille (BilleAttaque), attaque_monstre_enregistrement (float)

- Méthodes : afficher(surface), subir_attaque(), victoire(surface, longueur, largeur), defaite (surface, longueur, largeur)

#### Type de données : Monstre

- Attributs : points (int), x (int), y (int), en_vie (bool), directions (list), direction (tuple), enregistrement_temps (float), monstres (list), monstre (str)

- Méthodes : subir_attaque(), choix_deplacement(), deplacement(), afficher(surface)

#### Type de données : BilleAttaque

- Attributs : x (int), y (int), direction (tuple), attaque (bool), enregistrement_temps (float)

- Méthodes : lancer(surface, x_pacman, y_pacman, indice), deplacement(monstres), afficher(surface)

#### Type de données : Arbre

- Attributs : type_question (list), noeuds (dict), racine (Question)

- Méthodes : creer_arbre(coordonnees)

#### Type de données : Question

- Attributs : coordonnees (tuple), profondeur (int), bon_chemin (tuple), mauvais_chemin (tuple), choixA (str), choixB (str), bonne_touche (int), question (str), enfants (list)

- Méthodes : melange_choix(donnees_question)

#### Type de données : Menu

- Attributs : etape (int), affiche_accueil (bool)

- Méthodes : afficher_regles(surface, longueur, largeur), afficher_indications(surface, longueur, largeur), afficher(surface, longueur, largeur)

#### Type de données : Carte

- Attributs : ecran (Surface), affiche_question (bool), affiche_retour (bool)

- Méthodes : afficher(), afficher_question(surface, noeud, longueur, largeur), afficher_retour (surface, longueur, largeur)

### Affichage textuel (`labyrinthe.py`)

#### Type de données : Noeud

- Attributs : question (str), options (list), reponse (str), droite (Noeud ou None), gauche (Noeud ou None), parent (Noeud ou None)

#### Type de données : Arbre

- Attributs : type_questions (list), profondeur_max (int), racine (Noeud)

- Méthodes : creer_arbre(profondeur_actuelle : int)

#### Type de données : Labyrinthe

- Attributs : arbre (Arbre), noeud_courant (Noeud), profondeur_courante (int), temps_depart (float), difficulte (int), retour_facilite (bool), noeuds_erreurs (list), chemin (list)

- Méthodes : options_possibles():list, reponse_valide(reponse, options), peut_jouer(), afficher_question(donnees), victoire():bool 

