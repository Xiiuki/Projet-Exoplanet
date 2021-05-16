 
def create_database():

    # importation de la bibliothèque psycopg2
    
    import psycopg2

    import os

    # variable par défaut

    utilisateur = "postgres"

    # à définir dans les variables d'environnement

    mot_passe = os.environ.get('pg_psw')

    """
    Connexion dans un premier temps à la database postgres
    pour initialiser notre database exoplanets
    """

    # création de l'objet conn1 via la fonction connect de psycopg2

    conn1 = psycopg2.connect(database="postgres", user=utilisateur, password=mot_passe, host='127.0.0.1', port= '5432')
    
    # on force le commit

    conn1.autocommit = True

    # deux requêtes SQL pour suppresion / création 

    drop = '''DROP DATABASE IF EXISTS exoplanets;'''
    
    create = '''CREATE DATABASE exoplanets;'''

    # initialisation du cursor

    cursor = conn1.cursor()

    # try/except sur cursor.execute permet d'exécuter une commande 'sql'

    try:
        cursor.execute(drop)
        
        print("La base de données à été supprimée avec succès !")
        
    except:
        
        print("Un problème est survenue lors de la suppresion de la base de données !")

    try:
        
        cursor.execute(create)
        
        print("La base de données à été créée avec succès !")
        
    except:
        
        print("Un problème est survenue lors de la création de la base de données !")
    
    # ferme le curseur et devient inutilisable

    cursor.close
    
    # ferme la connexion à database

    conn1.close
    
    """
    Connexion dans un deuxième temps  à la database
    exoplanets pour création de ces tables
    """
    # création de l'objet conn2 via la fonction connect de psycopg2

    conn2 = psycopg2.connect(database="exoplanets", user=utilisateur, password=mot_passe, host='127.0.0.1', port= '5432')
    
    # on force le commit

    conn2.autocommit = True

    # initialisation du cursor

    cursor = conn2.cursor()
    
    # cursor.execute permet d'exécuter une commande 'sql'

    # création de la table planets_specification
    
    try:

        cursor.execute('''CREATE TABLE IF NOT EXISTS planets_specification(
                    psp_id SERIAL PRIMARY KEY NOT NULL,
                    pl_orbper REAL,
                    pl_rade REAL,
                    pl_bmasse REAL,
                    pl_dens REAL,
                    pl_orbeccen REAL,
                    pl_insol REAL,
                    pl_eqt REAL,
                    pl_orbincl REAL,
                    pl_ratdor REAL);
                ''')

        # Création de la table date
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS date(
                    date_id SERIAL PRIMARY KEY NOT NULL,
                    disc_year INTEGER,
                    disc_pubdate TEXT);
                ''')
        
        # Création de la table discovery
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS discovery(
                    disc_id SERIAL PRIMARY KEY NOT NULL,
                    discoverymethod TEXT,
                    disc_locale TEXT,
                    disc_facility TEXT,
                    disc_telescope TEXT);
                ''')
        
        # Création de la table planets
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS planets(
                    pl_id SERIAL PRIMARY KEY NOT NULL,
                    pl_name TEXT,
                    pl_letter TEXT,
                    date_id SERIAL,
                    FOREIGN KEY(date_id)
                        REFERENCES date(date_id),
                    disc_id SERIAL,
                    FOREIGN KEY (disc_id)
                        REFERENCES discovery(disc_id),
                    psp_id SERIAL,
                    FOREIGN KEY(psp_id)
                        REFERENCES planets_specification(psp_id));
                ''')
        
        # Création de la table stars_specification
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS stars_specification(
                    ssp_id SERIAL PRIMARY KEY NOT NULL,
                    st_spectype TEXT,
                    st_teff REAL,
                    st_rad REAL,
                    st_mass REAL,
                    st_lum REAL,
                    st_logg REAL,
                    st_age REAL,
                    st_dens REAL,
                    st_vsin REAL,
                    sy_gaiamag REAL);
                ''')
        
        # Création de la table stars
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS stars(
                    stars_id SERIAL PRIMARY KEY NOT NULL,
                    hostname TEXT,
                    ssp_id SERIAL,
                    FOREIGN KEY(ssp_id)
                        REFERENCES stars_specification(ssp_id));
                ''')
        
        # Création de la table planetary_system
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS planetary_system(
                    ps_id SERIAL PRIMARY KEY NOT NULL,
                    system_name TEXT,
                    sy_snum INTEGER,
                    sy_pnum INTEGER,
                    sy_mnum INTEGER,
                    stars_id SERIAL,
                    FOREIGN KEY(stars_id)
                        REFERENCES stars(stars_id),
                    pl_id SERIAL,
                    FOREIGN KEY(pl_id)
                        REFERENCES planets(pl_id));
                ''')

        print("Création des tables effectuée avec succès !")

    except:

        print(" Un problème est survenue lors de la création des tables !")


    # ferme le curseur et devient inutilisable

    cursor.close

    # ferme la connexion à database

    conn2.close()
    
    

# Lorsque le fichier est appelé directement on exécute la fonction create_database()

if __name__ == "__main__":
    
    create_database()