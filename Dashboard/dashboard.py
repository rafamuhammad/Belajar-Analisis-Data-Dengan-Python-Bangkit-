# IMPORT LIBRARY
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATA
@st.cache(allow_output_mutation=True)
def load_data():
    data_day = pd.read_csv("Data/day.csv") 
    return data_day

data_day = load_data()

# TITLE DASHBOARD
st.title("Bike Sharing Dashboard")

# SIDEBAR
st.sidebar.title("Information:")
st.sidebar.markdown("**• Name : Rafa Muhammad Ghifar Ramadhan**")
st.sidebar.markdown("**• Email : rafaa.muhammadd@gmail.com**")
st.sidebar.title("Dataset Bike Share")

# Show dataset in sidebar if toggled
if st.sidebar.checkbox("Show raw data", False):
    st.sidebar.write(data_day)

# MAIN PAGE
# ==============================

# PAGE: Visualization 1 - Is there an effect of the season on bike rentals?
st.header("Visualization 1: Is There an Effect of the Season on Bike Rentals?")
plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=data_day)
plt.title('Is There an Effect of the Season on Bike Rentals?')
plt.xlabel('Season')
plt.ylabel('Number of Bike Rentals')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Winter', 'Spring', 'Summer', 'Fall'])
st.pyplot(plt)  # Use Streamlit's pyplot to display the figure
plt.clf()  # Clear the figure for the next plot

# PAGE: Visualization 2 - Improved visualization for the relationship between temperature and bike rentals
st.header("Visualization 2: Impact of Temperature on Bike Rentals")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=data_day, color='b', alpha=0.6)
sns.regplot(x='temp', y='cnt', data=data_day, scatter=False, color='r', line_kws={"lw": 2})
plt.title('Impact of Temperature on Bike Rentals', fontsize=16)
plt.xlabel('Temperature (Normalized)', fontsize=12)
plt.ylabel('Number of Bike Rentals', fontsize=12)
plt.grid(True)
st.pyplot(plt)  # Use Streamlit's pyplot to display the figure
plt.clf()  # Clear the figure for future plots

# PAGE: Aggregate Data by Season
st.header("Aggregate Statistics for Bike Rentals by Season")
aggregated_data = data_day.groupby('season', observed=True).agg({'cnt': ['max', 'min', 'mean', 'sum']})
aggregated_data.columns = ['Max Count', 'Min Count', 'Average Count', 'Total Count']
aggregated_data = aggregated_data.reset_index()
st.dataframe(aggregated_data)

# PAGE: Aggregate Data by Weather
st.header("Aggregate Statistics for Bike Rentals by Weather")
weather_aggregated_data = data_day.groupby('weathersit', observed=True).agg({'cnt': ['max', 'min', 'mean', 'sum']})
weather_aggregated_data.columns = ['Max Count', 'Min Count', 'Average Count', 'Total Count']
weather_aggregated_data = weather_aggregated_data.reset_index()
st.dataframe(weather_aggregated_data)
