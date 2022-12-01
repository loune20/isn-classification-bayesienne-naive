# Classification bayésienne naïve
Projet d'isn écrit en **Python** pour s'initier au machine learning.  
Cet exemple se base sur le site de [Lovely Analytics](https://lovelyanalytics.com/2018/10/04/classification-bayesienne-naive-comment-ca-marche/)  
Pour en apprendre plus sur le théorême de Bayes (en anglais) : [ici](https://actuairesbigdata.wordpress.com/2016/01/13/une-explication-simple-de-classification-naive-bayesienne/) et [ici](https://arbital.com/p/bayes_rule/?l=1zq).  
On se propose d'utiliser comme outil Git, [Jupyter](https://www.dataquest.io/m/349-project-learn-and-install-jupyter-notebook/), Discord, HackMD : [Sprint1](https://hackmd.io/@loune/sprint1), [Sprint2](https://hackmd.io/@JeanneD/sprint2)

---

[Amazon dataset](http://jmcauley.ucsd.edu/data/amazon/),  
[App store dataset](https://medium.com/the-research-nest/data-science-tutorial-analysis-of-the-google-play-store-dataset-c720330d4903),  
[Video Games Amazon dataset](http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Video_Games_5.json.gz)  

---

# To-do
- [X] Sprint 2 (correction du sprint 1 avec ce qu'on a réellement fait au final) LIEN [ICI](https://hackmd.io/@JeanneD/sprint2)
- [X] Se répartir plus en détail les tâches à faire pour la 3ème partie

# Bayes
(3 mai)

- [ ] Pour un com, faire une liste contentant tous les mots précédemment analysés (récupérer celle de Jeanne) (words_list mais à actualiser) (Jeanne)
- [ ] Récuperer dans `pos_score` le score de chacun des mots (Jeanne)
- [ ] Appliquer Bayes avec la formule : `P(comPos |word1, word2, word3...) = (pos_score[word1]*pos_score[word2]*pos_score[3])/(freq_word[word1]*freq_word[word2]*freq_word[word3])` (Mathis si pas GUI, sinon Louise)
- [ ] Print le résultat de l'analyse : interface graphique (Louis si pygame, Mathis si Tkinter)


# Tri divers
(fini le 4 février)

## Louis
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


# Score de positivité
(fini le 11 février)

## Mathis : fréquence d'appparition du mot dans les commentaires positifs
- [X] Calculer fréquence apparition des mots de la liste `freq_word` dans les com positifs
- [X] Associer chaque mot à cette fréquence
- [X] Si elle est comprise entre 0.45 et 0.55 (ajuster) on supprime le mot de la liste

### Format
- entrée : dictionnaire `freq_word`
- sortie : dictionnaire `freq_word_in_pos = {"word1": freq_word1_in_pos, "word2": freq_word2_in_pos}` (`freq_word_in_pos float entre 0 et 1`)

## Jeanne :  probabilité que le commentaire contienne le mot sachant qu’il est positif 
- [X] Calculer la probabilité que le mot soit présent dans le commentaire (word[i]) sachant que le commentaire est positif (ComPos), afin d’obtenir le score de positivité de chaque mot: `pos_score[i] = freq_word_in_pos / prob_pos`

### Format
- entrée : dictionnaire `freq_word_in_pos`
- sortie : dictionnaire de type `pos_score = {"word1":pos_score1, "word2":pos_score2}` où `pos_score1` désigne le score de positivité de word1 (float compris entre 0 et 1)

---
