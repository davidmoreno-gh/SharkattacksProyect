import re
import pandas as pd
import numpy as np


def clean_labels(data):
    data.columns = data.columns.str.lower().str.replace(" ","_").str.replace(".","_").str.replace(":","").str.strip()
    data.rename(columns={"species_" : "species"})
    data.rename(columns={"unnamed_11" : "death"})
    return data

'''Esta función coge cada nombre de columna de nuestro dataframe, y aplica los siguientes métodos en string:
convierte todo en minúscula, remplaza los espacios, puntos y dos puntos por underscores
Elimina los posibles espacios del principio y final del string'''



def clean_corrupted_rows(data):
    useless_cols_to_drop = ['age', 'time', 'species', 'unnamed_21', 'unnamed_22']
    data = data.drop(columns = useless_cols_to_drop)
    return data

'''Esta función agrupa las columnas que hemos visto con más de un 60% de datos nulos y las borra'''



def eliminar_columnas_input(data):

    print("Columnas disponibles:")
    print(data.columns.tolist())
    
    selected_to_delete = input("Introduce las columnas que quieras eliminar (separadas por comas): ")
    selected_to_delete = [col.strip() for col in selected_to_delete.split(',')]
    
    columnas_no_existentes = [col for col in selected_to_delete if col not in data.columns]
    if columnas_no_existentes:
        print(f"Las siguientes columnas no existen en el DataFrame: {', '.join(columnas_no_existentes)}")
    
    data_user_clean = data.drop(columns=[col for col in selected_to_delete if col in data.columns])
    
    return data_user_clean



def clean_unwilling_rows(data):
    unwilling_cols_to_drop = ['date','type','name','injury']
    data = data.drop(columns = unwilling_cols_to_drop)
    return data



def clean_country(data, value):
    # We can delete the countries that have less than 13 attack
    data = data[data['country'].map(data['country'].value_counts()) > value]
    return data



def clean_state(data, value):
    # We can delete the states that have less than 16 attack
    data = data[data['state'].map(data['state'].value_counts()) > value]
    return data



def clean_sex(data, sub):
    changes = {' M': 'M', 'M x 2': 'M','M ': 'M', 'lli': 'F'}
    data[sub] = data[sub].replace(changes)
    return data



################# FUNCIONES DE DAVID ####################

'''def BC(string):
    """Mira en la cadena que le pasemos (pensado para el contenido de df.Date) nos va a devolver 0 
    en caso de que encuentre dentro de la cadena algo del tipo BC ó bc, para luego esos CEROS, convertirlos a null
    en nuestro df sobre el que vamos a graficar """
    try:
        x = re.search(r'(?i)B\.C', str(string))
        if x == []: #No hay match dentro de la cadena ("Date" de la fila en la que estemos)
            return string
        else:
            return np.nan #Si encuentra un Bc lo convierte en NaN
    except IndexError:
        return string'''

def interval_years(string):
    """Mira en la cadena que le damos si corresponden con stirngs de datos del tipo YYYY - YYYY o del tipo
    YYYY and YYYY, para poder hacer la media de este intervalo y ponerlo en la celda df.Year de esa fila"""
    try:
        y = re.findall('^\d{4}-\d{4}', str(string)) 
        if y != None:
            return int((int(y[0][:4])+int(y[0][5:]))//2) #Media del entero de los 4 primeros digitos + 4 siguientes
        else:
            return string
    except IndexError:
        return string

def sueltos (string): #4 Digitos aislados
    """Miramos los año sueltos que estan puesto solo como texto y un solo año"""
    try:
        z = re.findall("\d{4}", str(string))
        if z != None:
            return z[0]
        else:
            return 0
    except IndexError:
        return 0

def rescatar_fechas(string): #Clean column
    """A través de esta funcion aplicamos funcion BC y funcion interval_years en ese orden a lo largo de la string
    que le metamos, en principio elementos de la columna df.Date"""
    #string = BC(string)
    string = sueltos(string)
    string = interval_years(string)
    if int(string) == 0:
         return np.nan
    else:
        return string