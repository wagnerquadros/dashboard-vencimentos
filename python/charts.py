import plotly.express as px
import plotly.graph_objects as go


def criar_grafico_vencimentos(vencimentos_por_mes):
    fig = px.bar(
        vencimentos_por_mes,
        x="valor",
        y="mes_label",
        orientation="h",
        text="valor"
    )

    fig.update_traces(
        marker_color="#084f6b",
        texttemplate="R$ %{text:,.0f}",
        textposition="inside"
    )

    fig.update_layout(
        height=300,
        margin=dict(
            l=10,
            r=20,
            t=10,
            b=10
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        xaxis=dict(
            visible=False
        ),
        yaxis=dict(
            title=None
        )
    )

    return fig


def criar_grafico_top_clientes(top_clientes):
    fig = px.bar(
        top_clientes,
        x="valor",
        y="mci",
        orientation="h",
        text="valor"
    )

    fig.update_traces(
        marker_color="#084f6b",
        texttemplate="R$ %{text:,.0f}",
        textposition="inside",
        insidetextanchor="end",
        hovertemplate=(
            "<b>MCI: %{y}</b><br>"
            "Valor: R$ %{x:,.2f}"
            "<extra></extra>"
        )
    )

    fig.update_layout(
        height=400,
        margin=dict(
            l=10,
            r=20,
            t=10,
            b=10
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        xaxis=dict(
            visible=False
        ),
        yaxis=dict(
            title=None,
            type="category",
            autorange="reversed"
        ),
        bargap=0.30
    )

    return fig

def criar_grafico_situacao(indicadores):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=["Situação"],
            x=[indicadores["pct_prorrogados"]],
            orientation="h",
            name="Prorrogados",
            marker_color="#d54435",
            text=[f"{indicadores['pct_prorrogados']:.0f}%"],
            textposition="inside",
            hovertemplate=(
                f"<b>Prorrogados</b><br>"
                f"Contratos: {indicadores['nr_prorrogados']}<br>"
                f"Valor: R$ {indicadores['valor_prorrogados']:,.2f}"
                "<extra></extra>"
            )
        )
    )

    fig.add_trace(
        go.Bar(
            y=["Situação"],
            x=[indicadores["pct_normais"]],
            orientation="h",
            name="Normais",
            marker_color="#084f6b",
            text=[f"{indicadores['pct_normais']:.0f}%"],
            textposition="inside",
            hovertemplate=(
                f"<b>Normais</b><br>"
                f"Contratos: {indicadores['nr_normais']}<br>"
                f"Valor: R$ {indicadores['valor_normais']:,.2f}"
                "<extra></extra>"
            )
        )
    )

    fig.update_layout(
        barmode="stack",
        height=150,
        margin=dict(
            l=0,
            r=0,
            t=20,
            b=35
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis=dict(
            visible=False,
            range=[0, 100]
        ),
        yaxis=dict(
            visible=False
        ),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.15,
            xanchor="center",
            x=0.5
        ),
        bargap=0
    )

    return fig