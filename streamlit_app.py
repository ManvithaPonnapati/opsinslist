import streamlit as st
import pandas as pd

# Define the path to your CSV file
csv_path = "all_extract.csv"  # Replace with the actual path to your CSV file
st.set_page_config(page_title="CSV Viewer", layout="wide", initial_sidebar_state="auto")

# Apply the light theme directly in the code
st.markdown(
    """
    <style>
        :root {
            --primary-color: #1E88E5;
            --background-color: #ffffff;
            --secondary-background-color: #f0f2f6;
            --text-color: #000000;
            --font: "sans serif";
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Channelrhodopsins DB")
st.text("Manvitha Ponnapati, Alex Naka")
key_column = "opsin"  # Replace with the actual key column name
column_to_add = "sequence"  # Replace with the column name you want to add from the secondary CSV

df2 = pd.read_csv("opsins.csv")
# Load the CSV file
df = pd.read_csv(csv_path)
  # Drop the query_id column
# df["mutation"] = df["unaligned_mutation"]
df = df.merge(df2[[key_column, column_to_add]], on=key_column, how="left")
df = df.drop(columns=["query_id"])

nice = ["more beneficial","more detrimental","neutral","Functional","Beneficial","Neutral"]
labels = []
for row in df.iterrows():
    if row[1]["functional"].upper() in [x.upper() for x in nice]:
        labels.append(1)
    else:
        labels.append(0)

# Display checkboxes for each row
#increase rows to display more rows
# Display the table with checkboxes
df["labels"] = labels
st.dataframe(df, height=1000,width=1000)
