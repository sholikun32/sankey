import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def create_sankey_diagram(df):
    all_treatments = pd.unique(df[['Pengobatan 1', 'Pengobatan 2', 'Pengobatan 2.1', 'Pengobatan 3', 'Pengobatan 3.1', 'Pengobatan 4', 'Pengobatan 4.1', 'Pengobatan 5']].values.ravel('K'))
    treatment_codes = {treatment: code for code, treatment in enumerate(all_treatments)}

    for col in df.columns:
        df[col] = df[col].map(treatment_codes)

    source = df[['Pengobatan 1', 'Pengobatan 2', 'Pengobatan 2.1', 'Pengobatan 3', 'Pengobatan 3.1', 'Pengobatan 4', 'Pengobatan 4.1']].values.ravel()
    target = df[['Pengobatan 2', 'Pengobatan 2.1', 'Pengobatan 3', 'Pengobatan 3.1', 'Pengobatan 4', 'Pengobatan 4.1', 'Pengobatan 5', 'Pengobatan 5', 'Pengobatan 5', 'Pengobatan 5']].values.ravel()
    value = df[['Total', 'Total 1', 'Total 2', 'Total 3', 'Total 2', 'Total 3', 'Total 3']].values.ravel()

    treatment_labels = [treatment for treatment in all_treatments]
    treatment_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    line_colors = [treatment_colors[idx] for idx in source]

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=treatment_labels,
            color=treatment_colors,
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            colorscales='Viridis',
            line=dict(color=line_colors, width=0.5),
        )
    )])

    fig.update_layout(title_text="Grafik Sankey Pengobatan",
                      font_size=10,
                      title_font_size=14,
                      title_x=0.5,
                      title_y=0.9,
                      xaxis=dict(showticklabels=False),
                      yaxis=dict(showticklabels=False))

    return fig

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

    # Create the Sankey diagram
    st.plotly_chart(create_sankey_diagram(df))

if __name__ == "__main__":
    main()
