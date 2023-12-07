```lua
● Utilisez Python 3.9+ et Django 4.2+ pour cet exercice
● Utilisez votre gestionnaire de dépendances de choix
● Fournissez toutes les informations nécessaires pour exécuter localement dans le fichier README du dépôt et
un emplacement de fichier .env si nous devons exécuter des migrations, etc.
● Suivez les meilleures pratiques
● Veuillez me fournir un moyen de consulter le code : GitHub, Bitbucket, etc.

Créez une API basée sur Django à l'aide de Django REST Framework qui expose deux points de terminaison pour une
application qui ne peut actuellement être utilisée que pour les données de 2020 :
● processFile – POST
  ○ Accepte un fichier CSV
  ○ Traite le fichier CSV et valide chaque ligne
  ○ Ce document est livré avec quelques small.csv que votre programme devrait
accepter, contenant les colonnes suivantes :
    ■ date
    ■ country
    ■ purchase/sale
    ■ currency
    ■ net
    ■ Vat
  ○ Stocke les résultats de la validation des lignes et des cellules dans une structure de données appropriée
  ○ Lors du traitement d'une ligne, convertissez la colonne currency en EUR en récupérant
le taux requis à partir d'une API de convertisseur de devises
● retrieveRows – GET
  ○ Prend deux paramètres de requête
    ■ country (code ISO 3166)
    ■ date (AAAA/MM/JJ)
  ○ Renvoie une réponse JSON contenant les lignes en fonction du pays correct et de la
date
  ○ par exemple /retrieveRows?country=DE&date=2020/08/05
● Concevez l'étape de traitement pour évoluer aussi doucement que possible avec l'API de la banque
● Documentez les étapes prises pour atteindre cet objectif dans le fichier README du dépôt.
● Utilisez uniquement des bibliothèques tierces là où c'est nécessaire et utilisez du Python pur autant que possible.

```