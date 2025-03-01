import os
from flask import Flask, render_template, request
from script import get_predicted_value, helper

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form['symptoms']
    user_symptoms = [s.strip() for s in symptoms.split(',')]

    predicted_disease, unknown_symptoms = get_predicted_value(user_symptoms)

    if predicted_disease:
        desc, pre, med, die, wrkout = helper(predicted_disease)
        return render_template('result.html', disease=predicted_disease, desc=desc, precautions=pre, medications=med, diet=die, workout=wrkout)
    else:
        return render_template('index.html', error=f"Unknown symptoms entered: {', '.join(unknown_symptoms)}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
