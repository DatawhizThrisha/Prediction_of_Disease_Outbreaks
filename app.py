import streamlit as st
import pickle
import numpy as np
import time
with open('/mount/src/prediction_of_disease_outbreaks/diabetes_model.pkl',"rb") as file:
    dia_model=pickle.load(file)
with open('/mount/src/prediction_of_disease_outbreaks/heart_disease_model.pkl',"rb") as file:
    heart_model=pickle.load(file)
with open('/mount/src/prediction_of_disease_outbreaks/parkinsons_model.pkl',"rb") as file:
    park_model=pickle.load(file)
st.set_page_config(
    page_title="Heart Disease Prediction",
    layout="wide"
)

if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Diabetes Prediction"
st.sidebar.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Host+Grotesk:ital,wght@0,300..800;1,300..800&display=swap');
        [data-testid="stSidebarCollapseButton"] {
            display: none;
        }
        *{
            font-family: "Host Grotesk", serif;
            font-optical-sizing: auto;
            font-weight: 700;
            font-style: normal;
        }
        [data-testid="stSidebarUserContent"] {
            background-color:rgb(28, 29, 34);
            padding: 15px;
            border-radius: 7px 20px;
            margin:5%;
            width: 90%;
        }
        [data-testid="stBaseButton-secondary"] {
            display: block;
            background-color: #272a33;
            color: white;
            border: none;
            width: 100%;
            height: 50px;
            margin: 5px 0;
            text-align: center;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.5s ease;
            padding: 10px;
            font-size: 18px;
        } 
        [data-testid="stTextInput"]{
            margin:20px 0;
        }
        [data-testid="stBaseButton-secondary"]:hover {
            background-color: black;
            color: #c9ff7d;
            border: 0.5px solid #c9ff7d;
        } 
        [data-testid="stBaseButton-secondary"]:focus:not(:active) {
            background-color: #c9ff7d;
            color: black;
        } 
        [data-testid="stBaseButton-secondaryFormSubmit"]{
            width:80%
        }     
    </style>
