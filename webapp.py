import streamlit as st
import plotly.express as px
import sqlite3


connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT date FROM temperatures")
date = cursor.fetchall() # Returns a list of tuples
date = [item[0] for item in date] # index into each tuple and remove the tuple nesting

st.title("Average World Temperature")

cursor.execute("SELECT temperature from temperatures")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]

figure = px.line(x=date, y=temperature,
                 labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)