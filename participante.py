import pandas as pd
import matplotlib as plt

class Participante:
    #Diccionario precios: indica taller artístico vs su precio
    precios = {
        "Pintura": 6000,
        "Teatro": 8000,
        "Danza": 7000
    }
    
    #Método de Python: crep un nuevo objeto de la clase
    def __init__(self, nombre, edad, taller, clases):
        self.nombre = nombre
        self.edad = int(edad)
        self.taller = taller
        self.clases = int(clases)

    def calcular_total_a_pagar(self):
        return self.clases * Participante.precios.get(self.taller, 0)

    def diccionario(self):
        return {
            "Nombre": self.nombre,
            "Edad": self.edad,
            "Taller": self.taller,
            "Clases": self.clases,
            "Total a Pagar": self.calcular_total_a_pagar()
        }