import pdfplumber
import nome_arquivo

def Resumo(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        coluna_inferior = page.crop((10, 540, page.width, 645))

        table_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "text",
            "explicit_vertical_lines": [44, 57, 128, 148, 220, 
                     236, 246, 276, 371, 466, 576],
            "explicit_horizontal_lines": [560, 570, 580, 590, 608, 620, 630]
        }
        resumo = coluna_inferior.extract_table(table_settings)
        obj_resumo = {
            "Vendas_disponivel": resumo[2][2],
            "Compra_disponivel": resumo[2][6],
            "Venda_opcoes": resumo[2][7],
            "Compra_opcoes": resumo[2][8],
            "Valor_dos_negocios": resumo[2][9],
            "IRRF": resumo[6][2],
            "IRRF_day_trade": resumo[6][6],
            "Taxa_operacional": resumo[6][7],
            "Taxa_registro_BMF": resumo[6][8],
            "Taxa_BMF": resumo[6][9],
            "Outros_Custos": resumo[10][4],
            "ISS": resumo[10][6],
            "Ajuste_de_posicao": resumo[10][7],
            "Ajuste_Day_Trade": resumo[10][8],
            "Total_das_despesas": resumo[10][9],
            "Outros": resumo[13][0],
            "IRRF_Corretagem": resumo[13][2],
            "Total_Conta_Investimento": resumo[13][6],
            "Total_Conta_Normal": resumo[13][7],
            "Total_liquido": resumo[13][8],
            "Total_liquido_da_nota": resumo[13][9],
        }
        
        return obj_resumo
