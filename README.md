# End-to-End Twitter Sentiment Analysis

An end-to-end deep learning project that trains and serves a Twitter sentiment classifier for three classes: Negative, Neutral, and Positive.

The repository includes:

- Data preparation and model training in a Jupyter notebook.
- A saved Keras model and tokenizer for inference.
- A Streamlit web app for real-time tweet sentiment prediction.

## Repository Description (for GitHub)

End-to-end Twitter sentiment analysis using TensorFlow/Keras and Streamlit, with training notebook, saved tokenizer/model artifacts, and live web inference for Negative/Neutral/Positive classes.

## Key Features

- Multi-class sentiment classification (Negative, Neutral, Positive).
- Tokenization and sequence modeling with Keras.
- Pretrained model artifacts ready for inference.
- Simple interactive Streamlit UI.
- Reproducible workflow from notebook training to deployment.

## Project Structure

- RNN/project.ipynb: Full training and experimentation workflow.
- RNN/main.py: Streamlit inference app.
- RNN/tokenizer.pkl: Saved tokenizer used for inference.
- RNN/sentiment_analysis_model.keras: Trained Keras model.
- RNN/twitter_training.csv: Training dataset.
- RNN/twitter_validation.csv: Validation dataset.

Note: This workspace also contains other deep learning experiments and apps. The sentiment analysis flow is under the RNN directory.

## Tech Stack

- Python
- TensorFlow/Keras
- scikit-learn
- NumPy, Pandas
- Streamlit

## Setup

1. Clone the repository.
2. Move into the repository root.
3. Create and activate a virtual environment.
4. Install dependencies.

Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r RNN/requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r RNN/requirements.txt
```

## Run the Sentiment App

From the repository root:

```bash
cd RNN
streamlit run main.py
```

Open the local URL shown by Streamlit (usually http://localhost:8501).

## Training Workflow

1. Open RNN/project.ipynb.
2. Run data cleaning and preprocessing cells.
3. Train the model.
4. Save artifacts:
	- sentiment_analysis_model.keras
	- tokenizer.pkl
5. Launch the Streamlit app for inference.

## Current Output Labels

- 0: Negative
- 1: Neutral
- 2: Positive

## Suggested Improvements

- Add confidence-based output and uncertainty handling in the app.
- Add text normalization and stricter preprocessing parity between training and inference.
- Improve robustness with hard-negative examples and broader evaluation metrics (macro F1, confusion matrix).

## License

This project is licensed under the terms in LICENSE.
