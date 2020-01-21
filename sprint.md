# Objectif

Notre objectif est de déterminer si un commentaire, laissé sur un site de commande en ligne (dans notre cas Amazon), est positif (5 étoiles) ou négatif (1 étoile). Pour cela nous allons calculer la probabilité qu'il soit positif, car puisque nous ne gardons que des commenatires de 1 ou 5 étoiles, il est soit positif, soit négatif. 

- trier les données pour garder que la note et le commentaire (notes extrêmes uniquement)
- Analyser la fréquence des mots selon si les commentaires sont positifs (5 étoiles) ou négatifs (1 étoile)
- Application du théorème de Bayes pour associer chaque mot à un score de positivité
- Calculer la probabilité avec un nouveau commentaire qu'il soit positif ou négatif selon les mots utilisés



# Détail de l'organisation

## 1ère partie à finir avant le **(28 janvier)** :
Louise :
- Télécharger et ouvrir un fichier json contenant un dataset de commentaires Amazon en anglais (commentaires et avis associés à une note allant de 1 à 5 étoiles)
Supprimer les données inutiles, c'est-à-dire la date, le nom de la personne ayant écrit le commentaire, le titre du commentaire, mais également les commentaires ayant 2, 3 ou 4 étoiles. Ainsi, on ne garde que le commentaire et la note correspondante, qui est de 1 ou de 5 pour simplifier l'analyse (le commentaire est donc soit positif, soit négatif).
Commencer avec 1000 lignes (500 commentaires positifs et 500 commentaires négatifs), convertir le fichier json en csv, extraire et transformer en liste de la forme : `data_original = [("bla", True), ("bla2", False)]`

Mathis :
- Nettoyer le texte : mettre tout en minuscule, supprmier les mots de liaisons et les mots très courants qui n'ont pas d'importance dans l'analyse du texte (and, the, a, it, they etc...), supprimer la ponctuation (pre-processing: stop-words removal, lowercasing)

Jeanne :
- Rechercher les mots les plus fréquents pour ne garder que ceux qui sont présents dans plus de 20% des commentaires (Valeur du pourcentage à ajuster), et calculer leur fréquence d'apparition dans la totalité des commentaires


## 2ème partie à finir avant le **(22 février)** :
Commun :
- Associer à chaque mot son *"score de positivité"*. Pour cela nous allons calculer la probabilité que le commentaire soit positif (ComPos) sachant que le mot est présent dans le commentaire (MotInCom).
P(ComPos|MotInCom) =  P(ComPos & MotInCom)/P(MotInCom) ; sachant que  ComPos & MotInCom  =  nombre de fois où le mot est présent dans un com positif/ nombre de fois où il est est présent au total

## 3ème partieà finir avant le **(3 mai)** :
Commun :
- Pour un commentaire donné, faire une liste avec uniquement les mots qui se trouvent dans ce commentaire et qui ont été précédement analysés (Louise ou commun)
- Appliquer le théorême de Bayes, pour nous permettre de connaître la probabilité que ce commentaire soit positif ou négatif, selon le score de positivité des différents mots utilisés.


## Améliorations possibles :
Si on termine avant la date limite que l'on s'est imposé, on a pensé à plusieurs améliorations qui sont possibles :
- Calculer la fréquence d'erreurs
- Créer une interface graphique qui afficherait le commentaire, la note devinée par l'algorithme, puis la note réelle, avec un bouton permettant d'afficher un nouveau commentaire, ou evntuellement de rentrer notre propre commentaire (en anglais) et de voir s'il estime que c'est un commentaire positif ou negatif.
- Faire un jeu entre l'utilisateur et l'algorithme pour déterminer la note : le commentaire s'affiche et il faut deviner s'il est positif (note de 5 étoiles) ou négatif (note de 1 étoile)
- Améliorer le pre-processing du texte, pour par exemple reconnaître les abréviations qui sont fréquentes et qui pour l'instant ne sont pas reconnues. Cela permettrait de rendre l'analyse du texte plus précise (lowercasing + noise removal, voire normalization + stop-word removals, voire text enrichment)
