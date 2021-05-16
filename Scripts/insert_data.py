def insert_data(): 
    
    # importation de la bibliothèque sqlachemy et pandas 
    
    import os
    
    from sqlalchemy import create_engine
    
    import pandas as pd

    """ 
    Initialisation de l'engin SQLalchemy 
    pour ce connecter à la database exoplanets
    """

    user = 'postgres'
    password = os.environ.get('pg_psw')
    host = '127.0.0.1'
    port = '5432'
    dbname = 'exoplanets'  

    # creation de la variable engine 

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")

    """ 
    try/except sur les differentes insertion 
    l'utilisation des fonctions pandas permettes :
    - read_csv lire le csv voulu 
    - to_sql insérer les données dans la database
    """

    try:

        planets_specification = pd.read_csv("./Data/csv_cleaned/planets_specification.csv")

        planets_specification.to_sql('planets_specification', engine, if_exists='append', index=False)

        print("L'insertion des données de planets_specification c'est bien déroulée !")

    except:

        print(" Une erreur est survenue lors de l'insertion des données de planets_specification !")

    try:
     
        date = pd.read_csv("./Data/csv_cleaned/date.csv")

        date.to_sql('date', engine, if_exists='append', index=False)

        print("L'insertion des données de date c'est bien déroulée !")

    except:

        print(" Une erreur est survenue lors de l'insertion des données de date !")

    try:

        discovery = pd.read_csv("./Data/csv_cleaned/discovery_method.csv")

        discovery.to_sql('discovery', engine, if_exists='append', index=False)

        print("L'insertion des données de discovery c'est bien déroulée !")

    except:

        print(" Une erreur est survenue lors de l'insertion des données de discovery !")

    try:

        planets = pd.read_csv("./Data/csv_cleaned/planets.csv")

        planets.to_sql('planets', engine, if_exists='append', index=False)

        print("L'insertion des données de planets c'est bien déroulée !")

    except:

        print(" Une erreur est survenue lors de l'insertion des données de planets !")
    
    try:
    
        stars_specification = pd.read_csv("./Data/csv_cleaned/stars_specification.csv")

        stars_specification.to_sql('stars_specification', engine, if_exists='append', index=False)

        print("L'insertion des données de stars_specification c'est bien déroulée !")

    except:
        
        print(" Une erreur est survenue lors de l'insertion des données de stars_specification !")

    try:

        stars = pd.read_csv("./Data/csv_cleaned/stars.csv")

        stars.to_sql('stars', engine, if_exists='append', index=False)

        print("L'insertion des données de stars c'est bien déroulée !")

    except:

        print(" Une erreur est survenue lors de l'insertion des données de stars !")

    try:

        planetary_system = pd.read_csv("./Data/csv_cleaned/planetary_system.csv")

        planetary_system.to_sql('planetary_system', engine, if_exists='append', index=False)

        print("L'insertion des données de planetary_system c'est bien déroulée !")
    
    except:

        print(" Une erreur est survenue lors de l'insertion des données de planetary_system !")

# Lorsque le fichier est appelé directement on exécute la fonction insert_data()

if __name__ == "__main__":
    
    insert_data()