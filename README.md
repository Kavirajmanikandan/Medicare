# Medicare
🩺 Medicare - AI-Based Disease Prediction
🚀 A machine learning-powered Flask web app that predicts diseases based on user symptoms.

📌 Project Overview
Medicare is an AI-driven disease prediction system that helps users identify potential diseases based on their symptoms. The system utilizes XGBoost Classifier to predict diseases and provides additional information such as:

Disease description
Possible medications
Recommended diet
Precautionary measures
This project is built using Flask, Pandas, XGBoost, and is deployed on Render.

💡 Features
✅ User-friendly API for predicting diseases
✅ Provides detailed disease information
✅ Suggests medications & diet for better health management
✅ Identifies unknown symptoms (not present in the dataset)
✅ Deployed & accessible online via Render

🛠 Tech Stack
Machine Learning: XGBoost Classifier
Backend: Flask
Data Processing: Pandas, NumPy
Deployment: Render
Model Storage: Pickle

📂 Project Structure

Medicare/
│── app.py             # Flask application
│── script.py          # Helper functions for disease prediction
│── medicare.pkl       # Trained XGBoost model
│── label_encoder.pkl  # LabelEncoder for disease names
│── medicare.csv       # Dataset with symptoms and diseases
│── requirements.txt   # Dependencies for deployment
│── runtime.txt        # Python version specification
│── README.md          # Project documentation (this file)
│── templates/         # HTML files (if needed)
│── static/            # CSS, JS files (if needed)

🚀 How to Run Locally?

1️⃣ Clone the Repository

git clone https://github.com/yourusername/medicare.git
cd medicare

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Flask App

python app.py
Your app will be live at http://127.0.0.1:5000/

🌍 Deployment on Render

Push your project to GitHub
Go to Render & create a new Web Service
Connect GitHub repository & configure settings
Build Command:

pip install -r requirements.txt

Start Command:

gunicorn app:app

Click Deploy & get your live app URL

📌 API Usage
Once deployed, you can use Postman or cURL to test the API:

curl -X POST https://your-app-name.onrender.com/predict \
-H "Content-Type: application/json" \
-d '{"symptoms": ["fever", "cough"]}'

💡 Response Example:

{
  "disease": "Common Cold",
  "description": "A viral infection causing sneezing and a runny nose.",
  "medications": ["Paracetamol"],
  "diet": ["Warm soup, herbal tea"],
  "precautions": ["Drink plenty of fluids", "Take rest"]
}

🛠 Future Improvements
🚀 Expand symptom database for better accuracy
🚀 Improve UI with a React frontend
🚀 Integrate chatbot for interactive diagnosis
🚀 Add multilingual support

👨‍💻 Author
📌 Kaviraj M
📧 Kaviraj7318@gmail.com
🔗 www.linkedin.com/in/kaviraj03

📜 License
🔓 This project is open-source under the MIT License. Feel free to contribute!
