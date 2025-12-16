import streamlit as st
import pandas as pd
from scoring import calculate_score

st.set_page_config(page_title="Lead Ranking Dashboard", layout="wide")

st.title("🔬 3D In-Vitro Lead Scoring Dashboard")

# Load data
df = pd.read_csv("leads_data.csv")

# Calculate score
df["Probability_Score"] = df.apply(calculate_score, axis=1)

# Rank leads
df = df.sort_values(by="Probability_Score", ascending=False)
df.insert(0, "Rank", range(1, len(df) + 1))

# Search
search = st.text_input("Search by Location, Title, Company")

if search:
    df = df[df.apply(lambda row: search.lower() in row.astype(str).str.lower().to_string(), axis=1)]

# Display table
st.dataframe(df, use_container_width=True)

# Download CSV
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Download as CSV",
    data=csv,
    file_name="ranked_leads.csv",
    mime="text/csv"
)
