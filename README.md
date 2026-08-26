🎭 Money Heist Personality Predictor

An interactive Machine Learning web application that predicts which Money Heist character best matches your personality based on your answers to 9 personality-based questions.

The project combines Machine Learning, Python, Pandas, Scikit-learn and Streamlit to turn a trained classification model into an interactive web application.

🚀 Live Demo

👉 "Try the Money Heist Personality Predictor" (https://money-heist-personality-predictor.streamlit.app/)

Answer the questions, reveal your result, and discover your Money Heist character match. 🎭

---

✨ Features

- 🎯 Predicts a Money Heist character based on personality responses
- 🧠 Uses a trained Machine Learning classification model
- 🎭 Displays the predicted character
- 🖼️ Shows the corresponding character image
- 📊 Displays the predicted character's match percentage
- 📝 Provides a short personality description
- 💻 Interactive Streamlit interface
- 🌐 Deployed as a live web application

---

🧠 How It Works

The application asks the user 9 personality-based questions.

Each answer is converted into a numerical value from 1 to 5 and passed to the trained Machine Learning model.

User
 ↓
9 Personality Questions
 ↓
Numerical Features
 ↓
Random Forest Model
 ↓
Character Prediction
 ↓
Match Percentage
 ↓
Character Image + Description

---

🎯 Personality Features

The model uses the following personality-related features:

Feature| What it represents
Risk Taking| Comfort with risky situations
Leadership| Tendency to take responsibility
Emotionality| Influence of emotions on decisions
Planning| Planning and preparation style
Social| Interaction with other people
Impulsiveness| Tendency to make quick decisions
Problem Solving| Comfort with difficult problems
Empathy| Consideration of others' feelings
Adaptability| Ability to adjust to unexpected changes

---

🤖 Machine Learning Model

The project uses a Random Forest Classifier for character prediction.

The trained model is stored as:

model_rf.pkl

The application also uses "predict_proba()" to calculate the probability of the predicted character.

The model can predict characters such as:

- 🧠 Professor
- 🕴️ Berlin
- 🔥 Tokyo
- 💻 Rio
- 👑 Nairobi
- 😄 Denver
- ⛏️ Moscow
- 🛡️ Helsinki
- ⚔️ Oslo

---

🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- Machine Learning
- GitHub
- Streamlit Cloud

---

📁 Project Structure

Money-Heist-Personality/
│
├── app.py
├── model_rf.pkl
├── requirements.txt
│
└── images/
    ├── Professor.jpg
    ├── Berlin.jpg
    ├── Tokyo.jpg
    ├── Rio.jpg
    ├── Nairobi.jpg
    ├── Denver.jpg
    ├── Moscow.jpg
    ├── Helsinki.jpg
    └── Oslo.jpg

---

▶️ Run Locally

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Navigate into the project:

cd Money-Heist-Personality

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

🌐 Deployment

The application is deployed using Streamlit Community Cloud.

Live Application

👉 https://money-heist-personality-predictor.streamlit.app/

---

🎓 Project Objective

The main objective of this project was to build a practical end-to-end Machine Learning application.

Instead of keeping the ML model limited to a Jupyter Notebook, the trained model was integrated with a Streamlit frontend where users can interact with the model and receive an immediate prediction.

This project helped demonstrate the complete workflow:

Dataset
   ↓
Data Preparation
   ↓
Model Training
   ↓
Model Saving
   ↓
Streamlit Frontend
   ↓
Model Integration
   ↓
Deployment

---

🔮 Future Improvements

Possible future improvements include:

- Improve the training dataset
- Experiment with different classification algorithms
- Improve model performance
- Add more personality traits
- Add more characters
- Create a more cinematic UI
- Add animations and better result cards
- Improve the questionnaire
- Add more detailed personality analysis

---

👨‍💻 Author

Karan Sharma

BCA (AI) Student | Aspiring AI/ML Developer

Currently learning and building projects in:

- Python
- Data Science
- Machine Learning
- Artificial Intelligence
- Streamlit

---

⚠️ Disclaimer

This project is created for educational and entertainment purposes.

The character prediction is based on a Machine Learning model trained for this project and should not be considered a scientific or professional psychological assessment.

The project is inspired by the fictional world of Money Heist.
