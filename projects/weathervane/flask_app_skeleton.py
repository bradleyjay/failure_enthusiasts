from flask import Flask
import query_suite
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/weather_compare')
def weather_compare():
    query_suite.compare_today_fake()
    return query_suite.compare_today_fake()

if __name__ == '__main__':
    app.run()