import pandas as pd

#Ajusta a modalidade
def tratar_modalidade(valor):
    partes = str(valor).split(" - ", 2)

    if len(partes) == 3:
        nome = partes[2].strip()

        if nome:
            return nome

    return "RENEGOCIACAO"

def carregar_dados(caminho):
    df = pd.read_excel(caminho)

    # Para eliminar valores duplicados
    df = df[
        df["Faixa de Valor"] == "a. Todos"
        ].copy()

    # Remove colunas que não serão utilizadas
    df = df.drop(
        columns=[
            "Prefixo",
            "Tipo da Carteira",
            "Dependência",
            "UF",
            "Carteira",
            "Faixa de Valor",
            "Prefixo.1",
            "Contatado",
            "Cultura",
            "Produto"
        ]
    )

    # Colunas usadas
    df = df.rename(columns={
        "MCI": "mci",
        "Contrato": "contrato",
        "Prorrogada": "prorrogado",
        "Item": "item",
        "Valor": "valor",
        "Data": "data",
        "Saldo": "saldo",
        "Contatado": "contatado",
        "Garantia": "garantia",
        "Modalidade": "modalidade",
        "Produto": "produto"
    })

    df["modalidade"] = df["modalidade"].apply(tratar_modalidade)

    # Converte data
    df["data"] = pd.to_datetime(df["data"])

    # Cria coluna de mês
    df["mes"] = df["data"].dt.to_period("M").astype(str)

    # Normaliza prorrogado: 1=true nan=false
    df["prorrogado"] = df["prorrogado"].fillna(0).astype(bool)

    return df