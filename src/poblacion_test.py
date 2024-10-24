from poblacion import *


def test_lee_poblaciones(lista_poblaciones:list[RegistroPoblacion]):
    print(f"Se han leido {len(lista_poblaciones)}")
    print("Los dos primeros registros son")
    print(lista_poblaciones[:2])
    print("Los don últimos registros son")
    print(lista_poblaciones[-2:0])


if __name__ == "__main__":
    registros = lee_poblaciones("data/population.csv")
    #calcula_paises(registros)



