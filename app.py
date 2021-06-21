import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(
    external_stylesheets=[dbc.themes.SOLAR]
)

content = html.Div(
    [
        html.H1('Welcome!'),
        html.P('Blablabla'),
        dbc.Alert('Data Engineering Module')
    ]
)
app.layout = content

if __name__ == "__main__":
    app.run_server(app.run_server(host='0.0.0.0', port=8050, debug=True))