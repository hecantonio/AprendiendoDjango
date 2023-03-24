class Inmueble:

    def __init__(self, direccion, superficie, costo):
        self.direccion = direccion
        self.superficie = superficie
        self.costo = costo

    #getters y setters

    
    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion
        
    def setSuperficie(self, superficie):
        self.superficie = superficie

    def getSuperficie(self):
        return self.superficie
    
    def setCosto(self, costo):
        self.costo = costo
    
    def getCosto(self):
        return self.costo
    
    def pagarArriendo(self):
        print("\n >> Pagando arriendo: " + str(self.costo))

    def vender(self):
        print("\n >> Vendida por el precio de : " + str(self.costo))