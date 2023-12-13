import pdfplumber
import text
import nome_arquivo

def Titulo(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file):
        row = text.Pegar_texto(num_page)
        
        titulos = row[2].split()
        obj_titulo = {
            "Nr_Nota": titulos[0],
            "Folha": titulos[1],
            "Data_pregao": titulos[2]
        }   
        return obj_titulo 

def Corretora(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file):
        row = text.Pegar_texto(num_page)
        
        info_corretora1 = row[4].split()
        ino_corretora2 = row[5].split()
        endereco = ''
        total = 0
        while total <= len(ino_corretora2) - 4:
            endereco += f" {ino_corretora2[total]}"
            total += 1
            
        dados_corretora1 = row[6].split()
        dados_corretora2 = row[7].split()
        
        obj_corretora = {
            "Corretora": f"{info_corretora1[0]} {info_corretora1[1]} {info_corretora1[2]}",
            "Telefone_corretora": f"{info_corretora1[-3]} {info_corretora1[-2]}",
            "CNPJ": info_corretora1[-1],
            "Endereco_corretora": endereco,
            "Internet": dados_corretora1[1],
            "email": dados_corretora1[3],
            "Numero_da_corretora": dados_corretora1[4],
            "Telefone_Ouvidoria": dados_corretora2[2],
            "email_Ouvidoria": dados_corretora2[5]
        }
        return obj_corretora

def Cliente(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        coluna_cliente = page.crop((20, 150, page.width, 200))
        
        cliente_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [160, 170, 181, 194],
            "explicit_vertical_lines": [22, 470, 575]
        }
        cliente_dados = coluna_cliente.extract_table(cliente_settings)
        obj_cliente = {
            "Cliente": cliente_dados[0][0],
            "Endereco_cliente": f"{cliente_dados[1][0]} {cliente_dados[2][0]}",
            "CNPJ_ou_CPF": cliente_dados[0][2],
            "Codigo_do_cliente": cliente_dados[2][2]
        }
        return obj_cliente