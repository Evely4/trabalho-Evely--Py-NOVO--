import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

df = pd.read_csv('CADASTRO_IES_2020.CSV', encoding='ISO-8859-1', sep=';', low_memory=False)
df.head()

print(df.info())

# Análise exploratória
print("Análise exploratória:")
print("Total de linhas:", len(df))
print("\nResumo estatístico:")
print(df.describe())
print("\nQuantidade de valores NaN por coluna:")
print(df.isna().sum())

"""Primeiro Gráfico"""

print("Estatísticas básicas para 'DOC_EX_SEM_GRAD':")
print(df['DOC_EX_SEM_GRAD'].describe())

print("\nEstatísticas básicas para 'DOC_EX_GRAD':")
print(df['DOC_EX_GRAD'].describe())

plt.figure(figsize=(12, 6))

colunas_graduacao = ['DOC_EX_SEM_GRAD', 'DOC_EX_GRAD']

quantidades = df[colunas_graduacao].sum()

categorias = ['Sem Graduação', 'Com Graduação']

plt.figure(figsize=(8, 6))
plt.bar(categorias, quantidades, color=['blue', 'green'])
plt.xlabel('Categoria de Graduação')
plt.ylabel('Quantidade de Docentes')
plt.title('Quantidade de Docentes por Categoria de Graduação')
plt.savefig('quantidade_doc_por_cat.png')
plt.show()

"""Segundo gráfico"""

df = pd.read_csv('CADASTRO_IES_2020.CSV', encoding='ISO-8859-1', sep=';', low_memory=False)
print(df.columns)

print("Estatísticas básicas para 'DOC_EX_BRA':")
print(df['DOC_EX_BRA'].describe())

print("\nEstatísticas básicas para 'DOC_EX_EST':")
print(df['DOC_EX_EST'].describe())

print("\nEstatísticas básicas para 'DOC_EX_COM_DEFICIÊNCIA':")
print(df['DOC_EX_COM_DEFICIÊNCIA'].describe())

plt.figure(figsize=(12, 6))

categorias = ['DOC_EX_BRA', 'DOC_EX_EST', 'DOC_EX_COM_DEFICIÊNCIA']

valores = df[categorias].sum()

cat_doc = [
    'Brasileiros', 'Estrangeiros', 'PDC'
]

plt.figure(figsize=(10, 6))
plt.bar(categorias, valores, color=['blue', 'green', 'red'])
plt.xlabel('Categoria')
plt.ylabel('Quantidade de Docentes')
plt.title('Distribuição de Docentes por Categoria')
plt.xticks(categorias, cat_doc)
plt.savefig('distribuicao_doc_cat.png')
plt.show()

"""Terceiro gráfico"""

print("Estatísticas básicas para 'DOC_EX_0_29':")
print(df['DOC_EX_0_29'].describe())

print("\nEstatísticas básicas para 'DOC_EX_30_34':")
print(df['DOC_EX_30_34'].describe())

print("\nEstatísticas básicas para 'DOC_EX_35_39':")
print(df['DOC_EX_35_39'].describe())

print("\nEstatísticas básicas para 'DOC_EX_40_44':")
print(df['DOC_EX_40_44'].describe())

print("\nEstatísticas básicas para 'DOC_EX_45_49':")
print(df['DOC_EX_45_49'].describe())

print("\nEstatísticas básicas para 'DOC_EX_50_54':")
print(df['DOC_EX_50_54'].describe())

print("\nEstatísticas básicas para 'DOC_EX_55_59':")
print(df['DOC_EX_55_59'].describe())

print("\nEstatísticas básicas para 'DOC_EX_60_MAIS':")
print(df['DOC_EX_60_MAIS'].describe())

plt.figure(figsize=(12, 6))

colunas_faixa_etaria = ['DOC_EX_0_29', 'DOC_EX_30_34', 'DOC_EX_35_39', 'DOC_EX_40_44', 'DOC_EX_45_49', 'DOC_EX_50_54', 'DOC_EX_55_59', 'DOC_EX_60_MAIS']

quantidades = df[colunas_faixa_etaria].sum()

faixas_etarias = ['0-29 anos', '30-34 anos', '35-39 anos', '40-44 anos', '45-49 anos', '50-54 anos', '55-59 anos', '60+ anos']

