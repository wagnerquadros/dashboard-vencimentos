import streamlit as st
import pandas as pd

from data import carregar_dados

from metrics import (
    calcular_indicadores,
    calcular_vencimentos_por_mes,
    calcular_top_clientes
)

from charts import (
    criar_grafico_vencimentos,
    criar_grafico_top_clientes,
    criar_grafico_situacao
)

from styles import aplicar_estilos, exibir_cabecalho


# pip install openpyxl
df = carregar_dados("dados/vencimentos.xlsx")

st.set_page_config(
    page_title="Dashboard de Vencimentos",
    page_icon="📊",
    layout="wide"
)

indicadores = calcular_indicadores(df)
vencimentos_por_mes = calcular_vencimentos_por_mes(df)
top_clientes = calcular_top_clientes(df)

aplicar_estilos()
exibir_cabecalho()


tab_visao_geral, tab_cronograma, tab_contratos = st.tabs([
    "Visão Geral",
    "Cronograma por MCI",
    "Todos os Contratos"
])



with tab_visao_geral:

    st.subheader("Resumo da Carteira")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total de Vencimentos",
            value=f"R$ {indicadores['total_vencimentos']:,.2f}"
        )

    with col2:
        st.metric(
            label="Saldo Devedor",
            value=f"R$ {indicadores['saldo_devedor']:,.2f}"
        )

    with col3:
        st.metric(
            label="Contratos Prorrogados",
            value=indicadores["nr_prorrogados"]
        )

    with col4:
        st.metric(
            label="Clientes",
            value=indicadores["nr_clientes"]
        )

    #Gráfico
    st.subheader("Vencimentos por Mês")

    st.write(vencimentos_por_mes)

    fig_vencimentos = criar_grafico_vencimentos(
        vencimentos_por_mes
    )

    st.plotly_chart(
        fig_vencimentos,
        width="stretch",
        config={
            "displayModeBar": False
        }
    )



    st.subheader("Top Clientes por Valor")

    fig_clientes = criar_grafico_top_clientes(
        top_clientes
    )

    st.plotly_chart(
        fig_clientes,
        width="stretch",
        config={
            "displayModeBar": False
        }
    )

    st.subheader("Prorrogados x Normais")

    col_prorrogados, col_normais = st.columns(2)

    with col_prorrogados:
        st.html(
            f"""
            <div style="text-align:center;">
                <div style="font-size:32px; font-weight:700; color:#d54435;">
                    {indicadores['nr_prorrogados']}
                </div>
                <div style="color:#637277;">
                    Prorrogados
                </div>
                <div style="color:#d54435; font-weight:600; margin-top:4px;">
                    R$ {indicadores['valor_prorrogados']:,.0f}
                </div>
            </div>
            """
        )

    with col_normais:
        st.html(
            f"""
            <div style="text-align:center;">
                <div style="font-size:32px; font-weight:700; color:#084f6b;">
                    {indicadores['nr_normais']}
                </div>
                <div style="color:#637277;">
                    Normais
                </div>
                <div style="color:#084f6b; font-weight:600; margin-top:4px;">
                    R$ {indicadores['valor_normais']:,.0f}
                </div>
            </div>
            """
        )

    fig_situacao = criar_grafico_situacao(indicadores)

    st.plotly_chart(
        fig_situacao,
        width="stretch",
        config={
            "displayModeBar": False
        }
    )

