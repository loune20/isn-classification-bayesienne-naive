# To-do
- [X] Renommer fonction Jeanne
- [X] Voir ensemble convention de nommage
- [X] Détailler la partie application de Bayes (ou pas ?)
- [ ] Sprint 2 (correction du 1) (je crois que c'est bon ça nan Jeanne ?)
- [X] Code pour liste de tous les mots 
- [ ] Mettre en commun et fignoler la partie 1
POUR LA SEMAINE PRO : partie "score de positivité" pour Jeanne et Mathis à faire pour le 11 février


# Score de positivité (22 février)

## Mathis : fréquence d'appparition du mot dans les commentaires positifs
- [ ] Calculer fréquence apparition des mots de la liste `freq_word` dans les com positifs
- [ ] Associer chaque mot à cette fréquence
- [ ] Si elle est comprise entre 0.45 et 0.55 (ajuster) on supprime le mot de la liste

### Format
- entrée : dictionnaire `freq_word`
- sortie : dictionnaire `freq_word_in_pos = {"word1": freq_word1_in_pos, "word2": freq_word2_in_pos}` (`freq_word_in_pos float entre 0 et 1`)

## Jeanne :  probabilité que le commentaire contienne le mot sachant qu’il est positif 
- [X] Calculer la probabilité que le mot soit présent dans le commentaire (word[i]) sachant que le commentaire est positif (ComPos), afin d’obtenir le score de positivité de chaque mot: `pos_score[i] = freq_word_in_pos / prob_pos`

### Format
- entrée : dictionnaire `freq_word_in_pos`
- sortie : dictionnaire de type `pos_score = {"word1":pos_score1, "word2":pos_score2}` où `pos_score1` désigne le score de positivité de word1 (float compris entre 0 et 1)


# Bayes (3 mai)

- [ ] Pour un com, faire une liste contentant tous les mots précédemment analysés (récupérer celle de Jeanne)
- [ ] Récuperer dans `pos_score` le score de chacun des mots
- [ ] Appliquer Bayes avec la formule : `P(comPos |word1, word2, word3...) = (pos_score[word1]*pos_score[word2]*pos_score[3])/(freq_word[word1]*freq_word[word2]*freq_word[word3])`
- [ ] Print le résultat de l'analyse


# **DONE** Tri divers (31 janvier)

## Louise
- [X] Télécharger et ouvrir un fichier json contenant un dataset de commentaires Amazon en anglais (commentaires et avis associés à une note allant de 1 à 5 étoiles) que l’on peut trouver sur internet et le convertir en un fichier csv.
- [X] Supprimer les données inutiles, c’est-à-dire la date, le nom de la personne, le titre, mais également les commentaires ayant 2, 3 ou 4 étoiles. Ainsi, on ne garde que le commentaire et la note correspondante, qui est de 1 ou de 5 pour simplifier l’analyse (le commentaire est donc soit positif, soit négatif).
- [ ] Commencer avec 1000 lignes (500 commentaires positifs et 500 commentaires négatifs)
- [X] Extraire les données et les transformer en liste
- [X] Remplacer les 1 et 5 par False et True

### Format :
- entrée : fichier CSV pré-traité manuellement
- sortie: liste `data_original = [("comm1", True), ("comm2", False), ("comm3", False)]`
- format : simple code


## Mathis
- [X] Lowercasing
- [X] Stop-words removal
- [X] Supprimer la ponctuation (simple anomalies noise removal)
- [X] Récupérer format de base

### Format :
- entrée : `data_original`
- sortie : `data_treated`
- forme : fonction `preProcessing()`


## Jeanne

- [X] Supprimer mots présents dans moins de 30% des com (à ajuster)
- [X] Calculer leur fréquence d’apparition dans la totalité des commentaires.

### Format :
- entrée : `data_treated`
- sortie : dictionnaire frequency_of_words = `{"word1":freq_word1, "word2":freq_word2}`
- format : fonction `frequency_of_words()`

---
