from mundoPC.monitor import Monitor
from mundoPC.raton import Raton
from mundoPC.teclado import Teclado


class Computadora:
    contadorComputadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadora += 1
        self._idComputadora = Computadora.contadorComputadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton


    def __str__(self):
        return f''' 
         {self._nombre}: {self._idComputadora}
         Monitor: {self._monitor}
         Teclado: {self._teclado}
         Raton: {self._raton}        
          '''

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 =Monitor('HP', 15)
    computadora1 = Computadora('HP', monitor1, teclado1,raton1)
    print(computadora1)
    teclado2=Teclado('Acer', 'Bluetooth')
    raton2 = Raton('Acer', 'Bluetooth')
    monitor2 = Monitor('Acer', 27)
    computadora2 = Computadora('HP', monitor2, teclado2,raton2)
    print(computadora2)