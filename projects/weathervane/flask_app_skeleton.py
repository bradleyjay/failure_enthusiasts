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

    actual_data = query_suite.grab_from_actual(
        start_time, end_time, ['time', 'temperature'])

    predictive_data = query_suite.grab_from_predictive(
        start_time, end_time, ['time', 'temperature'])
    print('Predictive!')
    print(predictive_data)

    # unpack from dict (JS can't use it) -> list of lists. save data to variable, pass to js

    formatted_actual_data = []
    formatted_predictive_data = []

    for data in actual_data['actual_data']:
        formatted_actual_data.append({"time": float(data[0]), "temperature": float(data[1])})

    for data in predictive_data['predictive_data']:
        formatted_predictive_data.append({"time": float(data[0]), "temperature": float(data[1])})

    # sort each dataset by the "time" attribute
    formatted_actual_data = sorted(formatted_actual_data, key=lambda x: (x['time']))

    formatted_predictive_data = sorted(formatted_predictive_data, key=lambda x: (x['time']))

    print('\n\n sorted predictive data:')
    print(formatted_predictive_data)

    formatted_data = {"actual": formatted_actual_data, "predictive": formatted_predictive_data}

    return render_template('index.html', actual_data = formatted_actual_data, predictive_data = formatted_predictive_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)
