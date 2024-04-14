# Emotion Recognition

This folder contains the labeled datasets and code to train the classification models 
**NOTE: the code was run using Google Colab T4 GPU and the models are hosted in Huggingface Hub. To run and save the model, changes to the code are required as the models are hosted using a personal huggingface account**
- **CZ4034_Classification.ipynb:**
  The main notebook used to train the DistilBERT model and classify the final dataset with metrics displayed<br><br/>
- **Hyperparameter_Tuning.ipynb:**
  The notebook used to tune hyperparameters (learning rate, weight decay, batch size) with 5-fold cross validation<br><br/>
- **Stacked_Ensemble.ipynb:**
  The notebook used to train and ensemble 3 models (GPT-2, BERT and DistilBERT)<br><br/>
- **Stratified_Sampling.ipynb:**
  The notebook used to pick a small subset of lyrics from the unlabelled crawled dataset as proportionally represented by genre and emotions<br><br/>
- **eval_labeled_lyrics.csv:**
  1102 rows of manually labelled data for evaluation<br><br/>
- **train_labeled_lyrics.csv:**
  1117 rows of manually labelled data for training<br><br/>
- **final_labeled_dataset.csv:**
  20,799 rows of data in total labelled using the fine-tuned DistilBERT model<br><br/>

### EMOTION LABELS

    "0": "serenity",
    "1": "joy",
    "2": "ecstasy",
    "3": "love",
    "4": "acceptance",
    "5": "trust",
    "6": "admiration",
    "7": "submission",
    "8": "apprehension",
    "9": "fear",
    "10": "terror",
    "11": "awe",
    "12": "distraction",
    "13": "surprise",
    "14": "amazement",
    "15": "disapproval",
    "16": "pensiveness",
    "17": "sadness",
    "18": "grief",
    "19": "remorse",
    "20": "boredom",
    "21": "disgust",
    "22": "loathing",
    "23": "contempt",
    "24": "annoyance",
    "25": "anger",
    "26": "rage",
    "27": "aggressiveness",
    "28": "interest",
    "29": "anticipation",
    "30": "vigilance",
    "31": "optimism"

### Intensity Labels:

    "0": "low",
    "1": "medium",
    "2": "high",
    "3": "medium",
    "4": "low",
    "5": "medium",
    "6": "high",
    "7": "medium",
    "8": "low",
    "9": "medium",
    "10": "high",
    "11": "medium",
    "12": "low",
    "13": "medium",
    "14": "high",
    "15": "medium",
    "16": "low",
    "17": "medium",
    "18": "high",
    "19": "medium",
    "20": "low",
    "21": "medium",
    "22": "high",
    "23": "medium",
    "24": "low",
    "25": "medium",
    "26": "high",
    "27": "medium",
    "28": "low",
    "29": "medium",
    "30": "high",
    "31": "medium"

