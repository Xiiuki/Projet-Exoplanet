# Projet-Exoplanets

<img src="Images/téléchargement.jpeg" width="60%">

##### Photo by : NASA

### [GitLab version](https://gitlab.com/simplon-dev-data-nantes-2020/projet-chef-d-oeuvre/-/tree/Matthias_Mews/) | [GitHub version](https://github.com/Xiiuki/Projet-Exoplanets)


## <br>  Contexte du projet : </br>

Pour valider la certification Simplon dévellopeur Data, ce projet consiste à répondre à une demande client qui est la suivante :

- Fournir un Dashboard sur les données scientifiques d'exoplanètes.

Il faudrat donc réaliser toutes les étapes d'un dévellopeur data, études de la demande client, la collecte de données, l'analyse de celles-ci, la création d'une base de données, l'insertion des données, puis enfin questionner cette base de données afin d'obtenir un dashboard.

## <br> Livrables : </br> 
--------

    ├── README.md                          <--- Descriptif du projet
    │
    │
    ├── Rapport                            <--- Rapport projet + présentation 
    │
    │
    ├── Documents                          <--- Dossier documentation Client / Certif / Architecture BDD / Guide
    │   ├── Clients
    │   ├── Référentiel-certification
    │   ├── Guide
    │   └── Architecture 
    │   
    ├── Analyse_csv                        <--- Dossier regroupant des analyses csv 
    │
    │
    ├── Data                               <--- Dossier regroupant le csv original, puis les csv nettoyés
    │   ├── csv_brut
    │   └── csv_cleaned
    │
    ├── Scripts                            <--- Dossier regroupant des fichiers .py pour la bonne exécution du projet
    │
    │
    ├── Backup                             <--- Dossier de sauvegarde de la base de données
    │
    │
    ├── Templates                          <--- Dossier templates pour dashboard / amélioration projet        
    │   ├── Prototype dashboard
    │   └── Amélioration 
    │
    ├── Images                             <--- Dossier d'images     
    │
    │
    └── requirements.txt                   <--- Fichier essentiel pour l'installation des librairies     

--------

## <br> Requirements : </br>

```
- Les scripts sont testés sous Windows 10
- Python 3.8 + requirements 
- PostgreSQL 13 
- pgAdmin4 4.29
- MongoDB 1.26
- Visual Studio Code 1.56
- StarUML pour la lecture du fichier .mdj (https://staruml.io/download)
```


## <br> Installation </br>

Installation de postgresql :

Suivre les étapes indiquées :

- [download](https://www.postgresql.org/download/windows/)

- [installation](https://www.veremes.com/installation-postgresql-windows)

Installation pgAdmin4 :

- [download](https://www.pgadmin.org/download/)

Installation MongoDB pour les metadonnées :

- Voir Documents / guide 

Installation Visual Studio Code :

- [download](https://code.visualstudio.com/download)

- [installation](https://code.visualstudio.com/docs/introvideos/basics)


Le clone du projet et sa bonne installation sur votre pc sous git Bash:

- Le clonage (deux choix se proposent à vous) :
 
 
  - With github :
  
    ```
    cd 
    mkdir Exoplanets
    cd Exoplanets/
    git clone https://github.com/Xiiuki/Projet-Exoplanets                                                                    
    ```
    
  - With Gitlab :
    
    ```
    cd c:/
    mkdir Exoplanets
    cd Exoplanets/
    git clone git@gitlab.com:simplon-dev-data-nantes-2020/projet-chef-d-oeuvre.git                                                                   
    ```
  

 - Lancer VSCode 
 
 - Ouvrir le dossier cloner dans celui-ci

 - Ouvrir le terminal dans VScode 

   ```
   ctrl + shift + ù
   ```

 - Création de l'environnement virtuelle :
 
    ```
    python -m venv Exoplanets3.8
    ```
     
 - Lancement de l'environnement :

    ``` 
    ctrl + shift + p 
    ```  

    ```
    Python : Select Interpreter
    ```
    
    ```
    Selectionner le venv créé
    ```

 - Dans le terminal :

   ```
   .\Exoplanets\Scripts\activate
   ```

 - Installation des librairies :
    
    ```
    python -m pip install pip --upgrade
    python -m pip install -r requirements.txt
    ```
    
## <br> Exécution de l'application </br>

Suivre l'ordre donné :

- [cleaning_data](Scripts/cleaning_data.py)

- [create_database](Scripts/create_database.py)

- [insert_data](Scripts/insert_data.py)

- [backup_data](Scripts/backup_database.py)

- [queries](Scripts/queries.py)

- [app_vizualisation](Scripts/app_vizualisation.py)

Petit plus, avec les métadonnées :

- [metadata](Scripts/metadata.py)

Puis lancer MongoDB, connection, metadonnee, metadata_collection

## <br> Attention : </br>

Pour toutes demandes de renseignements, veuillez contacter l'autheur de ce projet via adresse mail uniquement.