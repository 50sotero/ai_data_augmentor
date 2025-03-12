import streamlit as st
import pandas as pd
import os
from openai import OpenAI
import csv
from io import StringIO
from sklearn.impute import KNNImputer

# App title and description
st.title("ai_data_augmentor 🚀")
st.write("""
Enhance small datasets by generating synthetic rows or imputing missing values using AI and ML techniques. 
Upload a CSV file, choose an action, and download the modified dataset.
""")

# Sidebar for user inputs
st.sidebar.header("Settings")
task_choice = st.sidebar.selectbox("Choose a task 🛠️", ["Add Synthetic Rows", "Replace Nulls with KNN Imputation"])
model_choice = st.sidebar.selectbox("Choose a model 🤖", ["GPT-4", "DeepSeek r-1"]) if task_choice == "Add Synthetic Rows" else None
num_rows = st.sidebar.number_input("Number of rows to add 🔢", min_value=1, max_value=100, value=5) if task_choice == "Add Synthetic Rows" else None
uploaded_file = st.sidebar.file_uploader("Upload a CSV file 📂", type=["csv"])

# Configure API client based on model selection
if model_choice == "GPT-4":
    api_key = st.secrets["openai"]["api_key"]
    model_engine = "gpt-4o-mini"
    client = OpenAI(api_key=api_key)
elif model_choice == "DeepSeek r-1":
    api_key = st.secrets["deepseek"]["api_key"]
    model_engine = "deepseek-chat"
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")

# Function to generate synthetic data using the selected model
def generate_synthetic_data(prompt, model_engine):
    try:
        response = client.chat.completions.create(
            model=model_engine,
            messages=[
                {"role": "system", "content": "You are a helpful data assistant. Generate realistic synthetic data in CSV format."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7,
            top_p=0.9
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"API Error: {str(e)}")
        return ""

# Enhanced ID detection: Check for integer type and "id" in the column name
def detect_id_column(df):
    for col in df.columns:
        if 'id' in col.lower() and pd.api.types.is_integer_dtype(df[col]):
            return col  # Return the column name if it matches both criteria
    return None

# Function for KNN imputation
def knn_impute(df, n_neighbors=3):

    # Proceed with KNN imputation
    imputer = KNNImputer(n_neighbors=n_neighbors)
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    return df


# Main app logic
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, sep=None, engine='python')
        st.success("CSV file successfully uploaded and read! 🎉")
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        st.stop()

    st.write("### Original Dataset:")
    st.dataframe(df)

    # Task 1: Add Synthetic Rows
    if task_choice == "Add Synthetic Rows":
        id_column = detect_id_column(df)
        if id_column:
            st.info(f"Detected ID column: **{id_column}**")
        else:
            st.info("No dedicated ID column detected. Rows will be appended without ID modifications.")

        if st.button("Generate Synthetic Data 🤖"):
            st.write("### Augmentation Progress:")
            progress_bar = st.progress(0)
            status_text = st.empty()

            with st.spinner("Generating synthetic data... ⏳"):
                recent_data = df.tail(3).to_csv(index=False)
                id_instruction = f"- Start IDs from {df[id_column].max() + 1}" if id_column else "- No ID generation needed"
                prompt = f"""Generate {num_rows} unique synthetic rows similar to the dataset below:
{recent_data}

Ensure the following:
{id_instruction}
- Maintain consistent data types and formats
- Add realistic variations to categorical values
- Keep numerical values within observed ranges
Output only the CSV data without any additional text or headers."""

                ai_response = generate_synthetic_data(prompt, model_engine)

            if not ai_response:
                st.error("Failed to generate synthetic data")
                st.stop()

            # Process AI response
            synthetic_rows = [row.strip() for row in ai_response.split("\n") if row.strip()]
            synthetic_rows = [row for row in synthetic_rows if ',' in row and not row.lower().startswith("book_id")]

            processed_rows = []
            max_id = df[id_column].max() if id_column else None

            for idx, row in enumerate(synthetic_rows[:num_rows], start=1):
                progress_bar.progress(idx / num_rows)
                status_text.text(f"Processing row {idx} of {num_rows}...")

                try:
                    parsed_row = next(csv.reader(StringIO(row)))

                    if id_column:
                        id_index = df.columns.get_loc(id_column)
                        parsed_row[id_index] = str(max_id + idx)

                    if len(parsed_row) != len(df.columns):
                        raise ValueError(f"Column mismatch: Expected {len(df.columns)} columns, got {len(parsed_row)}")

                    processed_rows.append(parsed_row)
                    st.write(f"✅ Row {idx}: {parsed_row}")
                except Exception as e:
                    st.warning(f"⚠️ Skipping invalid row: {row} | Error: {str(e)}")

            if processed_rows:
                synthetic_df = pd.DataFrame(processed_rows, columns=df.columns)

                for col in df.columns:
                    try:
                        synthetic_df[col] = synthetic_df[col].astype(df[col].dtype)
                    except Exception as e:
                        st.warning(f"Type conversion failed for {col}: {str(e)}")
                        synthetic_df[col] = synthetic_df[col].astype('object')

                augmented_df = pd.concat([df, synthetic_df], ignore_index=True)

                st.success(f"✅ Successfully added {len(processed_rows)} synthetic rows!")
                st.write("### Augmented Dataset:")
                st.dataframe(augmented_df)

                csv_data = augmented_df.to_csv(index=False).encode("utf-8")
                st.download_button("Download Augmented Dataset 📥", data=csv_data, file_name="augmented_dataset.csv", mime="text/csv")
            else:
                st.error("❌ No valid synthetic rows generated. Please try again.")

    # Task 2: Replace Nulls with KNN Imputation
    elif task_choice == "Replace Nulls with KNN Imputation":
        if st.button("Run KNN Imputation 🔄"):

            # Check if any null values exist in numeric columns
            numeric_cols = df.select_dtypes(include=['number']).columns
            if df[numeric_cols].isnull().any().any():
                with st.spinner("Imputing missing values using KNN... ⏳"):
                    imputed_df = knn_impute(df)
                    st.success("✅ Missing values successfully imputed using KNN!")
                    st.write("### Imputed Dataset:")
                    st.dataframe(imputed_df)

                    csv_data = imputed_df.to_csv(index=False).encode("utf-8")
                    st.download_button("Download Imputed Dataset 📥", data=csv_data, file_name="imputed_dataset.csv", mime="text/csv")

            else:
                st.info("No null values detected in numeric columns. Imputation is not required.")
                pass

else:
    st.info("Please upload a CSV file to get started.")
