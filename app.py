from flask import Flask, render_template, request
import pandas as pd
import pickle

model=pickle.load(open('model.pkl','rb'))
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        inp1=request.form['inp1']
        #   ['Graduate', 'Postgraduate', 'Diploma'] -->

        if inp1=='Diploma':
            v1=0
        elif inp1=='Graduate':
            v1=1
        else:
            v1=2

        v2=int(request.form['inp2'])

        inp3=request.form['inp3']

        if inp3=='Average':
            v3=0
        elif inp3=='Excellent':
            v3=1
        elif inp3=='Good':
            v3=2
        else:
            v3=3

        v4=int(request.form['inp4'])

        inp5=request.form['inp5']

        if inp5=='Finance':
            v5=0
        elif inp5=='HR':
            v5=1
        elif inp5=='IT':
            v5=2
        elif inp5=='Operations':
            v5=3
        elif inp5=='Sales':
            v5=4
        else:
            v5=5

        pred=model.predict([[v1,v2,v3,v4,v5]])

        if pred==0:
            pred_y='No'
        else:
            pred_y='Yes'

        return render_template('result.html',pred=pred_y)

# app.run(debug=True)


