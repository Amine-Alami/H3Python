import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

# ---------------------------------------------
weather = pd.read_csv('Data/weatherHistory.csv')
weather["Formatted Date"] = pd.to_datetime(weather["Formatted Date"],format="%Y-%m-%d %H:%M:%S", utc = True)

#On enlève la column 'Loud Cover' pat manque de données
weather = weather.drop(['Loud Cover'], axis=1)

weather = weather.sort_values(by="Formatted Date")

weather = weather[~(weather["Formatted Date"] < '2006-01-01')]

st.title("Projet analyse de données")
st.markdown('<h3>Analyse des données de météo</h3>', unsafe_allow_html=True)
st.markdown('<h6>Raw Data</h6>', unsafe_allow_html=True)

st.dataframe(weather)

st.write(weather.info())
# ---------------------------------------------
st.markdown('<h6>test</h6>', unsafe_allow_html=True)
sns.catplot(
            x=weather['Precip Type'],
            y=weather['Temperature (C)']
        )
# ---------------------------------------------

# ---------------------------------------------

# ---------------------------------------------