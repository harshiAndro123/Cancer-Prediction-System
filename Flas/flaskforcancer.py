import pickle
import os
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open(r'randmf.pkl', 'rb'))  

@app.route('/')  
def home():
    return render_template(r'index.html')

@app.route('/submit', methods=["POST", "GET"])
def submit():
    
    try:
        Age = int(request.form['Age'])
        Gender = int(request.form['Gender'])
        BMI = int(request.form['BMI'])
        Smoking = int(request.form['Smoking'])
        GeneticRisk = int(request.form['GeneticRisk'])
        PhysicalActivity = int(request.form['PhysicalActivity'])
        AlcoholIntake = int(request.form['AlcoholIntake'])
        CancerHistory = int(request.form['CancerHistory'])
    except ValueError:  
        return render_template("index.html", result="Please enter valid numerical values.")

    input_data = {
        'Age': Age,
        'Gender': Gender,
        'BMI': BMI,
        'Smoking': Smoking,
        'GeneticRisk': GeneticRisk,
        'PhysicalActivity': PhysicalActivity,
        'AlcoholIntake': AlcoholIntake,
        'CancerHistory': CancerHistory
    }

    input_features = [input_data['Age'], input_data['Gender'],
                       input_data['BMI'], input_data['Smoking'],input_data['GeneticRisk'],input_data['PhysicalActivity'],input_data['AlcoholIntake'],input_data['CancerHistory']]

    prediction = model.predict([input_features])
    print(prediction)

    result = prediction[0]

    if result == "0":
        result = "less"
    else:
        result = "more"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False)