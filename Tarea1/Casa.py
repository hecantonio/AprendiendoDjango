from Inmueble import Inmueble

class Casa(Inmueble):

    def __init__(self, direccion, superficie, garage, costo, color, urbanizacion, patio):
        super().__init__(direccion, superficie, garage, costo, color)
        self.urbanizacion = urbanizacion
        self.patio = patio

    #getters y setters

    def setUrbanizacion(self, urbanizacion):
        self.urbanizacion = urbanizacion
    
    def getUrbanizacion(self):
        return self.urbanizacion

    def setPatio(self, patio):
        self.patio = patio

    def getPatio(self):
        return self.patio
    

    #Metodos
    
    def getInfo(self):
        info = "----------------Información Casa---------------"
        info += "\n Dirección: " + self.getDireccion()
        info += "\n Superficie: " + self.getSuperficie()
        info += "\n Garage: " + self.getGarage()
        info += "\n Costo: " + str(self.getCosto())
        info += "\n Urbanización: " + self.getUrbanizacion()
        info += "\n Patio: " + self.getPatio()

        return info