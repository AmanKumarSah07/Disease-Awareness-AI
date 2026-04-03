# Disease Awareness and Prevention AI Agent 🩺

An AI-powered health assistant built with **Streamlit**, **LangChain**, and **Hugging Face**. This application serves as a preliminary health awareness tool to help users understand possible causes of symptoms, assess disease risks, and learn prevention strategies.

> ⚠️ **Disclaimer:** This tool is for educational and awareness purposes only. It does not replace a doctor and cannot provide professional medical diagnoses. Always consult a healthcare professional for medical advice.

## Features
- Interactive chat interface indicating symptom input
- General health query answering
- Educational advice regarding prevention and wellness
- Secure HuggingFace API key integration within the application structure

## Prerequisites
- **Python 3.8+**
- A free [Hugging Face Access Token](https://huggingface.co/settings/tokens)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AmanKumarSah07/Disease-Awareness-AI.git
   cd Disease-Awareness-AI
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables (Optional):**
   You can supply your Hugging Face API token in a `.env` file at the root of the project:
   ```env
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   ```
   Or securely enter it directly into the Streamlit sidebar when the app runs.

## Running the Application

Execute the following command to start the Streamlit server:

```bash
streamlit run app.py
```

The application should automatically open in your default browser at `http://localhost:8501`.

## File Structure

- `app.py`: The main Streamlit web application.
- `agent.py`: Contains LangChain mechanics and HuggingFace connection.
- `test_api.py`: Script to quickly test API configurations.
- `requirements.txt`: Python package dependencies.
