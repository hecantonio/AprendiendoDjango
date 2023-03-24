from Inmueble import Inmueble

class Edificio(Inmueble):

    def __init__(self, direccion, superficie, costo, pisos, cantDormitorios):
        super().__init__(direccion, superficie, costo)
        self.pisos = pisos
        self.cantDormitorios = cantDormitorios

    #getters y setters

    def setPisos(self, pisos):
        self.pisos = pisos

    def getPisos(self):
        return self.pisos
    
    def setCantDormitorios(self, cantDormitorios):
        self.cantDormitorios = cantDormitorios
    
    def getCantDormitorios(self):
        return self.cantDormitorios        
        

    #Metodos

    def seleccionarPiso(self, piso):
        print("\n >> Piso seleccionado: " + str(piso))

    def getInfo(self):
        info = "\n\n----------------Información Edificio---------------"
        info += "\n Dirección: " + self.getDireccion()
        info += "\n Superficie: " + self.getSuperficie()
        info += "\n Costo: " + str(self.getCosto())
        info += "\n Pisos: " + str(self.getPisos())
        info += "\n Cantidad dormitorios: " + str(self.getCantDormitorios())

        return info