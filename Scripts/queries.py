# importation de plusieurs bibliothèques

from sqlalchemy import create_engine
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

# Analyse exoplanètes

df1 = pd.read_sql("""
            SELECT pl_letter, COUNT(pl_letter)
            FROM planets
            GROUP BY pl_letter 
            """, engine)

fig1 = px.bar(df1, y='pl_letter', x='count')

# Masse de l'exoplanète / période orbital 

df2 = pd.read_sql("""
            SELECT pl_name , pl_bmasse, pl_orbper
            FROM planets
            LEFT JOIN planets_specification ON planets.psp_id = planets_specification.psp_id
            """, engine)

fig2 = px.scatter(df2, 
                x="pl_orbper", 
                y="pl_bmasse",
                hover_data=['pl_name'],
                labels=dict(pl_orbper="Période Orbitale en jours",
                            pl_bmasse="Masse de l'exoplanète (relative par rapport à la Terre)",
                            pl_name="Nom exoplanète"),
                title="<b> Influence de la masse de l'exoplanète sur sa période orbitale <b>"
                )

fig2.update_xaxes(range=[-3000, 40000])
fig2.update_yaxes(range=[-3000, 40000])

# Analyse stars 

# Diagram de Hertzsprung russell 

df3 = pd.read_sql("""
            SELECT hostname, st_lum, st_teff
            FROM stars
            LEFT JOIN stars_specification ON stars.ssp_id = stars_specification.ssp_id
            WHERE st_lum IS NOT NULL
                AND st_teff IS NOT NULL
            ORDER BY st_teff DESC
            """, engine)

# Cette variable permet d'initialiser la couleurs 

df = pd.read_csv(".\Data\csv_cleaned\stars_specification.csv")

df["st_teff"] = df["st_teff"].astype(str) #convert to string

df["st_teff"] = df["st_teff"].astype(float) #convert back to numeric

# Création de la figure 3 

fig3 = px.scatter(df3,
                x="st_teff", 
                y="st_lum", 
                hover_data=['hostname'],
                color="st_teff", 
                labels=dict(st_teff="Température éffective en Kelvin", 
                            st_lum="Luminosité (Soleil = 1)",
                            hostname="Nom étoile"),
                title="<b> Diagramme de Hertzsprung Russell (en fonction de la Luminosité / Kelvin) <b>"
                )

fig3.update_xaxes(range=[30000, 1000])