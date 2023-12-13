import pdfplumber
import nome_arquivo

def Negocios(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        coluna_negocios = page.crop((20, 215, page.width, 530))
        
        negocios_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "text",
            "explicit_vertical_lines": [25, 35, 100, 175, 230, 290, 380, 480, 500, 580]
        }
        negocios = coluna_negocios.extract_table(negocios_settings)
        
        i = 0
        total_negocios = {}
        num_negocios = 1
        while i <= len(negocios) - 1:
            obj_negocio = {
                "C_V": negocios[i][0],
                "Mercadoria": negocios[i][1],
                "Vencimento": negocios[i][2],
                "Quantidade": negocios[i][3],
                "Preco_Ajuste": negocios[i][4],
                "Tipo_do_negocio": negocios[i][5],
                "Vlr_de_Operacao_Ajuste": negocios[i][6],
                "D_C": negocios[i][7],
                "Taxa_Operacional": negocios[i][8]
            }
            total_negocios[f"Negocio_{num_negocios}"] = obj_negocio
            num_negocios += 1
            i += 1
        
        return total_negocios
