import pandas as pd
import numpy as np
import pickle

# Load dataset
data = pd.read_csv('medicare.csv')

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(data['Disease'])  # Train LabelEncoder with disease labels
pickle.dump(le, open('label_encoder.pkl', 'wb'))  # Save it for later use

# Load model correctly
xgb_model = pickle.load(open('medicare.pkl', 'rb'))  # Load XGBClassifier model
le = pickle.load(open('label_encoder.pkl', 'rb'))  # Load LabelEncoder separately

# Prepare feature columns
X = data.drop(['Disease', 'Description', 'Diet', 'Medication', 'Precaution_1', 'Precaution_2', 
               'Precaution_3', 'Precaution_4', 'workout'], axis=1)


# Function to predict disease
def get_predicted_value(patient_symptoms):
    patient_symptoms = [s.lower() for s in patient_symptoms]
    
    # Create an empty input vector
    input_vector = pd.DataFrame(columns=X.columns)
    input_vector.loc[0] = 0  

    unknown_symptoms = []
    
    for symptom in patient_symptoms:
        if symptom in X.columns:
            input_vector[symptom] = 1
        else:
            unknown_symptoms.append(symptom)
    
    if unknown_symptoms:
        return None, unknown_symptoms  # Return unknown symptoms list
    
    input_vector = input_vector.to_numpy()
    
    prediction = xgb_model.predict(input_vector)[0]  # Get prediction
    print(f"Raw Prediction from Model: {prediction}")  # Debugging

    # Convert prediction to integer
    prediction = int(prediction)
    print(f"Type of le: {type(le)}")  # Debugging to ensure le is a LabelEncoder
    print(f"Available classes in LabelEncoder: {le.classes_}")

    try:
        decoded_prediction = le.inverse_transform([prediction])[0]
    except ValueError:
        print(f"Error: Prediction {prediction} not found in LabelEncoder classes!")
        decoded_prediction = "Unknown Disease"

    return decoded_prediction, []


# Function to get disease details
def helper(dis):
    disease_data = data[data['Disease'] == dis]

    desc = disease_data['Description'].values[0] if not disease_data['Description'].isna().all() else "No description available"
    pre = [disease_data['Precaution_1'].values[0], disease_data['Precaution_2'].values[0], 
           disease_data['Precaution_3'].values[0], disease_data['Precaution_4'].values[0]]
    pre = [p for p in pre if pd.notna(p)]
    med = [disease_data['Medication'].values[0]] if not disease_data['Medication'].isna().all() else []
    die = [disease_data['Diet'].values[0]] if not disease_data['Diet'].isna().all() else []
    wrkout = [disease_data['workout'].values[0]] if not disease_data['workout'].isna().all() else []

    return desc, pre, med, die, wrkout
