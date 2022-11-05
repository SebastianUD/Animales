class Animal:
    def __init__(self):
        self.peso=0
        self.edad=0
        self.raza=""
        self.propietario=""
        self.fecha_vacunacion=""
    
    def correr(self):
        if self.edad >=5:
            print("rapido")
        elif self.edad < 5:
            print("lento")
    
    def emitir_sonido(self):
        pass
            
    def obtener_edad(self):
        pass