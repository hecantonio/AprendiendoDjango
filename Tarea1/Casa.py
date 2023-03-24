from Inmueble import Inmueble

class Casa(Inmueble):

    def __init__(self, direccion, superficie, costo, cantDormitorios, patio):
        super().__init__(direccion, superficie, costo)
        self.cantDormitorios = cantDormitorios
        self.patio = patio

    #getters y setters

    def setCantDormitorios(self, cantDormitorios):
        self.cantDormitorios = cantDormitorios
    
    def getCantDormitorios(self):
        return self.cantDormitorios

    def setPatio(self, patio):
        self.patio = patio

    def getPatio(self):
        return self.patio
    

    #Metodos

    def limpieza(self):
        print("\n >> Limpieza de casa...")
    
    def getInfo(self):
        info = "\n\n----------------Información Casa---------------"
        info += "\n Dirección: " + self.getDireccion()
        info += "\n Superficie: " + self.getSuperficie()
        info += "\n Costo: " + str(self.getCosto())
        info += "\n Cantidad dormitorios: " + str(self.getCantDormitorios())
        info += "\n Patio: " + self.getPatio()

        return info