# To-do list   
### Pour la semaine pro
- [X] Trouver dataset 
- [X] Ouvrir dataset
- [X] Trier données pour garder uniquement avis + note associée
- [X] Faire liste de la forme : `data_original = [("bla", True), ("bla2", False)]`


### Objectifs
 - [ ] trier les données pour garder que la note et le commentaire (notes extrêmes uniquement)
 - [ ] Analyser la fréquence des mots selon si les commentaires sont positifs (5 étoiles) ou négatifs (1 étoile)
 - [ ] Application du théorème de Bayes pour associer chaque mot à un score de positivité
 - [ ] Calculer la probabilité avec un nouveau commentaire qu'il soit positif ou négatif selon les mots utilisés

### Améliorations
 - [ ] Calcul de la fréquence d'erreurs
 - [ ] Interface graphique
 - [ ] Ajouter commentaires de 2 et 4 (puis 3)
 - [ ] Jeu entre utilisateur et algo pour déterminer la note
 - [ ] [Pre-processing de texte](https://kavita-ganesan.com/text-preprocessing-tutorial/) (très important dans notre cas : lowercaisng + noise removal, voire normalization + stop-word removals, voire text enrichment)



# Organisation

## Commun : 

- Ouvrir json, enlever colonnes inutiles, commencer avec 1000 lignes (500+ et 500-), convertir json en csv, extraire et transformer en liste (1 et 5 uniquement) (Louise)
- Nettoyer texte (pre-processing: stop-words removal, lowercasing) (Mathis)
- Rechercher mots + fréquents (en gardant ceux qui sont présents dans plus de x % des com, en calculant leur fréquence) (Jeanne)
-> (28 janvier)

- Associer à chaque mot son *"score de positivité"* : ComPos, MotInCom -> P(ComPos|MotInCos) =  P(ComPos & MotInCom)/P(MotInCom) ; sachant que  ComPos & MotInCom  =  nombre de fois où le mot est présent dans un com positif/ nombre de fois où il est est présent au total (commun)
-> (22 février)

- Pour un com donné, faire une liste avec uniquement les mots précédement analysés (Louise ou commun)
- Appliquer le théorême de Bayes (commun)
-> avoir fini à la fin des vacances de Pâques (3 mai)
