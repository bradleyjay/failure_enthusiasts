from flask import Flask, render_template
from render_image import render_static_img
# import query_suite
app = Flask(__name__)

@app.route('/')
def index():
    # call a function which will creates img and then update static download.png
    render_static_img()
    return render_template('index.html')

# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

# @app.route('/weather_compare')
# def weather_compare():
#     query_suite.compare_today_fake()
#     return query_suite.compare_today_fake()

if __name__ == '__main__':
    app.run(debug=True, port='8000')