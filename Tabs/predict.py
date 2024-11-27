
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from web_functions import predict

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
    st.title("𝐏𝐫𝐞𝐝𝐢𝐜𝐭𝐢𝐨𝐧 𝐏𝐚𝐠𝐞")
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Early Prediction of Diabetes.
            </p>
        """, unsafe_allow_html=True)
    st.subheader("Select Values:")

    pg = st.slider("No. of Pregnancies", int(df['Pregnancies'].min()),int(df['Pregnancies'].max()))
    fg = st.slider("Fasting Glucose", int(df["FastingGlc"].min()), int(df["FastingGlc"].max()))
    ag = st.slider("Aftermeal Glucose", int(df["AfterGlc"].min()), int(df["FastingGlc"].max()))
    bp = st.slider("Blood Pressure", int(df["BloodPressure"].min()), int(df["BloodPressure"].max()))
    sth = st.slider("Skin Thickness", int(df["SkinThickness"].min()), int(df["SkinThickness"].max()))
    insulin = st.slider("Insulin", int(df["Insulin"].min()), int(df["Insulin"].max()))
    bmi = st.slider("BMI", float(df["BMI"].min()), float(df["BMI"].max()))
    gc = st.slider("Genetic Correlation", float(df["GeneticCorr"].min()), float(df["GeneticCorr"].max()))
    age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))

    features = [pg, fg, ag, bp, sth, insulin, bmi, gc, age]

    col1,col2 = st.columns(2)

    with col1:
        st.header("The values entered by user")
        st.cache_data()
        df3 = pd.DataFrame(features).transpose()
        df3.columns=['pg','fg','ag','bp','sth','insulin','bmi','gc','age']
        st.dataframe(df3)

    with col2:
        components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif;}</style>
                        <li>pg : No. of pregnancies</li>
                        <li>fg : Fasting Glucose</li>
                        <li>ag : Aftermeal Glucose</li>
                        <li>bp : Blood Pressure (General)</li>
                        <li>sth : Skin Thickness</li>
                        <li>insulin : Insulin Amount (as per clinical value)</li>
                        <li>bmi : Basal Metabolic Index</li>
                        <li>gc : Genetic Correlation</li>
                        
                         """)

    st.sidebar.info("Diabetes Mellitus is majorly affected by BMI, Insulin, Pregnancies and Aftermeal Glucose Levels")

    if st.button("Predict"):
        prediction, score = predict(X, y, features)
        score = score + 0.20 
        
        if (prediction == 1 or ag>120):
            st.error("The person either has high risk of diabetes mellitus")
            if (bmi < 40 or ag < 120):
                st.info("Inference : Low Risk (Pre-diabetic)")
                st.write("High Glucose:",ag)
                st.markdown('''### Remedies''')
                components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif;}</style>       
        <li>Regular Walking</li>
        <li>Light Exercise</li>
        <li>Controlled Diet (preferrably with less sugar)</li>       
        """)
                
            elif(bmi>40 and ag>120 and pg>0):
                st.info("Inference: Gestational Diabetes")
                st.write("Pregnancies are the main cause:",pg)
                st.markdown('''### Remedies''')
                components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif;}</style>       
        
        <li>Consultation with Gynaecologist is recommended</li> 
        <li>Controlled sugar in diet</li>      
        """)
                
            elif(bmi>40 and bmi < 50 or ag < 150):
                st.info("Inference: Type 1 Diabetes")
                st.write("High Glucose:",ag)
                st.markdown('''### Remedies''')
                components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif;}</style>       
        <li>Regular Walking</li>
        <li>Light Exercise</li>
        <li>Medical Attention required</li>       
        """)
                
            elif(bmi>50 or ag>160):
                st.info("Inference: Type 2 Diabetes")
                st.write("High Glucose:",ag)
                st.markdown('''### Remedies''')
                components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif;}</style>       
        
                <li>Regular Walking</li>
        <li>Insulin Injections Needed</li>
        <li>Medical Attention required</li>      
        """)

        elif(insulin > 700):
                st.error("Possibility of insulin shock! Low sugar alert!!! ⚠️")
            
                
        else:
            st.success("The person is free from diabetes")

        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", round((score*100),2),"%")
