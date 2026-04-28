# End-to-End Twitter Sentiment Analysis

This repository contains an end-to-end deep learning project for Twitter sentiment classification. It includes the cleaned dataset, raw source data, training notebooks, a saved Keras model, a saved tokenizer, and a Streamlit application for real-time sentiment prediction.

The model predicts one of three sentiment classes:

- Negative
- Neutral
- Positive

## Project Overview

The goal of this project is to build a complete sentiment analysis workflow, starting from dataset preparation and model training, then saving the trained model artifacts, and finally serving predictions through a simple web interface.

The main workflow is:

1. Prepare and clean the Twitter sentiment dataset.
2. Tokenize tweet text and convert it into padded sequences.
3. Train a deep learning model using TensorFlow/Keras.
4. Save the trained model and tokenizer.
5. Load the saved artifacts in a Streamlit app.
6. Predict sentiment for user-entered tweets.

## Model Performance

Final training result:

```text
Epoch 50/50
9081/9081 - 156s - 17ms/step
accuracy: 0.9680
loss: 0.1036
val_accuracy: 0.9621
val_loss: 0.1467
```

This means the trained model reached approximately 96.80% training accuracy and 96.21% validation accuracy at the end of training.

## Repository Structure

```text
.
├── data/
│   └── dataset.csv
├── models/
│   ├── sentiment_analysis_model.keras
│   └── tokenizer.pkl
├── notebooks/
│   ├── main_project.ipynb
│   └── project.ipynb
├── raw_data/
│   ├── twitter_final_Dataset.csv
│   ├── twitter_final_Dataset.csv.zip
│   ├── twitter_training.csv
│   └── twitter_validation.csv
├── main.py
├── README.md
└── LICENSE
```

## Folder Details

### `data/`

Contains the main cleaned dataset used by the project.

- `dataset.csv`: Primary dataset file kept inside the `data` folder.

### `models/`

Contains trained model artifacts used by the prediction app.

- `sentiment_analysis_model.keras`: Saved TensorFlow/Keras sentiment analysis model.
- `tokenizer.pkl`: Saved tokenizer used to convert input text into model-ready sequences.

### `notebooks/`

Contains the experimentation and training notebooks.

- `project.ipynb`: Notebook for model development and experimentation.
- `main_project.ipynb`: Main notebook for the project workflow.

### `raw_data/`

Contains raw or source dataset files used during experimentation and dataset preparation.

- `twitter_training.csv`
- `twitter_validation.csv`
- `twitter_final_Dataset.csv`
- `twitter_final_Dataset.csv.zip`

### `main.py`

Streamlit application for loading the saved model and tokenizer, accepting a tweet as input, and returning the predicted sentiment.

## Tech Stack

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- scikit-learn
- Streamlit
- Git LFS

## Git LFS

Large files are tracked with Git LFS, including datasets and trained model artifacts.

Tracked large files include:

- `data/dataset.csv`
- `models/sentiment_analysis_model.keras`
- `models/tokenizer.pkl`
- `raw_data/*.csv`
- `raw_data/*.zip`

After cloning the repository, install Git LFS and pull the large files:

```bash
git lfs install
git lfs pull
```

## Setup

Clone the repository:

```bash
git clone git@github.com:dharmender12/end-to-end-twitter-sentiment-analysis.git
cd end-to-end-twitter-sentiment-analysis
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required Python packages:

```bash
pip install tensorflow keras numpy pandas scikit-learn streamlit
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install tensorflow keras numpy pandas scikit-learn streamlit
```

## Run the Streamlit App

From the repository root, run:

```bash
streamlit run main.py
```

The app will open in the browser, usually at:

```text
http://localhost:8501
```

Enter a tweet in the text box and click `Predict Sentiment` to get the predicted class.

## Inference Flow

The Streamlit app performs these steps:

1. Loads `models/sentiment_analysis_model.keras`.
2. Loads `models/tokenizer.pkl`.
3. Accepts a tweet from the user.
4. Converts the tweet into a sequence using the saved tokenizer.
5. Pads the sequence to length `99`.
6. Runs model prediction.
7. Maps the predicted class index to a sentiment label.

Current label mapping:

```python
{
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}
```

## Training Workflow

To reproduce or modify the training process:

1. Open the notebooks inside the `notebooks/` folder.
2. Load the dataset from `data/` or `raw_data/`.
3. Clean and preprocess tweet text.
4. Tokenize text data.
5. Convert text into padded sequences.
6. Train the sentiment classification model.
7. Save the model to `models/sentiment_analysis_model.keras`.
8. Save the tokenizer to `models/tokenizer.pkl`.
9. Run `main.py` to test predictions in the Streamlit app.

## Notes

- The repository no longer uses an `RNN/` folder.
- The `data/` folder is intentionally kept clean and contains only `dataset.csv`.
- Model files are stored in the top-level `models/` folder.
- Training notebooks are stored in the top-level `notebooks/` folder.
- Raw and additional dataset files are stored separately in `raw_data/`.

## License

This project is licensed under the terms of the `LICENSE` file.
