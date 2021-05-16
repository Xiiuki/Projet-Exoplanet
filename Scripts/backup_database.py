def backup_database():

    # importation des bibliothèques datetime/pathlib/zipfile

    from datetime import datetime

    from pathlib import Path

    import zipfile

    # initialisaiton des varialble path + amount 

    # le fichier ou dossier à sauvegarder

    OBJECT_TO_BACKUP = 'C:\\Program Files\PostgreSQL\\13\\data\\base\\380852'

    # dossier ou va être stocker la sauvegarde 

    BACKUP_DIRECTORY = 'C:\Exoplanets\Projet-Exoplanets\Backup'

    # le maximum de sauvegarde qui doit être présent dans le dossier sauvegarde 

    MAX_BACKUP_AMOUNT = 1  

    try:

        object_to_backup_path = Path(OBJECT_TO_BACKUP)
        
        backup_directory_path = Path(BACKUP_DIRECTORY)

        # valide que l'objet que nous allons sauvegarder existe avant de continuer

        assert object_to_backup_path.exists()  

        # valide que le répertoire de sauvegarde existe et créez-le si nécessaire
        
        backup_directory_path.mkdir(parents=True, exist_ok=True)

        # regarde le nombre de backup dans le dossier 
        
        existing_backups = [
            x for x in backup_directory_path.iterdir()
            if x.is_file() and x.suffix == '.zip' and x.name.startswith('backup-')
        ]

        # supprime les anciens backup pour correspondre au max_backup avant ajout du nouveau
        
        oldest_to_newest_backup_by_name = list(sorted(existing_backups, key=lambda f: f.name))

        # >= car nous allons en avoir un nouveau bientôt 

        while len(oldest_to_newest_backup_by_name) >= MAX_BACKUP_AMOUNT:  
            
            backup_to_delete = oldest_to_newest_backup_by_name.pop(0)
            
            backup_to_delete.unlink()

        # crée un fichier zip (pour les fichier et dossier d'option)
        
        backup_file_name = f'backup-{datetime.now().strftime("%Y%m%d-%H,%M,%S")}-{object_to_backup_path.name}.zip'
        
        zip_file = zipfile.ZipFile(str(backup_directory_path / backup_file_name), mode='w')
        
        if object_to_backup_path.is_file():
            
            # si l'objet à écrire est un fichier, écrivez le fichier
            
            zip_file.write(
                object_to_backup_path.absolute(),
                arcname=object_to_backup_path.name,
                compress_type=zipfile.ZIP_DEFLATED
            )

        elif object_to_backup_path.is_dir():
            
            # si l'objet à écrire est un répertoire, écrivez tous les fichiers
            
            for file in object_to_backup_path.glob('**/*'):
                
                if file.is_file():
                    
                    zip_file.write(
                        file.absolute(),
                        arcname=str(file.relative_to(object_to_backup_path)),
                        compress_type=zipfile.ZIP_DEFLATED
                    )
                    
        # ferme le fichier zip
        
        zip_file.close()

        print("La sauvegarde de la  base de données a été un succès !")

    except:

        print("La sauvegarde de la base de données a échoué !")

# Lorsque le fichier est appelé directement on exécute la fonction backup_database()

if __name__ == "__main__":
    
    backup_database()