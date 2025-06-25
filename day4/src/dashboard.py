import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Sample Data Setup (Replace this with real CSV load in production)
@st.cache_data
def load_telemetry_data():
    data = {
        'Timestamp': pd.date_range(start='2025-07-01 08:00:00', periods=100, freq='H'),
        'Sensor_ID': np.random.choice(['TEMP_ENGINE', 'PRES_FUEL', 'FLOW_COOLANT'], 100),
        'Value': np.random.normal(100, 10, 100),
        'Unit': np.random.choice(['C', 'kPa', 'LPM'], 100),
        'Status': np.random.choice(['OK', 'WARNING', 'ERROR'], 100)
    }
    df = pd.DataFrame(data)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    return df

# Load data
df_telemetry_cleaned = load_telemetry_data()

# Streamlit layout
st.set_page_config(layout="wide")
st.title("📊 Telemetry Dashboard (Powered by Streamlit)")

# Sidebar
st.sidebar.header("🔎 Filter Options")
sensor_ids = df_telemetry_cleaned['Sensor_ID'].unique()
selected_sensor = st.sidebar.selectbox("Select Sensor ID", sensor_ids)

min_date = df_telemetry_cleaned.index.min().date()
max_date = df_telemetry_cleaned.index.max().date()
date_range = st.sidebar.date_input("Select Date Range", (min_date, max_date), min_value=min_date, max_value=max_date)

# Filter data
start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
filtered_df = df_telemetry_cleaned[
    (df_telemetry_cleaned['Sensor_ID'] == selected_sensor) &
    (df_telemetry_cleaned.index.date >= start_date.date()) &
    (df_telemetry_cleaned.index.date <= end_date.date())
]

# Show filtered data
st.subheader(f"📄 Data for {selected_sensor}")
st.dataframe(filtered_df)

# Plot sensor value trend
st.subheader("📈 Sensor Value Trend")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(filtered_df.index, filtered_df['Value'], marker='o', linestyle='-', color='teal')
ax.set_title(f"Trend of {selected_sensor} Readings")
ax.set_xlabel("Timestamp")
ax.set_ylabel("Sensor Value")
ax.grid(True)
st.pyplot(fig)

# Status breakdown
st.subheader("📊 Sensor Status Counts")
status_counts = filtered_df['Status'].value_counts()

fig2, ax2 = plt.subplots(figsize=(6, 3))
status_counts.plot(kind='bar', color=['green', 'orange', 'red'], ax=ax2)
ax2.set_title("Status Breakdown")
ax2.set_ylabel("Count")
st.pyplot(fig2)
