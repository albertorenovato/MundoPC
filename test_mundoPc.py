from mundoPC.computadora import Computadora
from mundoPC.monitor import Monitor
from mundoPC.orden import Orden
from mundoPC.raton import Raton
from mundoPC.teclado import Teclado

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 =Monitor('HP', 15)
computadora1 = Computadora('HP', monitor1, teclado1,raton1)

teclado2=Teclado('Acer', 'Bluetooth')
raton2 = Raton('Acer', 'Bluetooth')
monitor2 = Monitor('Acer', 27)
computadora2 = Computadora('Acer', monitor2, teclado2,raton2)

teclado3 = Teclado('Gamer', 'Bluetooth')
raton3 = Raton('Gamer', 'Bluetooth')
monitor3 = Monitor ('Gamer', 34)

computadoras1 = [computadora1, computadora2]
orden1 =Orden(computadoras1)
print(orden1)
computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)
orden1.agregarComputadora(computadora3)
print(orden1)

computadoras2 = [computadora1, computadora3]
orden2 = Orden(computadoras2)
print(orden2)