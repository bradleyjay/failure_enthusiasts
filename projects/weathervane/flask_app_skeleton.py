from flask import Flask
import query_suite

import io
import random
from flask import Response, render_template, request, redirect
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import query_suite
import datetime
import time

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def chart_loader():
    if request.method == 'POST':
        string_date = request.form['date']
        pattern = '%Y-%m-%d'
        date = int(time.mktime(time.strptime(string_date, pattern)))
        metric = request.form['metric_name']
    else:
        metric = 'temperature'
        date = datetime.datetime.combine(datetime.datetime.today(), datetime.time.min).timestamp()

    #pass date here
    start_time = str(date)

    end_epoch = date + 68400
    #pass date here
    end_time = str(end_epoch)
    #pass metric here
    actual_data = query_suite.grab_from_actual(
        start_time, end_time, ['time', metric])
        #pass metric here
    predictive_data = query_suite.grab_from_predictive(
        start_time, end_time, ['time', metric])

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
    print("metric")
    print(metric)
    print("formatted data")
    print(formatted_data)

    return render_template('index.html', actual_data = formatted_actual_data, predictive_data = formatted_predictive_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)
