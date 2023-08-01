import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def create_sankey_diagram(df):
    # Your existing code to create the Sankey diagram
    # ...

def main():
    # Data frame (ganti dengan data frame Anda)
    data = {
        'Pengobatan 1': ['Pharmacy', 'Pharmacy', 'Pharmacy', 'Pharmacy', 'Pharmacy'],
        'Pengobatan 2': ['Pharmacy', 'Community health center', 'Private doctor', 'Private clinic', 'Traditional medicine'],
        'Total': [4.0, 5.0, 1.0, 2.0, 1.0],
        'Pengobatan 2.1': ['Pharmacy', 'Pharmacy', 'Community health center', 'Private doctor', 'Private clinic'],
        'Pengobatan 3': ['Community health center', 'Pharmacy', 'Community health center', 'Home remedies', 'Private clinic'],
        'Total 1': [1.0, 3.0, 5.0, 1.0, 2.0],
        'Pengobatan 3.1': ['Pharmacy', 'Community health center', 'Pharmacy', 'Home remedies', 'Private clinic'],
        'Pengobatan 4': ['PHC', 'PHC', 'PHC', 'PHC', 'PHC'],
        'Total 2': [4.0, 1.0, 5.0, 1.0, 1.0],
        'Pengobatan 4.1': ['PHC', 'Confirmed', 'NaN', 'NaN', 'NaN'],
        'Pengobatan 5': ['Confirmed', 'Confirmed', 'NaN', 'NaN', 'NaN'],
        'Total 3': [18.0, 1.0, 'NaN', 'NaN', 'NaN']
    }

    df = pd.DataFrame(data)

    # Set page title and layout
    st.set_page_config(page_title="Sankey Diagram", layout="wide")

    # Title and description
    st.title("Grafik Sankey Pengobatan")
    st.write("Ini adalah contoh aplikasi Streamlit dengan diagram Sankey.")

    # Display the Sankey diagram
    st.plotly_chart(create_sankey_diagram(df))

if __name__ == "__main__":
    main()
