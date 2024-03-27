class Calculadora():
    
    def ppm(tempo_leitura: int, palavras : int):
        ppm = float(tempo_leitura) / palavras
        ppm = int(round((ppm * 60), 0))

        return ppm
    