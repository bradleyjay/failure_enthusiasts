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
def hello():
    # unpack dict object here
    ####

    # save data to variable, pass to js
    retrieved_data = [[0,1], [1,4],[2,2],[4,0]]
    return render_template('index.html', retrieved_data = retrieved_data)


# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)


@app.route('/weather_compare')
def weather_compare():
    query_suite.compare_today_fake()
    return query_suite.compare_today_fake()

# testing


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    start_time = str(datetime.datetime.combine(
        datetime.datetime.today(), datetime.time.min).timestamp())

    end_time = str(datetime.datetime.now().timestamp())

    print('\n\n grab_from_actual  \n\n')
    data = query_suite.grab_from_actual(
        start_time, end_time, ['time', 'temperature'])

    # for i in range(0, 3):
    # bracket because without anything, returns generator. Brackets
    # returns a list!

    # plt.semilogx(C_s, [score[i] for score in score_array])

    xs = [float(datapair[0]) for datapair in data['actual_data']]
    ys = [float(datapair[1]) for datapair in data['actual_data']]

    # if we can't prove the data is clean, would have to...
    # for datapair in data['actual_data']:
    #     axis.plot(datapair[0], datapair[1])

    axis.plot(xs, ys)
    return fig


if __name__ == '__main__':
    app.run()
