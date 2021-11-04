import dash
from dash import html
from dash import dcc
import plotly.express as px

data = px.data.iris()
data.head()

fig = px.scatter(data, 'sepal_length', 'sepal_width')

app = dash.Dash()

app.layout = html.Div([dcc.Graph(id='fig', figure=fig),
                     dcc.Dropdown(id='drop', value=1, options=[{'label':i, 'value':i} for i in [1,2,3]])])


@app.callback(dash.dependencies.Output('fig', 'figure'), 
              dash.dependencies.Input('drop', 'value'))
def update(value):
    return px.scatter(data[data['species_id']==value], 'sepal_length', 'sepal_width')


app.run_server(host="0.0.0.0", port=9000)


