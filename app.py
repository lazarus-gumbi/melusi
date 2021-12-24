import calendar
from flask import Flask, render_template
from datetime import date
import requests
app = Flask(__name__)


@app.route('/')
def hello():
    curr_date = date.today()
    day_name = calendar.day_name[curr_date.weekday()]
    r = requests.get('http://numbersapi.com/random/')
    fact = r.text
    return render_template('index.html',day_name = day_name,fact = fact)

if __name__ == '__main__':
    app.run(debug=True)
