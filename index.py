import dash_html_components as html
import dash_core_components as dcc
import dash.dependencies as dep

# The server is necessary, as gunicorn calls this to start Flask instance
from app import app, server
from home import layout as home_layout
from bamqc.gbovertime import layout as gbovertime_layout
from bcl2fastq.index_summary import layout as index_layout
from rnaseqc.over_time import layout as rnaseqc_overtime_layout
from runreport.proj_hist import layout as runreport_projhist_layout
from runscanner.yield_over_time import layout as runscanner_yield_over_time_layout

app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
])


@app.callback(
    dep.Output('page-content', 'children'), [dep.Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return home_layout
    elif pathname == '/bamqc/gbovertime':
        return gbovertime_layout
    elif pathname == '/bcl2fastq/indexinfo':
        return index_layout
    elif pathname == '/rnaseqc/over_time':
        return rnaseqc_overtime_layout
    elif pathname == '/runreport/proj_hist':
        return runreport_projhist_layout
    elif pathname == '/runscanner/sum_over_time':
        return runscanner_yield_over_time_layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
