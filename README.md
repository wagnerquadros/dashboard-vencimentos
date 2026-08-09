# Dashboard de Vencimentos

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Charts-3F4F75?logo=plotly&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)

Dashboard desenvolvido em **Python** para análise e acompanhamento de vencimentos de contratos.

## Objetivo

O projeto tem como objetivo facilitar a visualização e análise de informações como:

- total de vencimentos;
- saldo devedor;
- contratos prorrogados;
- quantidade de clientes;
- vencimentos por mês;
- clientes com maiores valores;
- consulta de contratos por MCI;
- filtros por mês, modalidade e situação do contrato.

## Tecnologias

- Python 3.11
- Pandas
- Streamlit
- Plotly
- OpenPyXL

## Como usar

Clone o repositório:

```bash
git clone https://github.com/wagnerquadros/dashboard-vencimentos.git
```

Entre na pasta:

```bash
cd dashboard-vencimentos
```

Crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install streamlit pandas plotly openpyxl
```

Crie a pasta:

```text
dados/
```

e adicione o arquivo:

```text
vencimentos.xlsx
```

Execute a aplicação:

```powershell
streamlit run python/app.py
```