plt.figure(figsize=(12, 6))
plt.bar(faixas_etarias, quantidades, color='skyblue')
plt.xlabel('Faixa Etária')
plt.ylabel('Quantidade de Docentes')
plt.title('Quantidade de Docentes por Faixa Etária')
plt.xticks(rotation=45)
plt.savefig('quantidade_doc_faixa_et.png')
plt.show()

"""Quarto gráfico"""

print("Estatísticas básicas para 'DOC_EX_BRANCA':")
print(df['DOC_EX_BRANCA'].describe())

print("\nEstatísticas básicas para 'DOC_EX_PRETA':")
print(df['DOC_EX_PRETA'].describe())

print("\nEstatísticas básicas para 'DOC_EX_PARDA':")
print(df['DOC_EX_PARDA'].describe())

print("\nEstatísticas básicas para 'DOC_EX_AMARELA':")
print(df['DOC_EX_AMARELA'].describe())

print("\nEstatísticas básicas para 'DOC_EX_INDÍGENA':")
print(df['DOC_EX_INDÍGENA'].describe())

print("\nEstatísticas básicas para 'DOC_EX_COR_ND':")
print(df['DOC_EX_COR_ND'].describe())

plt.figure(figsize=(12, 6))

df = pd.read_csv('CADASTRO_IES_2020.CSV', encoding='ISO-8859-1', sep=';', low_memory=False)

colunas_cor = ['DOC_EX_BRANCA', 'DOC_EX_PRETA', 'DOC_EX_PARDA', 'DOC_EX_AMARELA', 'DOC_EX_INDÍGENA', 'DOC_EX_COR_ND']

quantidades = df[colunas_cor].sum()

cores = ['Branca', 'Preta', 'Parda', 'Amarela', 'Indígena', 'Não Declarada']

plt.figure(figsize=(10, 6))
plt.bar(cores, quantidades, color=['blue', 'green', 'red', 'yellow', 'brown', 'gray'])
plt.xlabel('Cor')
plt.ylabel('Quantidade de Docentes')
plt.title('Quantidade de Docentes por Cor')
plt.xticks(rotation=45)
plt.savefig('quantidade_doc_cor.png')
plt.show()


def add_page_with_graph(pdf, graph_path, title, description):
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=title, ln=True, align='C')
    pdf.image(graph_path, x=10, w=190)
    pdf.ln(15)
    pdf.set_font("Arial", size=13)
    pdf.multi_cell(0, 10, txt=description, align='C')
    pdf.ln(10)

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)


pdf.add_page()
pdf.set_font("Arial", size=20, style='B')
pdf.cell(200, 10, txt="Relatório de Análise de Dados dos Docentes", ln=True, align='C')

introduction_text = """
Este relatório apresenta uma análise de dados dos docentes, incluindo informações sobre a quantidade de docentes por categoria de graduação, por faixa etária, por cor e por categoria.
"""

pdf.set_font("Arial", size=14)
pdf.multi_cell(0, 10, txt=introduction_text, align='L')

title1 = "Gráfico 1: Quantidade de Docentes por Categoria de Graduação"
description1 = "Este gráfico mostra a quantidade de docentes divididos em duas categorias: Sem Graduação e Com Graduação."
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt=title1, ln=True, align='C')
pdf.image('quantidade_doc_por_cat.png', x=10, w=190)
pdf.ln(20)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt=description1, align='C')
pdf.ln(20)

title2 = "Gráfico 2: Distribuição de Docentes por Categoria"
description2 = "Este gráfico mostra a distribuição de docentes em três categorias: Brasileiros, Estrangeiros e PDC."
add_page_with_graph(pdf, 'distribuicao_doc_cat.png', title2, description2)

title3 = "Gráfico 3: Quantidade de Docentes por Faixa Etária"
description3 = "Este gráfico apresenta a quantidade de docentes em diferentes faixas etárias."
add_page_with_graph(pdf, 'quantidade_doc_faixa_et.png', title3, description3)

title4 = "Gráfico 4: Quantidade de Docentes por Cor"
description4 = "Este gráfico exibe a quantidade de docentes por cor, incluindo categorias como Branca, Preta, Parda, Amarela, Indígena e Não Declarada."
add_page_with_graph(pdf, 'quantidade_doc_cor.png', title4, description4)

pdf_file_name = "relatorio_docentes.pdf"
pdf.output(pdf_file_name)

print(f"PDF gerado com sucesso: {pdf_file_name}")