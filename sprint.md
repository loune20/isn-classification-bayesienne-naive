# Objectif

Notre objectif est de déterminer si un commentaire, laissé sur un site de commande en ligne (dans notre cas Amazon), est positif (5 étoiles) ou négatif (1 étoile). Pour cela nous allons calculer la probabilité qu'il soit positif uniquement. En effet, puisque nous ne gardons que des commentaires de 1 ou 5 étoiles, nous pouvons considérer que si le probabilité que le commentaire soit positif vaut P, alors la probabilité que le commentaire soit négatif vaut 1-P. Il s'agit d'une approximation mais considérant l'objectif (déterminer si le commentaire est positif) nous devrions atteindre des résultats satisfaisants.

Nous avons réparti le projet en 3 étapes principales : 
 - un ensemble de petites tâches de début de projet (tri, preprocessing du texte, tri de nouveau)
 - création d'un algorithme associant à chaque mot un score de positivité (partie machine learning)
 - application du théorême de Bayes pour associer à chaque commentaire la probabilité qu'il soit positif


# Détail de l'organisation

## 1ère partie : tri divers (*28 janvier*)
Cette partie est en fait divisée en trois sous-partie indépendantes que nous avons pu répartir entre nous : 

Louise :
- Télécharger et ouvrir un fichier json contenant un dataset de commentaires Amazon en anglais (commentaires et avis associés à une note allant de 1 à 5 étoiles) que l'on peut trouver sur internet.
- Supprimer les données inutiles, c'est-à-dire la date, le nom de la personne ayant écrit le commentaire, le titre du commentaire, mais également les commentaires ayant 2, 3 ou 4 étoiles. Ainsi, on ne garde que le commentaire et la note correspondante, qui est de 1 ou de 5 pour simplifier l'analyse (le commentaire est donc soit positif, soit négatif).
- Commencer avec 1000 lignes (500 commentaires positifs et 500 commentaires négatifs), convertir le fichier json en csv, extraire et transformer en liste (contenant des tuple ou bien des listes, avec le commentaire et la note : True si note de 5 et False si note de 1).

Mathis :
- Traitement des données pour nettoyer le texte (data pre-processing) : mettre tout en minuscule (lowercasing), supprmier les mots vides, c'est-à-dire les mots de liaisons et les mots très courants qui n'ont pas d'importance dans l'analyse du texte, notamment and, the, a, it, they, this etc... (stop-words removal) et supprimer la ponctuation (simple anomalies noise removal).

Jeanne :
- Rechercher les mots les plus fréquents pour ne garder que ceux qui sont présents dans plus de 30% des commentaires (valeur du pourcentage à ajuster), et calculer leur fréquence d'apparition dans la totalité des commentaires. Les enregistrer dans une liste avec le mot associé à sa fréquence d'apparition.


Les entrées et sorties de chaques fonctions/programmes sont établies comme suit : 
 - Louise : fichier CSV pré-traité à la main en entrée, liste de type  `data_original = [("comm1", True), ("comm2", False), ("comm3", False)]` où True signifie un commentaire positif (5 étoiles) et False un commentaire négatif (1 étoile)
 - Mathis : liste du même type que `data_original` (voire plus haut), sortie identique
 - Jeanne : liste du même type que `data_original`, sortie une autre liste de type : `freq_words = [(word1, freq_word1), (word2, freq_word2), (word3, freq_word3)]` où freq_word est un float compris entre 0 et 1 **a verifier par Jeanne**


## 2ème partie : score de positivté (*22 février*)
Commun :
Associer à chaque mot son "score de positivité"*. Pour cela nous allons calculer la probabilité que le commentaire soit positif (ComPos) sachant que le mot est présent dans le commentaire (InCom) :
P(ComPos|InCom) = P(ComPos & InCom)/P(InCom)
Sachant que P(ComPos & InCom) = nombre de fois où le mot est présent dans les commentaires positifs / nombre de fois où il est est présent au total dans tous les commentaires **formater** et **ajouter format donné attendu**

## 3ème partie: Bayes (*3 mai*)
Commun :
- Pour un commentaire donné, faire une liste avec uniquement les mots qui se trouvent dans ce commentaire et qui ont été précédement analysés (Louise ou commun)
- Appliquer le théorême de Bayes, pour nous permettre de connaître la probabilité que ce commentaire soit positif ou négatif, selon le score de positivité des différents mots utilisés. **a detailler**


## Améliorations possibles :
Si on termine avant la date limite que l'on s'est imposé, on a plusieurs améliorations sont possibles :
- Calculer la fréquence d'erreurs
- Créer une interface graphique qui afficherait le commentaire, la note devinée par l'algorithme, puis la note réelle, avec un bouton permettant d'afficher un nouveau commentaire, ou evntuellement de rentrer notre propre commentaire (en anglais) et de voir s'il estime que c'est un commentaire positif ou negatif.
- Faire un jeu entre l'utilisateur et l'algorithme pour déterminer la note : le commentaire s'affiche et il faut deviner s'il est positif (note de 5 étoiles) ou négatif (note de 1 étoile)
- Améliorer le pre-processing du texte, pour par exemple reconnaître les abréviations qui sont fréquentes et qui pour l'instant ne sont pas reconnues. Cela permettrait de rendre l'analyse du texte plus précise (normalization, voire text enrichment)
