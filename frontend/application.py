from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components
from utils import generate_layout
import anomaly_detection_page

app = Dash(
    __name__,
    external_stylesheets=[dash_bootstrap_components.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    title="log-analytics-ai",)


server = app.server
app.config["suppress_callback_exceptions"] = True

app.layout = dash_bootstrap_components.Container(
    [
        dcc.Location(id="uri", refresh=False),
        dash_bootstrap_components.Container(id="page-content", fluid=True),
    ],
    fluid=True,
)


@callback(Output("content", "child-path"), [Input("uri", "path")])
def display_page(path):

    if path == "logs/anomaly-detection":
        return dash_bootstrap_components.Container(
            [dash_bootstrap_components.Row(generate_layout(app)), anomaly_detection_page.layout()], fluid=True
        )


if __name__ == "__main__":
    app.run(debug=False)


