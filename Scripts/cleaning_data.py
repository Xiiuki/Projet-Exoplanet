def cleaning_data():
    
    # importation de la bibliothèque pandas
    
    import pandas as pd
    
    
    try: 
        
        """
        On définie la dataframe 0 comme mère, elle 
        viens lire le fichier csv brut.
        Par la suite, nous créons des variables qui 
        correspondrons aux nouveaux csv.
        """

        df0 = pd.read_csv("./Data/csv_brut/exoplanets-stars.csv")

        # Création du csv planetary_system

        try:
            planetary_system = df0[["hostname", "sy_snum", "sy_pnum", "sy_mnum"]]
            
            planetary_system.rename(columns={"hostname": "system_name"}, inplace=True)

            planetary_system = planetary_system.drop_duplicates("system_name")

            planetary_system.to_csv("./Data/csv_cleaned/planetary_system.csv", sep=",", encoding="utf-8", index=False)
            
            print("Le csv planetary_system a été correctement créé ! \n")
        
        except:

            print("Un problème est survenue lors de la création du csv planetary_system ! \n")

        # Création du csv stars

        try:
        
            stars = df0[["hostname"]]

            stars = stars.drop_duplicates("hostname")

            stars.to_csv("./Data/csv_cleaned/stars.csv", sep=",", encoding="utf-8", index=False)
            
            print("Le csv stars a été correctement créé ! \n")

        except:

            print("Un problème est survenue lors de la création du csv stars ! \n")
        
        # Création du csv stars_specification

        try:
        
            stars_specification = df0[["st_spectype", "st_teff", "st_rad", 
                                    "st_mass", "st_lum","st_logg", "st_age", 
                                    "st_dens", "st_vsin", "sy_gaiamag"]]

            stars_specification = stars_specification.drop_duplicates()

            stars_specification.to_csv("./Data/csv_cleaned/stars_specification.csv", sep=",", encoding="utf-8", index=False)
    
            print("Le csv stars_specification a été correctement créé ! \n")

        except:

            print("Un problème est survenue lors de la création du csv stars_specification ! \n")
        
        # Création de la table planets

        try:
        
            planets= df0[["pl_name", "pl_letter"]]

            planets.to_csv("./Data/csv_cleaned/planets.csv", sep=",", encoding="utf-8", index=False)
            
            print("Le csv planets a été correctement créé ! \n")

        except:

            print("Un problème est survenue lors de la création du csv planets ! \n")
        
        # Création de la table planets_specification

        try:
        
            planets_specification = df0[["pl_orbper", "pl_rade", "pl_bmasse", "pl_dens", "pl_orbeccen",
                                        "pl_insol", "pl_eqt", "pl_orbincl", "pl_ratdor"]]

            planets_specification.to_csv("./Data/csv_cleaned/planets_specification.csv", sep=",", encoding="utf-8", index=False)
            
            print("Le csv stars_specification a été correctement créé ! \n")

        except:

            print("Un problème est survenue lors de la création du csv stars_specification ! \n")
        
        # Création de la table date

        try:
        
            date = df0[["disc_year", "disc_pubdate"]]

            date.to_csv("./Data/csv_cleaned/date.csv", sep=",", encoding="utf-8", index=False)
            
            print("Le csv date a été correctement créé ! \n")

        except:
            
            print("Un problème est survenue lors de la création du csv date ! \n")
        
        # Création du csv discovery_method

        try:
        
            discovery_method = df0[["discoverymethod", "disc_locale", "disc_facility", "disc_telescope"]]

            discovery_method.to_csv("./Data/csv_cleaned/discovery_method.csv", sep=",", encoding="utf-8", index=False)
            
            print("Le csv discovery_method a été correctement créé ! \n")

        except:

            print("Un problème est survenue lors de la création du csv discovery_method ! \n")
        
        
    except:
        
        print("Un problème est survenue lors de la création d'un csv !")

# Lorsque le fichier est appelé directement on exécute la fonction cleaning_data()

if __name__ == "__main__":
    
    cleaning_data()