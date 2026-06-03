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

    st.title("Parkinson's Disease Prediction")

    fo = st.number_input("MDVP:Fo(Hz)", format="%.6f")
    fhi = st.number_input("MDVP:Fhi(Hz)", format="%.6f")
    flo = st.number_input("MDVP:Flo(Hz)", format="%.6f")
    jitter_percent = st.number_input("MDVP:Jitter(%)", format="%.6f")
    jitter_abs = st.number_input("MDVP:Jitter(Abs)", format="%.8f")
    rap = st.number_input("MDVP:RAP", format="%.6f")
    ppq = st.number_input("MDVP:PPQ", format="%.6f")
    ddp = st.number_input("Jitter:DDP", format="%.6f")
    shimmer = st.number_input("MDVP:Shimmer", format="%.6f")
    shimmer_db = st.number_input("MDVP:Shimmer(dB)", format="%.6f")
    apq3 = st.number_input("Shimmer:APQ3", format="%.6f")
    apq5 = st.number_input("Shimmer:APQ5", format="%.6f")
    apq = st.number_input("MDVP:APQ", format="%.6f")
    dda = st.number_input("Shimmer:DDA", format="%.6f")
    nhr = st.number_input("NHR", format="%.6f")
    hnr = st.number_input("HNR", format="%.6f")
    rpde = st.number_input("RPDE", format="%.6f")
    dfa = st.number_input("DFA", format="%.6f")
    spread1 = st.number_input("spread1", format="%.6f")
    spread2 = st.number_input("spread2", format="%.6f")
    d2 = st.number_input("D2", format="%.6f")
    ppe = st.number_input("PPE", format="%.6f")

    parkinsons_diagnosis = ""

    if st.button("Parkinson Result"):

        input_data = [[
            fo, fhi, flo,
            jitter_percent, jitter_abs,
            rap, ppq, ddp,
            shimmer, shimmer_db,
            apq3, apq5, apq, dda,
            nhr, hnr,
            rpde, dfa,
            spread1, spread2,
            d2, ppe
        ]]

        try:
            prediction = parkinsons_model.predict(input_data)

            if prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's Disease"
                st.error(parkinsons_diagnosis)
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's Disease"
                st.success(parkinsons_diagnosis)

        except Exception as e:
            st.error(f"Prediction Error: {e}")
