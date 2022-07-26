class Orden:
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self.idOrdene = Orden.contadorOrdenes
        self._computadoras =computadoras


    def agregarComputadora (self, nuevaComputadora):
        self._computadoras.append(nuevaComputadora)

    def __str__(self):
        computadoras_str = ''

        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f'''
            Orden: {self.idOrdene}
            Computadoras: {computadoras_str}
        '''

