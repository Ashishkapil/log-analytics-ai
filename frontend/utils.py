import dash_bootstrap_components
from dash import dcc, html, dash_table


def generate_layout(app):
    return html.Div(
        id="banner",
        className="banner",
        children=[
            # html.Img(src=app.get_asset_url("logai_logo.jpg")),
            html.Plaintext("Ashish"),
        ],
    )


def create_description_card():
    return html.Div(
        id="description-card",
        children=[
            html.H4("AI-based Log Analysis"),
            html.Div([create_menu()]),
            html.Div(id="introduction", children="  "),
        ],
    )



def create_display_layout():
    return html.Div(
        id="result_table_card_anomaly",
        children=[
            html.B("Timeseries"),
            html.Hr(),
            dash_bootstrap_components.Card(
                dash_bootstrap_components.CardBody(
                    [
                        dcc.Loading(
                            id="loading-timechart",
                            children=[dash_bootstrap_components.Row(dcc.Graph(id="time_chart"))],
                            type="default",
                        )
                    ],
                    style={"marginTop": 0, "marginBottom": 0},
                ),
            ),
            html.B("Anomalies"),
            html.Hr(),
            dash_bootstrap_components.Card(
                dash_bootstrap_components.CardBody(
                    [
                        dcc.Loading(
                            id="loading-anomaly-table",
                            children=[html.Div(id="anomaly-table")],
                            type="default",
                        )
                    ]
                ),
            ),
        ],
    )


def create_menu():
    menu = html.Div(
        [
            dash_bootstrap_components.Row(
                dcc.Link(
                    "Anomaly Detection",
                    href="/logai/anomaly",
                    className="tab second",
                    style={"font-weight": "bold", "text-decoration": "underline"},
                )
            ),
        ],
    )
    return menu
