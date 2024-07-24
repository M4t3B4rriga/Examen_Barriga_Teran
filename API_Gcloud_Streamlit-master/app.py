import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st
from markupsafe import escape

# Elimina esta línea, ya que estás importando escape de markupsafe
# from jinja2 import escape

# Path del modelo preentrenado
MODEL_PATH = 'models/pickle_model.plk'

# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):
    x = np.asarray(x_in).reshape(1,-1)
    preds = model.predict(x)
    return preds

def main():
    model = ''
    # Se carga el modelo
    if model == '':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)

    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA DE RECOMENDACIÓN PARA CULTIVO</h1>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Lectura de datos
    age = st.text_input("age:")
    workclass = st.text_input("workclass:")
    fnlwgt = st.text_input("fnlwgt:")
    education = st.text_input("education:")
    educationNum = st.text_input("education-num:")
    maritalStatus = st.text_input("marital-status:")
    occupation = st.text_input("occupation:")
    relationship = st.text_input("relationship:")
    race = st.text_input("race:")
    sex = st.text_input("sex:")
    capitalGain = st.text_input("capital-gain:")
    capitalLoss = st.text_input("capital-loss:")
    hoursPerWeek = st.text_input("hours-per-week:")
    nativeCountry = st.text_input("native-country:")
   
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"):
        x_in = [
            np.float_(age.title()),
            np.float_(workclass.title()),
            np.float_(fnlwgt.title()),
            np.float_(education.title()),
            np.float_(educationNum.title()),
            np.float_(maritalStatus.title()),
            np.float_(occupation.title()),
            np.float_(relationship.title()),
            np.float_(race.title()),
            np.float_(sex.title()),
            np.float_(capitalGain.title()),
            np.float_(capitalLoss.title()),
            np.float_(hoursPerWeek.title()),
            np.float_(nativeCountry.title()),
    
        ]
        predictS = model_prediction(x_in, model)
        st.success('EL CULTIVO RECOMENDADO ES: {}'.format(predictS[0]).upper())

if __name__ == '__main__':
    main()