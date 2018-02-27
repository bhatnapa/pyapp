from flask import Flask, render_template, request, json
from utils import collectdata

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showForm')
def showForm():
    return render_template('form.html')

@app.route('/submitForm', methods=['POST'])
def submitForm():
    # read the posted values from the UI
    _startFrequency = request.form['startFrequency']
    _stopFrequency = request.form['stopFrequency']
    _offset = request.form['offset']
    _method = request.form['method']

    if _startFrequency and _stopFrequency and _offset and _method:
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})
    # validate the received values
    #collectdata.kickoff(_startFrequency,_stopFrequency,_offset,_method)
    
    collectdata.ctrl_c_handler()

if __name__ == "__main__":
    app.run()
