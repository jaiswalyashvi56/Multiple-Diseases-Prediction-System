import pickle
import streamlit as st

# ---------------- LOAD MODELS ----------------
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# ---------------- SIDEBAR MENU ----------------
st.sidebar.title("Multiple Disease Prediction System")

selected = st.sidebar.radio(
    "Select Disease",
    ["Diabetes", "Heart Disease", "Parkinsons"]
)

# ---------------- DIABETES ----------------
if selected == "Diabetes":
    st.title("Diabetes Prediction")

    pregnancies = st.text_input("Number of Pregnancies")
    glucose = st.text_input("Glucose Level")
    bp = st.text_input("Blood Pressure")
    skin = st.text_input("Skin Thickness")
    insulin = st.text_input("Insulin Level")
    bmi = st.text_input("BMI")
    dpf = st.text_input("Diabetes Pedigree Function")
    age = st.text_input("Age")

    if st.button("Diabetes Result"):
        try:
            input_data = [[float(pregnancies), float(glucose), float(bp),
                           float(skin), float(insulin), float(bmi),
                           float(dpf), float(age)]]

            result = diabetes_model.predict(input_data)

            if result[0] == 1:
                st.error("Person is Diabetic")
            else:
                st.success("Person is Not Diabetic")
        except:
            st.warning("Enter all values correctly")


# ---------------- HEART ----------------
elif selected == "Heart Disease":
    st.title("Heart Disease Prediction")

    age = st.text_input("Age")
    sex = st.text_input("Sex (1=Male, 0=Female)")
    cp = st.text_input("Chest Pain Type")
    trestbps = st.text_input("Resting BP")
    chol = st.text_input("Cholesterol")
    fbs = st.text_input("Fasting Blood Sugar")
    restecg = st.text_input("Rest ECG")
    thalach = st.text_input("Max Heart Rate")
    exang = st.text_input("Exercise Induced Angina")
    oldpeak = st.text_input("Oldpeak")
    slope = st.text_input("Slope")
    ca = st.text_input("CA")
    thal = st.text_input("Thal")

    if st.button("Heart Result"):
        try:
            input_data = [[float(age), float(sex), float(cp), float(trestbps),
                           float(chol), float(fbs), float(restecg),
                           float(thalach), float(exang), float(oldpeak),
                           float(slope), float(ca), float(thal)]]

            result = heart_model.predict(input_data)

            if result[0] == 1:
                st.error("Person has Heart Disease")
            else:
                st.success("Person does not have Heart Disease")
        except:
            st.warning("Enter all values correctly")


# ---------------- PARKINSON ----------------
elif selected == "Parkinsons":
    st.title("Parkinsons Disease Prediction")

    fo = st.text_input("MDVP:Fo(Hz)")
    fhi = st.text_input("MDVP:Fhi(Hz)")
    flo = st.text_input("MDVP:Flo(Hz)")
    jitter = st.text_input("MDVP:Jitter(%)")
    shimmer = st.text_input("MDVP:Shimmer")

    if st.button("Parkinson Result"):
        try:
            input_data = [[float(fo), float(fhi), float(flo),
                           float(jitter), float(shimmer)]]

            result = parkinsons_model.predict(input_data)

            if result[0] == 1:
                st.error("Person has Parkinsons Disease")
            else:
                st.success("Person does not have Parkinsons Disease")
        except:
            st.warning("Enter all values correctly")