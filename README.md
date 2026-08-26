# 🎭 Money Heist Personality Predictor

An **ML-powered personality prediction web app** that analyzes a user's responses to 9 personality-based questions and predicts which **Money Heist character** they are most similar to.

The project combines **Machine Learning, Python, Pandas, Scikit-learn and Streamlit** to create an interactive personality prediction experience.

> ⚠️ This is a Money Heist-inspired entertainment project and is **not a scientific psychological assessment**.

---

## 🚀 Demo

Answer 9 personality-based questions and let the ML model predict your character.

The app displays:

* 🎭 Predicted Money Heist character
* 🖼️ Character image
* 🎯 Model confidence / match percentage
* 📝 Short character description

Example:

**You are Berlin 🕴️**

**Match: 90%**

> Confident, organized, commanding and calculated.

---

## 🧠 How It Works

The application asks the user 9 questions based on different personality traits:

1. Risk Taking
2. Leadership
3. Emotionality
4. Planning
5. Social Interaction
6. Impulsiveness
7. Problem Solving
8. Empathy
9. Adaptability

Each answer is converted into a numerical value from **1 to 5**.

These values are passed to the trained Machine Learning model.

```text
User Answers
     ↓
9 Personality Features
     ↓
Machine Learning Model
     ↓
Character Prediction
     ↓
Character Probability
     ↓
Photo + Match % + Description
```

---

## 🤖 Machine Learning

The prediction model is saved as:

```text
model_rf.pkl
```

The project uses a **Random Forest model** for character classification.

The model predicts one of the following characters:

* Professor
* Berlin
* Tokyo
* Rio
* Nairobi
* Denver
* Moscow
* Helsinki
* Oslo

The model's `predict_proba()` method is also used to calculate the predicted character's probability.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Streamlit**
* **Pickle**
* **Machine Learning**
* **Git & GitHub**

---

## 📁 Project Structure

```text
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
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd Money-Heist-Personality
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Features

### 🎯 Personality Prediction

Predicts the Money Heist character that best matches the user's responses.

### 🖼️ Character Images

Displays the corresponding character image after prediction.

### 📈 Match Percentage

Shows only the predicted character's model probability instead of displaying a complete probability table.

### 📝 Character Description

Provides a short description explaining the personality style associated with the predicted character.

### 💻 Interactive UI

Built using Streamlit for a simple and interactive web experience.

---

## 🎯 Project Objective

The main goal of this project was to build an **end-to-end Machine Learning application** rather than just training a model in a Jupyter Notebook.

It demonstrates how a trained ML model can be connected to a real interactive frontend where users provide input and receive an immediate prediction.

---

## 🔮 Future Improvements

Some possible improvements for future versions:

* Improve the personality dataset
* Experiment with different ML algorithms
* Improve model accuracy
* Add more Money Heist characters
* Add a more cinematic Money Heist-inspired UI
* Deploy the application online
* Add personality-trait analysis
* Store anonymous prediction statistics

---

## 👨‍💻 Author

**Karan Sharma**

BCA (AI) Student | Aspiring AI/ML Developer

Interested in:

* Machine Learning
* Artificial Intelligence
* Data Science
* Python
* Building practical ML applications

---

## ⭐ If You Like This Project

If you found this project interesting, consider giving the repository a ⭐ on GitHub!

---

### ⚠️ Disclaimer

This project is created for **educational and entertainment purposes**. The predictions are fictional character matches based on a trained Machine Learning model and should not be interpreted as a professional psychological evaluation.
