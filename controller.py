from model import InputForm
from flask import Markup
from flask import Flask, render_template, request, json
from collectdata import kickoff
from logic import compute1
from compute import compute
from datetime import time
#import sys

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showForm', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        kickoff(form.StartF.data, form.StopF.data,
                         form.Offset.data, form.Gain.data)

        # result = compute(form.StartF.data, form.StopF.data,
        #                  form.Offset.data, form.Gain.data)
        result = None
    else:
        result = None
    #print form, dir(form)
    #print form.keys()
    for f in form:
        print f.id
        #print f.name
        #print f.label
    return render_template('view_plain.html',
                           form=form, result=result)

@app.route("/showgraph")
    #, methods = ['GET', 'POST'])
def chart():
    #if request.method == 'POST':
        values = compute1()
        labels= ["10Hz","20Hz","March","April","May","June","July","August"]
        #values = [10,9,8,7,6,4,7,8]
        return render_template('chart.html', values = values, labels=labels)

if __name__ == '__main__':
   app.run(debug=True)