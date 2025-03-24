import dash_bootstrap_components
from dash import dcc, html
from utils import create_description_card, create_display_layout


def create_control_card():
    return html.Div(
        id="control-card",
        children=[
            html.Hr(),
            html.Div(
                children=[html.Button(id="pattern-btn", children="Run", n_clicks=0)],
                style={"textAlign": "center"},
            ),
            # create_modal(
            #     modal_id="pattern_exception_modal",
            #     header="An Exception Occurred",
            #     content="An exception occurred. Please click OK to continue.",
            #     content_id="pattern_exception_modal_content",
            #     button_id="pattern_exception_modal_close",
            # ),
        ],
    )
def create_anomaly_detection_layout():
    return dash_bootstrap_components.Row(
        [
            dash_bootstrap_components.Col(
                html.Div(
                    [
                        create_description_card(),
                        create_control_card(),
                        html.Div(
                            ["initial child"],
                            id="output-clientside",
                            style={"display": "none"},
                        ),
                    ]
                ),
                width=2,
            ),
            dash_bootstrap_components.Col(
                [
                    dash_bootstrap_components.Row(
                        [
                            dash_bootstrap_components.Col(
                                dash_bootstrap_components.Card(
                                    dash_bootstrap_components.CardBody(
                                        [
                                            html.H4("Summary"),
                                            html.Div(
                                                id="anomaly-summary"
                                            ),  # Add log AD summary
                                        ]
                                    )
                                ),
                                width=4,
                            ),
                            dash_bootstrap_components.Col(
                                dash_bootstrap_components.Card(
                                    dash_bootstrap_components.CardBody(
                                        [
                                            html.H4("Attributes"),
                                            html.Div(id="anomaly-attribute-options"),
                                        ]
                                    )
                                ),
                                width=8,
                            ),
                        ]
                    ),
                    create_display_layout(),
                ]
            ),
        ],
    )


layout = create_anomaly_detection_layout()
