from Inmueble import Inmueble

class Edificio(Inmueble):

    def __init__(self, direccion, superficie, garage, costo, color, pisos, ascensor):
        super().__init__(direccion, superficie, garage, costo, color)
        self.pisos = pisos
        self.ascensor = ascensor

    #getters y setters

    def setPisos(self, pisos):
        self.pisos = pisos

    def getPisos(self):
        return self.pisos
    
    def setAscensor(self, ascensor):
        self.ascensor = ascensor
    
    def getAscensor(self):
        return self.ascensor        
        

    #Metodos

    def seleccionarPiso(self, piso):
        print("\n >> Piso seleccionado: " + str(piso))

    def getInfo(self):
        info = "\n\n----------------Información Edificio---------------"
        info += "\n Dirección: " + self.getDireccion()
        info += "\n Superficie: " + self.getSuperficie()
        info += "\n Garage: " + self.getGarage()
        info += "\n Costo: " + str(self.getCosto())
        info += "\n Color: " + str(self.getColor())
        info += "\n Pisos: " + str(self.getPisos())
        info += "\n Ascensor: " + self.getAscensor()

        return info