with tab_cronograma:

    st.subheader("Cronograma por Cliente")

    mci_busca = st.text_input(
        "Informe o MCI"
    )

    if mci_busca:

        contratos_cliente = df[
            df["mci"].astype(str).str.contains(
                mci_busca,
                case=False,
                na=False
            )
        ]

        if contratos_cliente.empty:

            st.warning(
                "Nenhum contrato encontrado para este MCI."
            )

        else:

            st.success(
                f"{len(contratos_cliente)} contrato(s) encontrado(s)."
            )

            total_parcelas = contratos_cliente["valor"].sum()
            total_saldo = contratos_cliente["saldo"].sum()
            nr_prorrogados = contratos_cliente["prorrogado"].sum()

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    label="Total das Parcelas",
                    value=f"R$ {total_parcelas:,.2f}"
                )

            with col2:
                st.metric(
                    label="Saldo Devedor",
                    value=f"R$ {total_saldo:,.2f}"
                )

            with col3:
                st.metric(
                    label="Prorrogados",
                    value=nr_prorrogados
                )


            tabela_cliente = contratos_cliente.copy()
            tabela_cliente["data"] = pd.to_datetime(tabela_cliente["data"]).dt.strftime("%d-%m-%Y")
            tabela_cliente["prorrogado"] = tabela_cliente["prorrogado"].map({
                True: "Sim",
                False: "Não"
            })

            tabela_cliente = tabela_cliente[
                [
                    "contrato",
                    "data",
                    "item",
                    "valor",
                    "saldo",
                    "prorrogado"
                ]
            ]

            st.dataframe(
                tabela_cliente,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "contrato": "Contrato",
                    "data": "Vencimento",
                    "item": "Finalidade",
                    "valor": st.column_config.NumberColumn(
                        "Valor da Parcela",
                        format="R$ %.2f"
                    ),
                    "saldo": st.column_config.NumberColumn(
                        "Saldo Devedor",
                        format="R$ %.2f"
                    ),
                    "prorrogado": "Prorrogado"
                }
            )


with tab_contratos:

    st.subheader("Todos os Contratos")

    col_filtro1, col_filtro2, col_filtro3, col_filtro4 = st.columns(4)

    with col_filtro1:

        meses_disponiveis = sorted(
            df["data"]
            .dt.to_period("M")
            .astype(str)
            .unique()
            .tolist()
        )

        filtro_mes = st.selectbox(
            "Mês",
            ["Todos"] + meses_disponiveis
        )

    with col_filtro2:
        filtro_prorrogado = st.selectbox(
            "Prorrogado",
            ["Todos", "Sim", "Não"]
        )

    with col_filtro3:
        modalidades = ["Todas"] + sorted(
            df["modalidade"].unique().tolist()
        )

        filtro_modalidade = st.selectbox(
            "Modalidade",
            modalidades
        )

    with col_filtro4:
        mcis = ["Todos"] + sorted(
            df["mci"].astype(str).unique().tolist()
        )

        filtro_mci = st.selectbox(
            "Cliente / MCI",
            mcis
        )

    dados_filtrados = df.copy()

    #Filtro por mês
    if filtro_mes != "Todos":
        dados_filtrados = dados_filtrados[
            dados_filtrados["data"]
            .dt.to_period("M")
            .astype(str) == filtro_mes
            ]

    #Filtro por prorrogado
    if filtro_prorrogado == "Sim":
        dados_filtrados = dados_filtrados[
            dados_filtrados["prorrogado"] == True
        ]

    elif filtro_prorrogado == "Não":
        dados_filtrados = dados_filtrados[
            dados_filtrados["prorrogado"] == False
        ]

    #Filtro por modalidade
    if filtro_modalidade != "Todas":
        dados_filtrados = dados_filtrados[
            dados_filtrados["modalidade"] == filtro_modalidade
            ]

    #Filtro por mci
    if filtro_mci != "Todos":
        dados_filtrados = dados_filtrados[
            dados_filtrados["mci"].astype(str) == filtro_mci
        ]

    dados_filtrados = dados_filtrados.sort_values(
        by="data",
        ascending=True
    )

    #Copia criada para manter o formato data no df original
    tabela_contratos = dados_filtrados.copy()

    tabela_contratos["data"] = (
        tabela_contratos["data"]
        .dt.strftime("%d/%m/%Y")
    )

    st.write(
        f"{len(dados_filtrados)} contrato(s) encontrado(s)."
    )

    st.dataframe(
        tabela_contratos,
        width="stretch",
        hide_index=True
    )

