import sys

sys.path.insert(0, 'config')
sys.path.insert(0, 'utils')

import os
import config
import joblib
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import import_data_as_pandas_dataframe, print_matrix, create_path

class Algorithm(object):
    def __init__(self, *, train_data, test_data, model_name, model_path):
        """
        Initialize the Algorithm class with training and testing data.

        Parameters:
        - train_data: Pandas DataFrame containing training data
        - test_data: Pandas DataFrame containing testing data
        - model_name: Name of the model
        - model_path: Path to save the model
        """
        
        self.train_data = train_data
        self.test_data = test_data
        self.model_name = model_name
        self.model_path = model_path

        # Initialize Support Vector Machine (SVM) model with a linear kernel
        self.model = SVC(kernel = 'linear')
        
        # Initialize TF-IDF tokenizer for text data
        self.tokenizer = TfidfVectorizer()

    def run(self):
        """
        Train the SVM model using the TF-IDF transformed features of the training data.
        """
        
        features_train_data = self.tokenizer.fit_transform(self.train_data['feature'])
        labels_train_data = self.train_data['label']

        # Fit the SVM model
        self.model.fit(features_train_data, labels_train_data)

    def calculate_score(self) -> None:
        """
        Compute evaluation metrics such as accuracy, precision, recall, and F1-score.
        """
        
        # Calculate metrics
        true_labels = []
        predicted_labels = []

        for true_label, prediction_dict in self.results_predictions.items():
            for predicted_label, count in prediction_dict.items():
                true_labels.extend([true_label] * count)
                predicted_labels.extend([predicted_label] * count)

        # Initialize variables
        true_positives = 0
        false_positives = 0
        false_negatives = 0
        total_samples = len(true_labels)

        # Calculate true positives, false positives, and false negatives
        for true_label, predicted_label in zip(true_labels, predicted_labels):
            if true_label == predicted_label:
                true_positives += 1
            else:
                if predicted_label == 'positive':
                    false_positives += 1
                else:
                    false_negatives += 1

        # Calculate metrics
        self.accuracy = true_positives / total_samples
        self.precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
        self.recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
        self.f1_score = 2 * (self.precision * self.recall) / (self.precision + self.recall) if (self.precision + self.recall) > 0 else 0
    
    def test(self) -> None:
        """
        Test the trained model on the test dataset and calculate evaluation metrics.
        """
        
        labels_test_data = self.test_data['label'].values
        features_test_data = self.test_data['feature'].values

        # Tokenization
        tokens_test_data = self.tokenizer.transform(features_test_data)

        # Predictions
        predictions = [self.model.predict(text) for text in tokens_test_data]

        # Generate matrix
        self.results_predictions = {label: {item: 0 for item in labels_test_data} for label in set(labels_test_data)}

        for test, expected_category, predicted_category in zip(features_test_data, labels_test_data, predictions):
            self.results_predictions[expected_category][predicted_category[0]] += 1
        
    def save(self) -> None:
        """
        Save the trained model to a specified file path.
        """

        print(f"[INFO] Saving the model to {self.model_name}")

        create_path(self.model_path)
                
        joblib.dump(self.model, os.path.join(self.model_path, self.model_name))
        joblib.dump(self.tokenizer, os.path.join(self.model_path, "tokenizer.joblib"))
        
        print("[INFO] Model saved successfully")
    
    def show_matrix(self) -> None:
        """
        Print the confusion matrix.
        """
        
        print_matrix(self.results_predictions, 15)

if __name__ == '__main__':
    # Initialize Algorithm instance with training and testing data
    algorithm = Algorithm(
        train_data      = import_data_as_pandas_dataframe(os.path.join(config.dataset["path"], config.dataset["path_processed"]), config.dataset["path_train"]),
        test_data       = import_data_as_pandas_dataframe(os.path.join(config.dataset["path"], config.dataset["path_processed"]), config.dataset["path_test"]),
        model_name      = config.model["svm"]["name"],
        model_path      = os.path.join(config.model["path"], config.model["path_model"], config.model["svm"]["path"])
    )

    algorithm.run()
    algorithm.test()
    algorithm.calculate_score()
    algorithm.show_matrix()
    algorithm.save()

    print(f"[INFO] Saving model with F1-Score: {algorithm.f1_score}")