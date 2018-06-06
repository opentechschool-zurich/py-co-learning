import dash
import os
from flask import send_from_directory
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dtime
import dash_table_experiments as dte
import datetime as dt
import pandas as pd

app = dash.Dash()

external_css = [
    '/static/dash-docs-base.css'
]
for css in external_css:
    app.css.append_css({"external_url": css})


# Use this if there is no internet connection

# app.css.config.serve_locally = True
# app.scripts.config.serve_locally = True

@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)


app.config['suppress_callback_exceptions'] = True
app.layout = html.Div(className='container', style={'margin': '0 auto'}, children=[
    html.H1('Ibis Hotel Booking'),
    dcc.DatePickerRange(
        id='Dr1',
        clearable=True,
        reopen_calendar_on_clear=True,
        start_date_placeholder_text='Select a date',
        start_date=dtime.today().strftime("%Y-%m-%d"),
        end_date=(dt.date.today()+dt.timedelta(7)).strftime("%Y-%m-%d")
    ),
    html.Div(id='button-div', style={'float':'right'}, children=[
        html.Button(id="button-show", children="Show available rooms", n_clicks=0),
        html.Button(id="button-book", children="Book available rooms", n_clicks=0),
    ]),
    html.Div(id='info'),

    html.Div(id='output', children=[
        dte.DataTable(
        rows=[{}],
        row_selectable=True,
        filterable=False,
        sortable=True,
        selected_row_indices=[],
        id='datatable'
    )

    ])
])


@app.callback(
    Output('datatable', 'rows'),
    [Input('button-show', 'n_clicks')],
state=[State('Dr1', 'start_date'), State('Dr1', 'end_date')])
def show_rooms(n_clicks, start_date, end_date):
    if n_clicks > 0 and start_date and end_date:


        fmt = "%Y-%m-%d"
        s = dt.datetime.strptime(start_date, fmt)
        e = dt.datetime.strptime(end_date, fmt)
        day_count = (e-s).days
        all_dates = [dt.date.today()+dt.timedelta(i) for i in range(day_count)]
        all_dates_str = [x.strftime(fmt) for x in all_dates]

        # input dates into class function, return list of dicts
        d = dict(price=100, beds=2, see_view=True, booked_dates=['date1, date2'], name='Testroom1')
        df = pd.DataFrame(d)
        rows = df.to_dict('records')
        return rows
    else:
        return [{}]


@app.callback(Output('info', 'children'), [Input('button-book', 'n_clicks')], state=[
State('datatable', 'rows'), State('datatable', 'selected_row_indices')
])
def make_booking(n_clicks, rows, inds):
    if n_clicks > 0:
        df = pd.DataFrame(rows)[inds]
        keys = df['id']




if __name__ == '__main__':
    app.run_server(debug=True)
