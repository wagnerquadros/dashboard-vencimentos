import streamlit as st
import pandas as pd


dados = [
    {
        "mci": "1001",
        "contrato": "C001",
        "data": "2026-08-10",
        "valor": 150000,
        "saldo": 420000,
        "item": "Lavoura de Soja",
        "prorrogado": False
    },
    {
        "mci": "1002",
        "contrato": "C002",
        "data": "2026-08-15",
        "valor": 85000,
        "saldo": 210000,
        "item": "Bovinocultura",
        "prorrogado": True
    },
    {
        "mci": "1001",
        "contrato": "C003",
        "data": "2026-09-10",
        "valor": 60000,
        "saldo": 150000,
        "item": "Máquinas e Equipamentos",
        "prorrogado": False
    },
    {
        "mci": "1003",
        "contrato": "C004",
        "data": "2026-09-20",
        "valor": 95000,
        "saldo": 310000,
        "item": "Lavoura de Arroz",
        "prorrogado": True
    }
]

df = pd.DataFrame(dados)



st.set_page_config(
    page_title="Dashboard de Vencimentos",
    page_icon="📊",
    layout="wide"
)

st.title("Dashboard de Vencimentos")

st.caption("Acompanhamento de vencimentos, contratos e clientes")

tab_visao_geral, tab_cronograma, tab_contratos = st.tabs([
    "Visão Geral",
    "Cronograma por MCI",
    "Todos os Contratos"
])

#Indicadores
total_vencimentos = df["valor"].sum()
saldo_devedor = df["saldo"].sum()
contratos_prorrogados = df["prorrogado"].sum()
nr_clientes = df["mci"].nunique()


with tab_visao_geral:

    st.subheader("Resumo da Carteira")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total de Vencimentos",
            value=f"R$ {total_vencimentos:,.2f}"
        )

    with col2:
        st.metric(
            label="Saldo Devedor",
            value=f"R$ {saldo_devedor:,.2f}"
        )

    with col3:
        st.metric(
            label="Contratos Prorrogados",
            value=contratos_prorrogados
        )

    with col4:
        st.metric(
            label="Clientes",
            value=nr_clientes
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

    st.write(
        "A tabela completa será exibida aqui."
    )


