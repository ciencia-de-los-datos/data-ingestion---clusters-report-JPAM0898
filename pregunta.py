"""
Ingestión de datos - Reporte de originales
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'originals_report.txt', teniendo en cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo espacio entre palabra y palabra.


"""
import pandas as pd
import re
import numpy as np


def ingest_data():
    #df = pd.read_csv('clusters_report.txt', sep='\t', header=None, names=['original'])
    # df['original'] = df['original'].str.replace('cluster', '').replace('Cantidad de', '').replace('Porcentaje de', '').replace('Principales palabras clave', '').replace('palabras clave', '').str.replace('-', '')

    df = pd.read_fwf("clusters_report.txt", colspecs=[(3,5),(9,14),(25,29),(40,119)], header=None)
    df.drop(df.index[:3], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df2 = pd.DataFrame()
    df2['cluster'] = df[0]
    df2['cantidad_de_palabras_clave'] = df[1]
    df2['porcentaje_de_palabras_clave'] = df[2].str.replace(',', '.')
    df2.dropna(inplace=True)
    df2.reset_index(drop=True,inplace=True)
    df2['cluster'] = df2['cluster'].str.strip()
    df2['cantidad_de_palabras_clave'] = df2['cantidad_de_palabras_clave'].str.strip()
    df2['porcentaje_de_palabras_clave'] = df2['porcentaje_de_palabras_clave'].str.strip()
           
        

    
    return df2