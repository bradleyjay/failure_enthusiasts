from flask import Flask
import query_suite

import io
import random
from flask import Response, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import query_suite
import datetime

app = Flask(__name__)


@app.route('/')
def chart_loader():

    start_time = str(datetime.datetime.combine(
        datetime.datetime.today(), datetime.time.min).timestamp())

    end_time = str(datetime.datetime.now().timestamp())

    print('\n\n grab_from_actual  \n\n')
    data = query_suite.grab_from_actual(
        start_time, end_time, ['time', 'temperature'])

    # save data to variable, pass to js
    
    formatted_actual_data = []
    for actual_dat in data['actual_data']:
        formatted_actual_data.append([float(actual_dat[0]),float(actual_dat[1])])

    # formatted_actual_data = [[0,1], [1,4],[2,2],[4,0]]

    print('\n\n\n This is d:\n')
    print(formatted_actual_data)

    return render_template('index.html', formatted_actual_data = formatted_actual_data)


if __name__ == '__main__':
    app.run()
