class Inmueble:

    def __init__(self, direccion, superficie, garage, costo, color):
        self.direccion = direccion
        self.superficie = superficie
        self.garage = garage
        self.costo = costo
        self.color = color

    #getters y setters

    
    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion
        
    def setSuperficie(self, superficie):
        self.superficie = superficie

    def getSuperficie(self):
        return self.superficie
    
    def setGarage(self, garage):
        self.garage = garage
    
    def getGarage(self):
        return self.garage

    def setCosto(self, costo):
        self.costo = costo
    
    def getCosto(self):
        return self.costo
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def pagarArriendo(self):
        print("Pagando arriendo: " + str(self.costo))

    def pintar(self):
        print("Pintar de color: " + self.color)