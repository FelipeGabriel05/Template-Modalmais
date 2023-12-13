import text
import negocios
import resumo
import titulo

def Main():
    total_page = text.Total_paginas()
    num_page = 0
    page = 1
    extract = {}
    while num_page < total_page:
        Template_Modalmais = {
            "Titulo da Nota": titulo.Titulo(num_page),
            "Corretora": titulo.Corretora(num_page),
            "Cliente": titulo.Cliente(num_page),
            "Negocios Realizados": negocios.Negocios(num_page),
            "Resumo": resumo.Resumo(num_page)
        }
        extract[f"Pagina_{page}"] = Template_Modalmais
        num_page += 1
        page += 1

    return extract

if __name__ == '__main__':
    Main()
