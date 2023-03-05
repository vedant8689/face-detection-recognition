import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
st.title('Attendance analysis for workforce management')
if st.button("Analyse Attendance"):

    df = pd.read_csv('Pages/sample_data.csv')

    fig = px.line(df, x='Time', y="Date")
    fig.show()

    plt.hist(df['EID'], bins=15)