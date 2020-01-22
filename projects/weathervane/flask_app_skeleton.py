from flask import Flask
import query_suite

import io
import random
from flask import Response, render_template, request, redirect
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import query_suite
import datetime

app = Flask(__name__)

metric = 'temperature'
date = datetime.datetime.today()

@app.route('/')
def chart_loader(date, metric):
    #pass date here
    start_time = str(datetime.datetime.combine(
        datetime.datetime.today(), datetime.time.min).timestamp())
    #pass date here
    end_time = str(datetime.datetime.now().timestamp())

    print('\n\n grab_from_actual  \n\n')
    #pass metric here
    actual_data = query_suite.grab_from_actual(
        start_time, end_time, ['time', 'temperature'])
        #pass metric here
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

    formatted_data = {"actual": formatted_actual_data, "predictive": formatted_predictive_data}

    return render_template('index.html', actual_data = formatted_actual_data, predictive_data = formatted_predictive_data)

@app.route('/update', methods=['POST'])
def update_chart():
    date = request.form['date']
    metric_name = request.form['metric_name']
    # return str(date + ' ' +  metric_name)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)
