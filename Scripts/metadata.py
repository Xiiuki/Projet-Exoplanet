def metadata(): 
    import os
    import pymongo
    import subprocess
    import json
    from pymongo import MongoClient

    # chemin du dossier à meta
    path = "C:\Exoplanets\Projet-Exoplanets"

    # exclusion de fichier 

    exclude = set([".ipynb_checkpoints", ".git", ".vscode", "Exoplanets3.8"])

    # création d'une liste viste 

    shpfiles = []

    for dirpath, subdirs, files in os.walk(path):

        subdirs[:] = [d for d in subdirs if d not in exclude]

        for x in files:

            shpfiles.append(os.path.join(dirpath, x))

    # print(shpfiles)

    for l in shpfiles:

        input_file = l.replace("\\", "/")
        exe = "C:/Exiftool/exiftool.exe"
        process = subprocess.Popen([exe, input_file], stdout=subprocess.PIPE, stderr= subprocess.STDOUT, universal_newlines=True)
        print(input_file) # si ça bloque tu sais quel fichier n'est pas lu correctement

        # création d'un dictionnaire 
        metadata = {}

        for output in process.stdout:

            line = (output.strip().split(":",1))
            metadata[line[0].strip()] = line[1].strip()

        # permet la création du client qui va se connecter à MongoDB

        client = MongoClient()

        # préparation à la création de la base de données metadonnee

        db = client.metadonnee

        collection = db.metadata_collection
        
        result = collection.insert_one(metadata)

        # permet de vérifier la liste des collections créées :

        db.list_collection_names()

# Lorsque le fichier est appelé directement on exécute la fonction metadata()

if __name__ == "__main__":
    
    metadata()