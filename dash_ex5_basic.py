# React programming 最終的值會根據你輸入的值做改變
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

# 最後的layout外觀由這裡決定
app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        # 這裡的輸入的property是initial value，與其的id為my-input
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    # 輸出
    html.Div(id='my-output'),
])

# 裝飾下面的function來改變最終app.layout的結果
@app.callback(
    # component_id 和 component_property 是可以省略的
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}' # 有多少個output這邊就要return多少個值

if __name__ == '__main__':
    app.run_server(debug=True)