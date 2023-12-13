import nome_arquivo
import pdfplumber

def Pegar_texto(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        return row

def Total_paginas():
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        total = len(pdf.pages)
        return total