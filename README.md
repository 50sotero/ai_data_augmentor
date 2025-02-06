# AI Data Augmentor 🚀

A **Streamlit app** that enhances small datasets by generating **synthetic rows** using AI models like **OpenAI's GPT-4** and **DeepSeek r-1**. The app intelligently detects ID columns and ensures consistent data formatting, making it perfect for augmenting datasets of any structure.

---

## Features

✅ Upload a **CSV** file for data augmentation  
✅ Choose between **OpenAI GPT-4** and **DeepSeek r-1** models  
✅ Automatically detect and increment **ID columns**  
✅ Specify the **number of synthetic rows** to generate  
✅ Maintain **data types** and **formats** dynamically  
✅ Download the **augmented dataset** as a CSV file  

---

## Installation

Ensure you have **Python 3.7+** installed.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai_data_augmentor.git
   cd ai_data_augmentor
   ```

2. **Install the required dependencies**:
   ```bash
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
2. **Choose a model**: GPT-4 or DeepSeek r-1 🤖
3. **Specify the number of rows** to generate 🔢
4. The app detects any **ID columns** and increments them automatically
5. Click **Generate Synthetic Data** and preview the **augmented dataset**
6. **Download** the final augmented dataset as a CSV 📥

---

## Example Output

After processing, the app displays:
- **Original Dataset**: Preview of the uploaded CSV file
- **Augmented Dataset**: Original data + synthetic rows
- **Download Option**: Button to download the augmented CSV file

---

## Code Overview

- **File Upload**: `st.file_uploader()` for CSV input  
- **Model Selection**: Choose between **GPT-4** and **DeepSeek r-1**  
- **ID Detection**:  
  - Dynamically detects ID columns if:
    - The **column name contains "id"** (case-insensitive)
    - The column is of **integer type**
- **Synthetic Data Generation**:  
  - The `generate_synthetic_data()` function uses the selected AI model to create new rows.
  - Ensures consistent **data types** and **formats** across all columns.
- **Download Button**: Provides a CSV download link for the augmented dataset.

---

## Notes

- The app **automatically detects** ID columns and increments them if needed.  
- Ensure your API keys for **OpenAI** and **DeepSeek** are correctly configured in `.streamlit/secrets.toml`.  
- If no ID column is detected, the app will append rows **without modifying any columns**.

---

## License

This project is licensed under the **MIT License**.
