from Edificio import Edificio
from Casa import Casa

edificio = Edificio("Guayaquil", "1000 m2", "Si", 500, "blanco", 10, "Si")
print(edificio.getInfo())
edificio.pagarArriendo()
edificio.pintar()
edificio.seleccionarPiso(2)
print("\n 1er tipo objeto = " + str(type(edificio)))

casa = Casa("Guayaquil", "200 m2", "Si", 200, "marron", "Ciudad Celeste", "Si")
print(casa.getInfo())
casa.pagarArriendo()
casa.pintar()
casa.limpieza()
print("\n 2do tipo objeto = " + str(type(casa)))
