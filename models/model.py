import sys

sys.path.insert(0, 'utils')

import numpy as np
from tensorflow import keras
from utils import print_matrix

class CustomModel(keras.Sequential):
    """
    Class representing a custom Sequential model.
    """

    # TODO: Add types to functions
    def __init__(self, test_data = None, labels_dict = None, tokenizer = None, max_length = None, *args, **kwargs) -> None:
        """
        Initializes the CustomModel.

        Args:
        - test_data (DataFrame): DataFrame containing test data.
        - labels_dict (dict): Dictionary mapping label indices to label names.
        - tokenizer (Tokenizer): Tokenizer object.
        - max_length (int): Maximum length for sequences.
        """

        super(CustomModel, self).__init__(*args, **kwargs)

        # Initialize instance variables
        self.test_data = test_data
        self.labels_dict = labels_dict
        self.tokenizer = tokenizer
        self.max_length = max_length

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
        tokens_test_data = self.tokenizer.texts_to_sequences(features_test_data)

        # Truncate
        truncated_test_data = keras.preprocessing.sequence.pad_sequences(tokens_test_data, maxlen=self.max_length)

        # Predictions
        predictions = np.argmax(self.predict(truncated_test_data), axis=1)
        predicted_categories = [self.labels_dict[i] for i in predictions]

        # Generate matrix
        self.results_predictions = {label: {item: 0 for item in labels_test_data} for label in set(labels_test_data)}

        for test, expected_category, predicted_category in zip(features_test_data, labels_test_data, predicted_categories):
            self.results_predictions[expected_category][predicted_category] += 1

    def show_matrix(self) -> None:
        """
        Print the confusion matrix.
        """
        
        print_matrix(self.results_predictions, 15)
