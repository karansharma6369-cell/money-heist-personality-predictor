
import streamlit as st
import pandas as pd
import pickle
import os


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Money Heist Personality Predictor",
    page_icon="🎭",
    layout="centered"
)


# =========================================================
# LOAD ML MODEL
# =========================================================

try:
    with open("model_rf.pkl", "rb") as f:
        model = pickle.load(f)

except FileNotFoundError:
    st.error(
        "❌ model_rf.pkl nahi mila. "
        "Is file ko app.py ke same folder mein rakho."
    )
    st.stop()


# =========================================================
# CHARACTER INFORMATION
# =========================================================

characters = {

    "Professor": (
        "🧠",
        "The Master Strategist",
        "Strategic, patient, analytical and highly planned."
    ),

    "Berlin": (
        "🕴️",
        "The Commander",
        "Confident, organized, commanding and calculated."
    ),

    "Tokyo": (
        "🔥",
        "The Risk Taker",
        "Bold, independent, emotional and action-oriented."
    ),

    "Rio": (
        "💻",
        "The Techie",
        "Curious, sensitive, creative and technically minded."
    ),

    "Nairobi": (
        "👑",
        "The Motivator",
        "Energetic, empathetic, social and team-oriented."
    ),

    "Denver": (
        "😄",
        "The Free Spirit",
        "Energetic, spontaneous, emotional and adaptable."
    ),

    "Moscow": (
        "⛏️",
        "The Protector",
        "Dependable, caring, practical and loyal."
    ),

    "Helsinki": (
        "🛡️",
        "The Loyal One",
        "Calm, dependable, supportive and disciplined."
    ),

    "Oslo": (
        "⚔️",
        "The Silent Operator",
        "Reserved, practical, focused and disciplined."
    )
}


# =========================================================
# CHARACTER IMAGES
# =========================================================

character_images = {

    "Professor": "images/Professor.jpg",
    "Berlin": "images/Berlin.jpg",
    "Tokyo": "images/Tokyo.jpg",
    "Rio": "images/Rio.jpg",
    "Nairobi": "images/Nairobi.jpg",
    "Denver": "images/Denver.jpg",
    "Moscow": "images/Moscow.jpg",
    "Helsinki": "images/Helsinki.jpg",
    "Oslo": "images/Oslo.jpg"
}


# =========================================================
# QUESTIONS
# =========================================================

questions = [

    (
        "Risk_Taking",
        "Agar koi opportunity risky ho lekin reward bada ho, tum kya karoge?",
        [
            "Bilkul risk nahi lunga",
            "Usually avoid karunga",
            "Situation dekhkar decide karunga",
            "Risk lene ke chances high hain",
            "Risk lene ke liye ready rahunga"
        ]
    ),

    (
        "Leadership",
        "Group mein difficult situation aaye to kya tum responsibility lena chahoge?",
        [
            "Nahi, follow karunga",
            "Usually kisi aur ko lead karne dunga",
            "Situation par depend karta hai",
            "Zarurat padne par lead karunga",
            "Naturally leadership lena pasand karunga"
        ]
    ),

    (
        "Emotionality",
        "Tumhare emotions tumhare decisions ko kitna influence karte hain?",
        [
            "Bahut kam",
            "Kam",
            "Kabhi-kabhi",
            "Kaafi zyada",
            "Bahut zyada"
        ]
    ),

    (
        "Planning",
        "Important kaam start karne se pehle tum kitna plan banate ho?",
        [
            "Almost plan nahi karta",
            "Basic planning",
            "Moderate planning",
            "Detailed planning",
            "Har important possibility ka plan banata hoon"
        ]
    ),

    (
        "Social",
        "New logon ke group mein tum kitni easily interact karte ho?",
        [
            "Bahut difficult",
            "Thoda difficult",
            "Depends on situation",
            "Usually easily",
            "Bahut easily connect kar leta hoon"
        ]
    ),

    (
        "Impulsiveness",
        "Kya tum bina zyada soche turant decision le lete ho?",
        [
            "Almost never",
            "Rarely",
            "Sometimes",
            "Often",
            "Very often"
        ]
    ),

    (
        "Problem_Solving",
        "Difficult problem solve karne mein tum kitne comfortable ho?",
        [
            "Bahut uncomfortable",
            "Thoda difficult",
            "Average",
            "Usually comfortable",
            "Complex problems interesting lagte hain"
        ]
    ),

    (
        "Empathy",
        "Decision lete waqt doosron ki feelings ko kitna consider karte ho?",
        [
            "Bahut kam",
            "Kam",
            "Kabhi-kabhi",
            "Kaafi zyada",
            "Bahut strongly"
        ]
    ),

    (
        "Adaptability",
        "Plan suddenly fail ho jaye to tum kitni easily adjust karte ho?",
        [
            "Bahut difficult",
            "Thoda difficult",
            "Manage kar leta hoon",
            "Usually quickly adapt",
            "Unexpected changes easily handle karta hoon"
        ]
    )
]


