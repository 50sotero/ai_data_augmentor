# Small Data Augmentor 🚀

A simple Streamlit app to enhance small datasets by generating synthetic rows using OpenAI's GPT models. Upload a CSV file, specify the number of rows to add, and download the augmented dataset.

## Features
✅ Upload a CSV file for augmentation  
✅ Specify the number of synthetic rows to generate  
✅ AI-generated data using OpenAI's GPT models  
✅ Download the augmented dataset as a CSV file  

## Installation

Ensure you have Python 3.7+ installed.

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/small_data_augmentor.git
   cd small_data_augmentor
   ```

2. Run the installation script:
   - On **Linux/MacOS**:
     ```bash
     bash install.sh
     ```
   - On **Windows**:
     ```bash
     install.bat
     ```

This will create a virtual environment and install the required dependencies from `requirements.txt`.

## Usage

1. Set up your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   Alternatively, you can store it in Streamlit secrets.

2. Run the Streamlit app:
   ```bash
   streamlit run small_data_augmentor.py
   ```

3. Open your web browser and navigate to the URL shown in the terminal.

## How It Works
1. Upload a CSV file 📂
2. Choose the number of synthetic rows to generate 🔢
3. Click on **Generate Synthetic Data** 🤖
4. Download the augmented dataset 📅

## Example Output
After processing, the app displays:
- **Original Dataset**: Preview of the uploaded CSV
- **Augmented Dataset**: Original dataset + synthetic rows
- **Download Option**: Button to download the new dataset

## Code Overview
The main logic includes:
- `file_uploader`: Uploads the user's CSV file
- `number_input`: Allows users to select the number of new rows
- `generate_synthetic_data`: Uses OpenAI to generate new rows
- `download_button`: Provides a CSV download link

## Notes
- The app assumes that OpenAI will generate synthetic data in a comma-separated format matching the original dataset's columns.
- Replace `text-davinci-003` with the appropriate OpenAI model if needed.
- Ensure you have a valid OpenAI API key before running the app.

## License
This project is licensed under the MIT License.

---

Enjoy augmenting your datasets! 🚀

