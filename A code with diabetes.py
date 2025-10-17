import joblib
import streamlit as st
# joblib.dump(model,'Logistical Regression P2.pkl')
# print('saved the name')
la_model = joblib.load('Logistical Regression P2.pkl')
# print(la_model)
st.title("Diabetic predicter")
st.subheader("Checks if a person's diabetic.")

Glucose = st.number_input("Enter the Glucose level: ",value=0)
Blood_Pressure = st.number_input("Enter the Blood Pressure value: ",value=0)
Skin_Thickness =st.number_input("Enter the skin thickness: ",value=0)
Insulin = st.number_input("Enter the Insulin level: ",value=0)
BMI = st.number_input("Enter the BMI Index: ")
DPF = st.number_input("Enter the Diabetic Pedigree Function: ")
Age = st.number_input("Enter the age: ",value=0)

test = [[Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,DPF,Age]]
res = la_model.predict(test)

if st.button('res'):
    if res[0]==0:
        st.success("Person's non-diabetic")
    else:
        st.error("Person's a diabetic")
