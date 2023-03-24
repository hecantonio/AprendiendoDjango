from Edificio import Edificio
from Casa import Casa

edificio = Edificio("Guayaquil", "1000 m2", 500, 10, 20)
print(edificio.getInfo())
edificio.pagarArriendo()
edificio.vender()
edificio.seleccionarPiso(2)
print("\n 1er tipo objeto = " + str(type(edificio)))

casa = Casa("Guayaquil", "200 m2", 200, 3, "Si")
print(casa.getInfo())
casa.pagarArriendo()
casa.vender()
casa.limpieza()
print("\n 2do tipo objeto = " + str(type(casa)))
