import streamlit as st


def aplicar_estilos():
    st.markdown("""
    <style>

    /* Fundo geral da aplicação */
    .stApp {
        background-color: #f4f7f7;
    }

    /* Espaçamento principal */
    .block-container {
        padding-top: 3.5rem;
        padding-bottom: 2rem;
    }

    /* Cabeçalho principal */
    .dashboard-header {
        background: linear-gradient(
            90deg,
            #0a4f6c,
            #116f8e,
            #2ba8c7
        );

        border-bottom: 4px solid #f2c400;

        padding: 24px 30px;
        margin: 0 0 28px 0;

        color: white;

        font-size: 28px;
        font-weight: 700;

        border-radius: 0;
    }

    /* Cards dos indicadores */
    [data-testid="stMetric"] {
        background-color: white;

        border: 1px solid #d9e2e3;
        border-radius: 8px;

        padding: 18px 20px;

        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.06);
    }

    /* Nome do indicador */
    [data-testid="stMetricLabel"] {
        font-size: 13px;
        text-transform: uppercase;
        color: #637277;
    }

    /* Valor do indicador */
    [data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: 700;
        color: #074d6b;
    }

    /* Títulos das seções */
    h3 {
        color: #43575c;

        font-size: 16px !important;
        font-weight: 700 !important;

        text-transform: uppercase;
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        font-weight: 600;
    }

    /* Tab selecionada */
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #07506d;
    }

    </style>
    """, unsafe_allow_html=True)


def exibir_cabecalho():
    st.html("""
    <div class="dashboard-header">
        Carteira Clientes Agro
    </div>
    """)