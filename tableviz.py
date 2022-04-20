from dash import Dash, dash_table
import pandas as pd
import html
from dash import dcc
from dash import Dash, dcc, html


# df= pd.read_csv("Diff100.csv")

app = Dash(__name__)

server = app.server 


# app.layout = dash_table.DataTable(
#     data=df.to_dict('records'),
#     sort_action='native',
#     columns=[{'id': c, 'name': c} for c in ['जिल्ला','पालिका','विजयी-दल','दोस्रो-दल','मतान्तर']],
#     editable=True,
#     style_data_conditional=[
#         {
#             'if': {
#                 'filter_query': '{विजयी-दल} = "नेकपा एमाले"',
#                 'column_id': 'विजयी-दल',
#             },
#             'backgroundColor': '#FF5C5C',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{दोस्रो-दल} = "नेकपा एमाले"',
#                 'column_id': 'दोस्रो-दल',
#             },
#             'backgroundColor': '#FF5C5C',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{विजयी-दल} = "नेपाली काँग्रेस"',
#                 'column_id': 'विजयी-दल',
#             },
#             'backgroundColor': '#5DB56B',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{दोस्रो-दल} = "नेपाली काँग्रेस"',
#                 'column_id': 'दोस्रो-दल',
#             },
#             'backgroundColor': '#5DB56B',
#             'color': 'white'
#         },
#        {
#             'if': {
#                 'filter_query': '{विजयी-दल} = "माओवादी केन्द्र"',
#                 'column_id': 'विजयी-दल',
#             },
#             'backgroundColor': '#A32D2D',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{दोस्रो-दल} = "माओवादी केन्द्र"',
#                 'column_id': 'दोस्रो-दल',
#             },
#             'backgroundColor': '#A32D2D',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{विजयी-दल} = "माओवादी केन्द्र"',
#                 'column_id': 'विजयी-दल',
#             },
#             'backgroundColor': '#A32D2D',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{दोस्रो-दल} = "माओवादी केन्द्र"',
#                 'column_id': 'दोस्रो-दल',
#             },
#             'backgroundColor': '#A32D2D',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{विजयी-दल} = "स्वतन्त्र"',
#                 'column_id': 'विजयी-दल',
#             },
#             'backgroundColor': '#2CD9FF',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{दोस्रो-दल} = "स्वतन्त्र"',
#                 'column_id': 'दोस्रो-दल',
#             },
#             'backgroundColor': '#2CD9FF',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{दोस्रो-दल} = "राप्रपा नेपाल"',
#                 'column_id': 'दोस्रो-दल',
#             },
#             'backgroundColor': '#A284F9',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{दोस्रो-दल} = "लोकतान्त्रिक फोरम"',
#                 'column_id': 'दोस्रो-दल',
#             },
#             'backgroundColor': '#ea8720',
#             'color': 'white'
#         },
#         {
#             'if': {
#                 'filter_query': '{विजयी-दल} = "संघीय फोरम"',
#                 'column_id': 'विजयी-दल',
#             },
#             'backgroundColor': '#D4E2F8',
            
#         },
#         {
#             'if': {
#                 'filter_query': '{दोस्रो-दल} = "संघीय फोरम"',
#                 'column_id': 'दोस्रो-दल',
#             },
#             'backgroundColor': '#D4E2F8',
            
#         },
#         {
#             'if': {
#                 'filter_query': '{विजयी-दल} = "राष्ट्रिय जनता पार्टी"',
#                 'column_id': 'विजयी-दल',
#             },
#             'backgroundColor': '#D4E2F8',
            
#         },
#         {
#             'if': {
#                 'filter_query': '{विजयी-दल} = "राष्ट्रिय जनता पार्टी"',
#                 'column_id': 'दोस्रो-दल',
#             },
#             'backgroundColor': '#D4E2F8',
#         },
#         {
#             'if': {
#                 'filter_query': '{दोस्रो-दल} = "नयाँ शक्ति पार्टी"',
#                 'column_id': 'दोस्रो-दल',
#             },
#             'backgroundColor': '#e064a7',
#             'color': 'white'
#         }
#     ],
#     tooltip_data=[{
#         'विजयी-दल': {'value': row['Conc1'], 'type': 'markdown'},
#         'दोस्रो-दल': {'value': row['Conc2'], 'type': 'markdown'},
#     } for row in df.to_dict('records')],
#     style_data={
#         'height': 'auto',
#         # all three widths are needed
#     }, fill_width=False    
# )

# # buffer = io.StringIO()

# # html_bytes = buffer.getvalue().encode()
# # encoded = b64encode(html_bytes).decode()


app.layout = html.Div([
    html.H4('Simple plot export options'),
    html.P("↓↓↓ try downloading the plot as PNG ↓↓↓", style={"text-align": "right", "font-weight": "bold"}),
    # dcc.Graph(id="graph", figure=dash_table),
    # html.A(
    #     html.Button("Download as HTML"), 
    #     id="download",
    #     href="data:text/html;base64," + encoded,
    #     download="plotly_graph.html"
    # )
])

if __name__ == '__main__':
    app.run_server(debug=True)
