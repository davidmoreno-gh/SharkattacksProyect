import re
import numpy as np
import pandas as pd

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