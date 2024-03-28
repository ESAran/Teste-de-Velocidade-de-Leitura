class Calculadora():
    
    def ppm(tempo_leitura: int, palavras : int):
        ppm = float(tempo_leitura) / palavras
        ppm = int(round((ppm * 60), 0))

        return ppm
    
    def tempo_leitura_pag_ppm(ppm):
        # Livros tem em média 300 à 350 palavras por página.
        vel_pag1 = 300/ppm
        vel_pag2 = 350/ppm

        return round(((vel_pag1 + vel_pag2)/2), 1)