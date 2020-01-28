# To-do

# Tri divers (31 janvier)

## Louise :
- [ ] Télécharger et ouvrir un fichier json contenant un dataset de commentaires Amazon en anglais (commentaires et avis associés à une note allant de 1 à 5 étoiles) que l’on peut trouver sur internet et le convertir en un fichier csv.
- [ ] Supprimer les données inutiles, c’est-à-dire la date, le nom de la personne, le titre, mais également les commentaires ayant 2, 3 ou 4 étoiles. Ainsi, on ne garde que le commentaire et la note correspondante, qui est de 1 ou de 5 pour simplifier l’analyse (le commentaire est donc soit positif, soit négatif). Commencer avec 1000 lignes (500 commentaires positifs et 500 commentaires négatifs)
- [ ] Extraire les données et les transformer en liste
- [ ] Remplacer les 1 et 5 et False et True

### Format
- entrée : fichier CSV pré-traité manuellement
- sortie: liste `data_original = [("comm1", True), ("comm2", False), ("comm3", False)]`
- format : simple code


## Mathis
- [ ] Lowercasing
- [ ] Stop-words removal
- [ ] Supprimer la ponctuation (simple anomalies noise removal)

### Format
- entrée : `data_original`
- sortie : `data_original`
- forme : plusieurs fonctions


## Jeanne

- [ ] Rechercher mots + fréquents dans les com et garder ceux présents dans + de 30% des com (ajuster)
- [X] Calculer leur fréquence d’apparition dans la totalité des commentaires.

### Format
- entrée : `data_original`
- sortie : dictionnaire frequency_of_words = `{"word1":freq_word1, "word2":freq_word2}`
- format : plusieurs fonctions

---

# Score de positivité (22 février)