""", unsafe_allow_html=True)
c=st.sidebar.container()
with c:
    c.markdown("""
        <div class="side-style">
            <div style="color: white; font-size: 24px; text-align: center;">
                Prediction of Disease Outbreak System
            </div>
            <hr>
    """, unsafe_allow_html=True)
    if c.button("Diabetes Prediction"):
        st.session_state.active_tab = "Diabetes Prediction"

    if c.button("Heart Disease Prediction"):
        st.session_state.active_tab = "Heart Disease Prediction"

    if c.button("Parkinson Prediction"):
        st.session_state.active_tab = "Parkinson Prediction"



if st.session_state.active_tab == "Diabetes Prediction":
    st.title("This is the Diabetes Prediction page.")
    
    st.write("Give the Required Information to Predict that you have Diabetes through Machine Learning")
    col1,col2,col3=st.columns(3)
    with col1:
        preg=st.text_input("Number of Pregnancies")
        sthick=st.text_input("Enter your skin fold thickness")
        pedi=st.text_input("Diabetes Pedigree Function Value")
        dia_pred=st.button("Diabetes Test Result",type="primary")
        
    with col2:
        gulc=st.text_input("Enter Your Gulcose Level")
        ins=st.text_input("Insulin Level")
        age=st.text_input("Enter Your Age")
        
    with col3:
        bp=st.text_input("Enter Your Blood Pressure Level(mm Hg)")
        bmi=st.text_input("Enter Your BMI (weight in kg/(height in m)^2)")
    if(dia_pred):
        with st.spinner():
            time.sleep(2)
            features=np.array([preg,gulc,bp,sthick,ins,bmi,pedi,age]).reshape(1,-1)
            prediction=dia_model.predict(features)
            if (prediction[0]==0):
                st.balloons()
                st.success("Congratulations , Your Diabetes Test Resulted as Negative")
            else:
                st.warning("We are very Sad to say that Your Diabetes Test Result is Positive")
elif st.session_state.active_tab == "Heart Disease Prediction":
    st.title("This is the Heart Disease Prediction page.")
    st.write("Give the Required Information to Predict that you have Heart Disease through Machine Learning")
    Hcol1,Hcol2,Hcol3=st.columns(3)
    with Hcol1:
        age=st.text_input("Enter Your Age")
        rbp=st.text_input("Enter your Resting Blood Pressure")
        rer=st.text_input("Resting Electrocardiagraphic Results (0-2)")
        oldp=st.text_input("Enter Your OldPeak value")
        thal=st.text_input("Enter your Thal Value (0-2)")
        heart_pred=st.button("Heart Disease Test Result",type="primary")
        
    with Hcol2:
        sex=st.text_input("Enter your Sex (M-1 or F=0)")
        serum=st.text_input("Enter Your Serum Colestoral (mg/dl)")
        mhr=st.text_input("Enter Your Maximum Heart Rate Acheived")
        slpe=st.text_input("Slope of the Peak Exercise ST Segment")
        
    with Hcol3:
        ctype=st.text_input("Enter Your Chest pain type (0-3)")
        fbs=st.text_input("Enter Your Fasting Blood Sugar (mg/dl)")
        eia=st.text_input("Exercise Induced Angina")
        nmv=st.text_input("Number of Major Vessels Colored by flouroscopy")
    
    if(heart_pred):
        with st.spinner():
            time.sleep(2)
            features=np.array([int(age),int(sex),int(ctype),int(rbp),int(serum),int(fbs),int(rer),int(mhr),int(eia),float(oldp),int(slpe),int(nmv),int(thal)]).reshape(1,-1)
            prediction=heart_model.predict(features)
            if (prediction[0]==0):
                st.balloons()
                st.success("Congratulations , Your Heart Disease Test Resulted as Negative")
            else:
                st.warning("We are very Sad to say that Your Heart Disease Test Result is Positive")
elif st.session_state.active_tab == "Parkinson Prediction":
    st.title("This is the Parkinson Prediction page.")
    st.write("Give the Required Information to Predict that you have Parkinson Disease through Machine Learning")
    pcol1,pcol2,pcol3=st.columns(3)
    with pcol1:
        mdv1=st.text_input("Enter Your MDVP:Fo(Hz)")
        mdv4=st.text_input("Enter your MDVP:Jitter(%)")
        mdv7=st.text_input("Enter your MDVP:PPQ")
        mdv9=st.text_input("Enter Your MDVP:Shimmer(dB)")
        mdv10=st.text_input("Enter Your MDVP:APQ")
        hnr=st.text_input("Enter your HNR")
        spr1=st.text_input("Enter your Spread1")
        ppe=st.text_input("Enter your PPE")
        park_pred=st.button("Parkinson Disease Test Result",type="primary")
        
    with pcol2:
        mdv2=st.text_input("Enter Your MDVP:Fhi(Hz) ")
        mdv5=st.text_input("Enter your MDVP:Jitter(Abs)")
        jit=st.text_input("Enter your Jitter:DDP")
        shi1=st.text_input("Enter Your Shimmer:APQ3")
        shi3=st.text_input("Enter your Shimmer:DDA")
        rpde=st.text_input("Enter Your RPDE")
        spr2=st.text_input("Enter your Spread2")
        
        
        
    with pcol3:
        mdv3=st.text_input("Enter your MDVP:Flo(Hz)")
        mdv6=st.text_input("Enter your MDVP:RAP")
        mdv8=st.text_input("Enter your MDVP:Shimmer")
        shi2=st.text_input("Enter your Shimmer:APQ5")
        nhr=st.text_input("Enter your NHR")
        dfa=st.text_input("Enter your DFA")
        d2=st.text_input("Enter your D2")
        
        
        
    
    if(park_pred):
        with st.spinner():
            time.sleep(2)
            features = np.array([
                 float(mdv1), float(mdv2), float(mdv3), float(mdv4), 
                float(mdv5), float(mdv6), float(mdv7), float(jit), float(mdv8), 
                float(mdv9), float(shi1), float(shi2), float(mdv10), float(shi3), 
                float(nhr), float(hnr), float(rpde), float(dfa), float(spr1), 
                float(spr2), float(d2), float(ppe)
            ], dtype=np.float64).reshape(1, -1)
            prediction=park_model.predict(features)
            if (prediction[0]==0):
                st.balloons()
                st.success("Congratulations , Your Parkinson Disease Test Resulted as Negative")
            else:
                st.warning("We are very Sad to say that Your Heart Disease Test Result is Positive")
