class Coche:

    color = "azul"
    marca = "mazda"
    modelo = ""
    velocidad = 20

    def __init__(self, color, marca, modelo, velocidad):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color