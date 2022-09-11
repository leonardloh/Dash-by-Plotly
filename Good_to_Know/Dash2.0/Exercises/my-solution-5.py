# If you prefer to run the code online instead of on your computer click:
# https://github.com/Coding-with-Adam/Dash-by-Plotly#execute-code-in-browser

from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytext = dcc.Markdown(children='')
myinput = dbc.Input(value="# Hello World - let's build web apps in Python!")
mybutton = dbc.RadioItems(options=[
    {"label": "Red", "value": 1},
    {"label": "Green", "value": 2},
    {"label": "Blue", "value": 3}])
# Customize your own Layout
app.layout = dbc.Container([mybutton, mytext, myinput])

# Callback allows components to interact
@app.callback(
    Output(mytext, component_property='children'),
    Output(mytext, component_property='style'),
    Input(myinput, component_property='value'),
    Input(mybutton, component_property='value')
)
def update_title(user_input, radio_input):  # function arguments come from the component property of the Input
    if radio_input == 1:
        color = "Red"
    if radio_input == 2:
        color = "Green"
    if radio_input == 3:
        color = "Blue"
    return user_input, {'color': color}  # returned objects are assigned to the component property of the Output


# Run app
if __name__=='__main__':
    app.run_server(port=8052)
