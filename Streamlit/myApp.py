import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------
weather = pd.read_csv('../Data/weatherHistory.csv')
weather["Formatted Date"] = pd.to_datetime(weather["Formatted Date"],format="%Y-%m-%d %H:%M:%S", utc = True)

#On enlève la column 'Loud Cover' pat manque de données
weather = weather.drop(['Loud Cover'], axis=1)

weather = weather.sort_values(by="Formatted Date")

weather = weather[~(weather["Formatted Date"] < '2006-01-01')]

st.title("Projet analyse de données")
st.markdown('<h3>Analyse des données de météo</h3>', unsafe_allow_html=True)
st.markdown('<h5>Raw Data</h5>', unsafe_allow_html=True)

st.dataframe(weather)

# ---------------------------------------------
st.markdown('<h5>title 1</h5>', unsafe_allow_html=True)

fig = plt.figure(figsize=(9, 7))
sns.boxplot(
            x=weather['Precip Type'],
            y=weather['Temperature (C)']
        )
st.pyplot(fig)


# ---------------------------------------------

st.markdown('<h5>title 2</h5>', unsafe_allow_html=True)
box = weather[(weather['Temperature (C)'] > -8) & (weather['Temperature (C)'] < 38)]
fig2 = plt.figure(figsize=(9, 7))
sns.boxplot(
            x=box['Precip Type'],
            y=box['Temperature (C)']
        )
st.pyplot(fig2)

# ---------------------------------------------

st.markdown('<h5>title 3</h5>', unsafe_allow_html=True)
fig3 = plt.figure(figsize=(9, 7))
sns.catplot(
            data = weather,
            x="Humidity",
            y="Summary",
            kind="bar",
            height = 7
        )
st.pyplot(fig3)

# ---------------------------------------------

st.markdown('<h5>title 4</h5>', unsafe_allow_html=True)
fig4 = plt.figure(figsize=(9, 7))
sns.relplot(
            data =weather.sample(500),
            x='Humidity',
            y='Temperature (C)'
)
st.pyplot(fig4)
# ---------------------------------------------

st.markdown('<h5>title 5</h5>', unsafe_allow_html=True)
fig5 = plt.figure(figsize=(9, 7))
sns.relplot(
            data =weather.sample(1000),
            x='Wind Speed (km/h)',
            y='Temperature (C)'
)
st.pyplot(fig5)
# ---------------------------------------------

#st.markdown('<h5>title</h5>', unsafe_allow_html=True)
#fig = plt.figure(figsize=(9, 7))

#st.pyplot(fig)
# ---------------------------------------------

#st.markdown('<h5>title</h5>', unsafe_allow_html=True)
#fig = plt.figure(figsize=(9, 7))

#st.pyplot(fig)