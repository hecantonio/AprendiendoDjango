from Edificio import Edificio
from Casa import Casa

edificio = Edificio("Guayaquil", "1000 m2", "Si", 500, "blanco", 10, "Si")
print(edificio.getInfo())
edificio.pagarArriendo()
#print("1er objeto" + type(edificio))

casa = Casa("Guayaquil", "200 m2", "Si", 500, "marron", "Ciudad Celeste", "Si")
print(casa.getInfo())
casa.pagarArriendo()
#print("1er objeto" + type(casa))
