class Calculadora():
    
    def ppm(tempo_leitura: int, palavras : int):
        ppm = float(tempo_leitura) / palavras
        ppm = int(round((ppm * 60), 0))

        return ppm
    
    def tempo_leitura_pag_ppm(ppm):
        '''Calcula o tempo de leitura médio de páginas pelo PPM
        Considerando livros que tenham em média 300 a 350 palavras por página.'''
        # Livros tem em média 300 à 350 palavras por página.
        vel_pag1 = 300/ppm
        vel_pag2 = 350/ppm

        return round(((vel_pag1 + vel_pag2)/2), 1)
    
    def tempo_pagina(livro, qtde_pg, frequencia, periodo):
        '''Retorna quanto tempo será gasto lendo uma quantidade determinada páginas
        por um período e frequência.
        ---
        Período:
        * d - dia
        * s - semana
        * m - mês'''
        totalpg = livro#._paginas
        if (periodo=='s'):
            pg_dia = (qtde_pg*frequencia)/7
        elif (periodo=='m'):
            pg_dia = (qtde_pg*frequencia)/30
        elif (periodo=='d'):
            pg_dia = qtde_pg*frequencia

        return livro/pg_dia