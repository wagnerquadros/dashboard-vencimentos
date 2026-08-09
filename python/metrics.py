import pandas as pd

MESES_PT = {
    1: "Jan",
    2: "Fev",
    3: "Mar",
    4: "Abr",
    5: "Mai",
    6: "Jun",
    7: "Jul",
    8: "Ago",
    9: "Set",
    10: "Out",
    11: "Nov",
    12: "Dez"
}


def calcular_indicadores(df):
    total_vencimentos = df["valor"].sum()
    saldo_devedor = df["saldo"].sum()
    nr_clientes = df["mci"].nunique()

    nr_prorrogados = df["prorrogado"].sum()
    nr_normais = len(df) - nr_prorrogados

    valor_prorrogados = df.loc[
        df["prorrogado"],
        "valor"
    ].sum()

    valor_normais = df.loc[
        ~df["prorrogado"],
        "valor"
    ].sum()

    total_contratos = len(df)

    pct_prorrogados = nr_prorrogados / total_contratos * 100
    pct_normais = nr_normais / total_contratos * 100

    return {
        "total_vencimentos": total_vencimentos,
        "saldo_devedor": saldo_devedor,
        "nr_clientes": nr_clientes,
        "nr_prorrogados": nr_prorrogados,
        "nr_normais": nr_normais,
        "valor_prorrogados": valor_prorrogados,
        "valor_normais": valor_normais,
        "pct_prorrogados": pct_prorrogados,
        "pct_normais": pct_normais
    }

def calcular_vencimentos_por_mes(df):
    vencimentos_por_mes = (
        df.groupby("mes")["valor"]
        .sum()
        .reset_index()
    )

    vencimentos_por_mes["mes_label"] = (
        pd.to_datetime(
            vencimentos_por_mes["mes"] + "-01"
        )
        .apply(
            lambda data:
            f"{MESES_PT[data.month]}/{str(data.year)[2:]}"
        )
    )

    return vencimentos_por_mes

def calcular_top_clientes(df, limite=10):
    top_clientes = (
        df.groupby("mci")["valor"]
        .sum()
        .reset_index()
        .sort_values("valor", ascending=False)
        .head(limite)
    )

    top_clientes["mci"] = top_clientes["mci"].astype(str)

    return top_clientes