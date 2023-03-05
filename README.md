# Dev_web

Description du projet :
Le projet consiste en une application web qui permet de récupérer les données de la base de données rna, puis de les afficher dans une interface. L'application web implémente un système de CRUD pour ajouter, supprimer et modifier les lignes de la base de données. L'application contient également un tableau de bord (dashboard) qui fournit des statistiques sur les données.
le projet contient : 
   un fichier Docker file : qui crée une image Docker qui contiendra une application Python Flask.
   un fichier docker-compose :  configuration YAML
   un dossier src : contenant : 
        un dossier app :
            un dossier static : contenant notre fichier css
            un dossier templates : contenant nos pages html
            un fichier __init__ : contenant notre application web il genere nos page html et gere la base données 
        un dossier import : contenant : 
             le dossier data:  base de données rna dans des fichiers csv
            le fichier import.py : pour inseres nos fichiers csv dans la bdd rna 

Technologies utilisées :

HTML : utilisé pour créer les pages web
Python : utilisé pour le code backend
Docker : utilisé pour faciliter le déploiement de notre application
       conteneurs: 
       web : pour exécuter notre application web 
       phpMyAdmin : pour le serveur de la base de données
       MySQL : pour la gestion de la bases de données


