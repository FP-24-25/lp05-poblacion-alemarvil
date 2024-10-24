from collections import namedtuple
import csv
from unicodedata import digit


RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta:str)-> list [RegistroPoblacion]:
    '''lector del archivo csv

    :param ruta: ruta
    :type ruta: str
    :return: lista 
    :rtype: _type_
    '''
    poblaciones=[]
    with open(ruta, encoding='utf-8') as f:
        lector_csv = csv.reader(f)
        for pais, codigo, año, censo in lector_csv:
            RegistroPoblacion = poblaciones(
                pais = str(pais),
                codigo = str(codigo),
                año = int(año),
                censo = int(censo)
            )
            poblaciones.append(RegistroPoblacion)
    return poblaciones


def calcula_paises(poblaciones:list[RegistroPoblacion])-> list[str]:
    paises = set()  
    for poblacion in poblaciones:   
        paises.add(poblacion.pais)
    return sorted(paises)


def filtra_por_pais(poblaciones,nombre_o_codigo):
    nombre_o_codigo:dict(str,str) = {}
    for pais in poblaciones:
        nombre_o_codigo[pais.pais] = pais.codigo
    return nombre_o_codigo
    datos = []
    for dato in poblaciones:
        
        

    


