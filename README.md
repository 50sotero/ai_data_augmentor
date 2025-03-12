# AI Data Augmentor 🚀

A **Streamlit app** that enhances small datasets by generating **synthetic rows** using AI models like **OpenAI's GPT-4** and **DeepSeek r-1**, and by **imputing missing values** in numeric columns using **KNN imputation**. The app intelligently detects ID columns, ensures consistent data formatting, and handles missing data, making it perfect for comprehensive dataset augmentation.

---

## Features

✅ Upload a **CSV** file for data augmentation  
✅ Choose between:
   - **Adding Synthetic Rows** using AI models 🤖 **
     
✅ Automatically detect and increment **ID columns**  
✅ Maintain **data types** and **formats** dynamically  
✅ Download the **augmented dataset** as a CSV file  
   - **Replacing Null Values** in numeric columns using **KNN Imputation** 🔄  

---

## Installation

Ensure you have **Python 3.7+** installed.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai_data_augmentor.git
   cd ai_data_augmentor
   ```

2. **Activate venv & install the required dependencies**:
   ```bash
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

## Configuration

1. **Set up your API keys**:
   - **OpenAI GPT-4**:
     - Create a `.streamlit/secrets.toml` file and add your OpenAI API key:
       ```toml
       [openai]
       api_key = "your-openai-api-key"
       ```
   - **DeepSeek r-1**:
     - Add your DeepSeek API key:
       ```toml
       [deepseek]
       api_key = "your-deepseek-api-key"
       ```

2. **Run the Streamlit app**:
   ```bash
   streamlit run ai_data_augmentor.py
   ```

3. Open your browser and navigate to the **local URL** provided in the terminal.

---

## How It Works

1. **Upload a CSV file** 📂
2. **Choose a task**:
   - **Add Synthetic Rows**: Generate new rows using AI models 🤖  
   - **Replace Nulls with KNN Imputation**: Automatically impute missing values 🔄  
3. **Specify parameters** (e.g., number of rows to add or neighbors for KNN)
4. The app detects any **ID columns** and manages data types dynamically
5. Preview the **augmented dataset** and **download** the results

---

## Example Output

After processing, the app displays:
- **Original Dataset**: Preview of the uploaded CSV file
- **Augmented Dataset**: Original data with synthetic rows or imputed values
- **Download Option**: Button to download the modified CSV file

---

## Code Overview

- **File Upload**: `st.file_uploader()` for CSV input  
- **Task Selection**: Choose between synthetic row generation or KNN imputation  
- **ID Detection**:  
  - Detects ID columns if:
    - The **column name contains "id"** (case-insensitive)
    - The column is of **integer type**
- **Synthetic Data Generation**:  
  - The `generate_synthetic_data()` function uses AI models to create new rows
- **KNN Imputation**:  
  - The `knn_impute()` function replaces missing values in numeric columns using **K-Nearest Neighbors**  
  - Includes a pre-check to ensure **null values** exist before imputation
- **Download Button**: Provides a CSV download link for the augmented dataset

---

## Notes

- The app **automatically detects** ID columns and increments them when generating new rows.  
- Ensure your API keys for **OpenAI** and **DeepSeek** are correctly configured in `.streamlit/secrets.toml`.  
- The app will **skip KNN imputation** if no null values are detected in numeric columns.  
- If no ID column is detected, the app will append rows **without modifying any columns**.

---

## License

This project is licensed under the **MIT License**.

---

Enjoy augmenting and cleaning your datasets with AI & ML! 🚀
