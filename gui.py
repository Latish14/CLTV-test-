# -*- coding: utf-8 -*-
"""GUI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Pratyush-3003/CLTV/blob/main/GUI.ipynb
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from lifetimes import BetaGeoFitter, GammaGammaFitter
from lifetimes.utils import summary_data_from_transaction_data

st.set_page_config(page_title="CLV Predictor", layout="wide")
st.title("📊 Customer Lifetime Value (CLV) Predictor")

uploaded_file = st.file_uploader("Upload transaction CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='latin-1')


    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    df['CustomerID'] = df['CustomerID'].astype(int)
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    summary = summary_data_from_transaction_data(df, 'CustomerID', 'InvoiceDate', 'TotalPrice')


    bgf = BetaGeoFitter(penalizer_coef=0.1)
    bgf.fit(summary['frequency'], summary['recency'], summary['T'])

    ggf = GammaGammaFitter(penalizer_coef=0)
    ggf.fit(summary['frequency'][summary['frequency'] > 0], summary['monetary_value'][summary['frequency'] > 0])

    summary['predicted_purchases'] = bgf.conditional_expected_number_of_purchases_up_to_time(
        90, summary['frequency'], summary['recency'], summary['T']).round().astype(int)

    summary['predicted_monetary'] = ggf.conditional_expected_average_profit(
        summary['frequency'], summary['monetary_value'])

    summary['CLV'] = ggf.customer_lifetime_value(
        bgf, summary['frequency'], summary['recency'],
        summary['T'], summary['monetary_value'], time=24, discount_rate=0.00
    )

    st.subheader("CLV Predictions Table")
    st.write(summary[['predicted_purchases', 'predicted_monetary', 'CLV']].head())


    clv_filtered = summary[summary['CLV'] < 10000]['CLV']
    p25, p50, p75 = np.percentile(clv_filtered, [25, 50, 75])

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(clv_filtered, bins=50, kde=True, color='skyblue')
    plt.axvline(p25, color='green', linestyle='--', label=f'25th %ile: {p25:.0f}')
    plt.axvline(p50, color='blue', linestyle='--', label=f'50th %ile: {p50:.0f} (Median)')
    plt.axvline(p75, color='red', linestyle='--', label=f'75th %ile: {p75:.0f}')
    plt.legend()
    ax.set_title("CLV Distribution")
    st.pyplot(fig)