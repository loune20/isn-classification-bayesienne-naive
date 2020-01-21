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


- Télécharger et ouvrir un fichier json contenant un dataset de commentaires Amazon anglais (commentaires et avis associés à une note allant de 1 à 5)
Supprimer les données inutiles, c'est-à-dire la date, le nom de la personne ayant écrit le commentaire, le titre du commentaire, mais également les commentaires ayant 2, 3 ou 4 étoiles. Ainsi, on ne garde que le commentaire et la note correspondante, qui est de 1 ou de 5 pour simplifier l'analyse (le commentaire est soit positif, soit négatif).
Commencer avec 1000 lignes (500 commentaires positifs et 500 commentaires négatifs), convertir le fichier json en csv, extraire et transformer en liste  (Louise)

- Nettoyer le texte : mettre tout en minuscule, supprmier les mots de liaisons et les mots très courants qui n'ont pas d'importance dans l'analyse du texte (and, the, a, it, they etc...) (pre-processing: stop-words removal, lowercasing) (Mathis)

- Rechercher des mots les plus fréquents (en gardant ceux qui sont présents dans plus de x % des com, en calculant leur fréquence) (Jeanne)
-> **(28 janvier)**

- Associer à chaque mot son *"score de positivité"* : ComPos, MotInCom -> P(ComPos|MotInCos) =  P(ComPos & MotInCom)/P(MotInCom) ; sachant que  ComPos & MotInCom  =  nombre de fois où le mot est présent dans un com positif/ nombre de fois où il est est présent au total (commun)
-> **(22 février)**

- Pour un com donné, faire une liste avec uniquement les mots précédement analysés (Louise ou commun)
- Appliquer le théorême de Bayes (commun)
-> avoir fini à la fin des vacances de Pâques **(3 mai)**
