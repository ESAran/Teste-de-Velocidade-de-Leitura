from calculadora import Calculadora


if __name__ == '__main__':
    ppm = Calculadora.ppm(400, 121)
    print(Calculadora.tempo_leitura_pag_ppm(ppm))

    print(Calculadora.tempo_pagina(300, 10, 15, 'm'))