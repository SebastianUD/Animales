from animal import Animal
from perro import Perro
from bovino import Bovino

class Granja(Animal):
    def __init__(self):
        self.Misperros=[]
        self.Misbovinos=[]
    
    def agregar_perro(self,edad,raza,peso,propietario,fecha):
        miPerro=Perro()
        miPerro.edad = edad
        miPerro.raza = raza
        miPerro.peso = peso
        miPerro.propietario = propietario
        miPerro.fecha_vacunacion = fecha
        self.Misperros.append(miPerro)
    
    def agregar_bovino(self,edad,raza,peso,propietario,fecha,establo):
        miBovino=Bovino()
        miBovino.edad = edad
        miBovino.raza = raza
        miBovino.peso = peso
        miBovino.propietario = propietario
        miBovino.fecha_vacunacion = fecha
        miBovino.establo = establo
        self.Misbovinos.append(miBovino)
    
    def obtener_perro(self,indice):
        return self.Misperros[indice]
    
    def obtener_bovino(self,indice):
        return self.Misbovinos[indice]