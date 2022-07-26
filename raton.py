from mundoPC.dispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contadorRaton = 0

    def __init__(self,marca, tipoEntrada):
        Raton.contadorRaton += 1
        self._idRaton = Raton.contadorRaton
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f'ID: {self._idRaton}, Marca: {self._marca}, Tipo Entrada: {self._tipoEntrada}'


if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1)
    raton2 = Raton('Acer','Bluetooth')
    print(raton2)