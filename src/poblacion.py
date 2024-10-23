from collections import namedtuple
import csv


RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta):
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


def calcula_poblaciones(poblaciones):
    paises = set()  
    for poblacion in poblaciones:   
        paises.add(poblacion.pais)
    return sorted(paises)