# =========================================================
# FEATURE ORDER
# =========================================================

feature_order = [q[0] for q in questions]


# =========================================================
# PAGE TITLE
# =========================================================

st.title("🎭 Money Heist Personality Predictor")

st.write(
    "9 questions ka honestly answer do aur dekho "
    "tum kis Money Heist character se sabse zyada match karte ho."
)


# =========================================================
# USER ANSWERS
# =========================================================

answers = {}


for i, (feature, question, options) in enumerate(
    questions,
    1
):

    st.subheader(
        f"{i}. {question}"
    )

    answers[feature] = st.radio(

        "Choose one:",

        range(1, 6),

        format_func=lambda x, opts=options:
            f"{x} — {opts[x - 1]}",

        key=feature,

        label_visibility="collapsed"
    )


# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button(
    "🎯 Reveal My Character",
    use_container_width=True
):

    # -----------------------------------------------------
    # CREATE INPUT DATAFRAME
    # -----------------------------------------------------

    X = pd.DataFrame(
        [
            [
                answers[f]
                for f in feature_order
            ]
        ],
        columns=feature_order
    )


    try:

        # -------------------------------------------------
        # MODEL PREDICTION
        # -------------------------------------------------

        prediction = str(
            model.predict(X)[0]
        )


        # -------------------------------------------------
        # CHARACTER INFORMATION
        # -------------------------------------------------

        emoji, title, description = characters.get(

            prediction,

            (
                "🎭",
                "Mystery Character",
                "Model prediction received."
            )
        )


        # -------------------------------------------------
        # GET PREDICTION PROBABILITY
        # -------------------------------------------------

        confidence = None

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(X)[0]

            class_probabilities = dict(
                zip(
                    model.classes_,
                    probabilities
                )
            )

            if prediction in class_probabilities:

                confidence = class_probabilities[
                    prediction
                ]


        # -------------------------------------------------
        # RESULT SECTION
        # -------------------------------------------------

        st.divider()

        # -------------------------------------------------
        # CHARACTER IMAGE
        # -------------------------------------------------

        image_path = character_images.get(
            prediction
        )


        if image_path and os.path.exists(image_path):

            st.image(
                image_path,
                width=300
            )

        else:

            # If image is missing, don't crash the app
            st.markdown(
                f"""
                <div style="
                    text-align: center;
                    font-size: 90px;
                    padding: 20px;
                ">
                    {emoji}
                </div>
                """,
                unsafe_allow_html=True
            )


        # -------------------------------------------------
        # CHARACTER NAME
        # -------------------------------------------------

        st.success(
            f"{emoji} You are **{prediction}**"
        )


        # -------------------------------------------------
        # CHARACTER TITLE
        # -------------------------------------------------

        st.header(
            title
        )


        # -------------------------------------------------
        # PREDICTION PERCENTAGE
        # -------------------------------------------------

        if confidence is not None:

            st.subheader(
                f"🎯 Match: {confidence:.1%}"
            )


        # -------------------------------------------------
        # CHARACTER DESCRIPTION
        # -------------------------------------------------

        st.write(
            description
        )

        st.divider()


    except Exception as e:

        st.error(
            "❌ Prediction error. Check karo ki "
            "model_rf.pkl isi 9-feature order ko expect karta hai."
        )

        st.code(
            str(e)
        )


# =========================================================
# FOOTER
# =========================================================

st.caption(
    "⚠️ Money Heist-inspired entertainment project; "
    "not a scientific psychological assessment."
)
