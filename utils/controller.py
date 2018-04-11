from model import InputForm
from flask import Flask, render_template, request, json
from collectdata import kickoff
from logic import compute1
from compute import compute
import sys

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

# @app.route('/showForm', methods=['PUT'])
# def result():
#     if request.method == 'PUT':
#         compute1()
#     else:
#         print 'Error'


if __name__ == '__main__':
    app.run(debug=True)