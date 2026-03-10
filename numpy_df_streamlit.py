import numpy as np
import pandas as pd
import streamlit as st
num_rows = 5
data = []

st.write("# Random Data Generator")

# Add streamlit slider
num_rows = st.slider("Number of rows", 1, 10000, 500)

# Set numpy random seed (using 42 as an example between 2-50)
np.random.seed(42)

data = []
for i in range(num_rows):
    data.append(
        {
            "Preview": f"https://picsum.photos/400/200?lock={i}",
            "Views": np.random.randint(0, 1000),
            "Active": np.random.choice([True, False]),
            "Category": np.random.choice(["🤖 LLM", "📊 Data", "⚙️ Tool"]),
            "Progress": np.random.randint(1, 100),
        }
    )

# Convert the 'data' into a DataFrame object
df = pd.DataFrame(data)

# Configure streamlit image and progress column
# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Preview Image")
    # Display the first image as an example
    st.image(df.iloc[0]["Preview"], caption="Sample Preview Image")

with col2:
    st.subheader("Progress Overview")
    # Display progress bars for first few rows
    for idx, row in df.head(5).iterrows():
        st.progress(row["Progress"] / 100, text=f"Row {idx}: {row['Progress']}%")

# Display the DataFrame
st.subheader("Generated Data")
st.dataframe(df)

df = pd.DataFrame(data)

config = {
    "Preview": st.column_config.ImageColumn(),
    "Progress": st.column_config.ProgressColumn(),
}

if st.toggle("Enable editing"):
    edited_data = st.data_editor(df, column_config=config, use_container_width=True)
else:
    st.dataframe(df, column_config=config, use_container_width=True)

st.subheader("Top 10 Views")
st.line_chart(df["Views"].head(10))

