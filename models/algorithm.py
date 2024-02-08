import sys

sys.path.insert(0, 'utils')
sys.path.insert(0, 'models')

import os
import json
import numpy as np
import pandas as pd
from tensorflow import keras
from stopper import CustomStopper
from model import CustomModel
from label_encoder import LabelEncoder
from utils import print_matrix, create_path

class Algorithm(object):
    """
    Class representing an algorithm for text classification.
    """

    def __init__(self, *, train_data: pd.DataFrame, test_data: pd.DataFrame, vocab_size: int, embedding_dim: int, max_length: int, trunc_type: str, padding_type: str, oov_tok: str, optimizer: str, loss: str, metric_names: list[str], epochs: int, batch_size: int, model_path: str, model_name: str) -> None:
        """
        Initialize the Algorithm object with specified parameters.

        Parameters:
        - train_data (pd.DataFrame): DataFrame containing the training data.
        - test_data (pd.DataFrame): DataFrame containing the testing data.
        - vocab_size (int): Size of the vocabulary.
        - embedding_dim (int): Dimension of word embeddings.
        - max_length (int): Maximum length of input sequences.
        - trunc_type (str): Truncation type for sequences.
        - padding_type (str): Padding type for sequences.
        - oov_tok (str): Token for out-of-vocabulary words.
        - optimizer (str): Optimization algorithm for training.
        - loss (str): Loss function for training.
        - metric_names (list of str): Metrics used for evaluation.
        - epochs (int): Number of epochs for training.
        - batch_size (int): Batch size for training.
        - model_path (str): Path to save the trained model.
        - model_name (str): Name of the trained model.
        """

        # Data
        self.train_data = train_data
        self.test_data = test_data

        # Hyperparameters
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.max_length = max_length
        self.trunc_type = trunc_type
        self.padding_type = padding_type
        self.oov_tok = oov_tok
        self.optimizer = optimizer
        self.loss = loss
        self.metric_names = metric_names
        self.epochs = epochs
        self.batch_size = batch_size
        
        # Save
        self.model_path = model_path
        self.model_name = model_name

        # Tokenizer
        self.tokenizer = None

    def train(self) -> None:
        """
        Train the model using the provided training data.
        """

        labels_train_data = LabelEncoder(self.train_data['label'].values).fit_transform() # Encode labels to numbers
        features_train_data = self.train_data['feature'].values

        # Save labels as dictionary
        labels_number = list(set(labels_train_data))
        labels_string = list(set(self.train_data['label'].values))

        self.labels_dict = {labels_number[i]: labels_string[i] for i in range(len(labels_number))}

        # Tokenization
        self.tokenizer = keras.preprocessing.text.Tokenizer(num_words = self.vocab_size, split = " ", oov_token = self.oov_tok)
        self.tokenizer.fit_on_texts(features_train_data)

        tokens_train_data = self.tokenizer.texts_to_sequences(features_train_data)

        # Truncate
        truncated_train_data = keras.preprocessing.sequence.pad_sequences(tokens_train_data, maxlen = (self.max_length))

        # Layers
        # TODO: Maybe parameterize this??
        self.model = CustomModel(self.test_data, self.labels_dict, self.tokenizer, self.max_length)
        self.model.add(keras.layers.Embedding(self.vocab_size, self.embedding_dim, input_length = self.max_length))
        self.model.add(keras.layers.Bidirectional(keras.layers.LSTM(64, return_sequences = True)))
        self.model.add(keras.layers.Conv1D(256, 5, activation="relu"))
        self.model.add(keras.layers.MaxPooling1D(5))
        self.model.add(keras.layers.Conv1D(256, 5, activation="relu"))
        self.model.add(keras.layers.GlobalMaxPooling1D())
        self.model.add(keras.layers.Dense(512, activation="relu"))
        self.model.add(keras.layers.Dropout(0.5))
        self.model.add(keras.layers.Dense(256, activation="relu"))
        self.model.add(keras.layers.Dropout(0.5))
        self.model.add(keras.layers.Dense(128, activation="relu"))
        self.model.add(keras.layers.Dropout(0.5))
        self.model.add(keras.layers.Dense(len(set(labels_train_data)), activation = "softmax"))

        # Compilation
        self.model.compile(optimizer = self.optimizer, loss = self.loss, metrics = self.metric_names)

        # Custom stopper
        custom_stopper = CustomStopper()

        # Actual training
        self.model.fit(truncated_train_data, labels_train_data, epochs = self.epochs, batch_size = self.batch_size, callbacks = [custom_stopper])

    def save(self) -> None:
        """
        Save the model, tokenizer, and label dictionary to files.
        """
        
        create_path(self.model_path)  # Ensure that the model path exists

        # Save the model
        self.model.save(os.path.join(self.model_path, self.model_name))

        # Save the tokenizer as a JSON file
        with open(os.path.join(self.model_path, "tokenizer.json"), "w") as json_file:
            json_file.write(self.tokenizer.to_json())

        # Convert label dictionary keys to integers and save as JSON
        str_labels_dict = {int(key): value for key, value in self.labels_dict.items()}
        
        with open(os.path.join(self.model_path, "labels.json"), "w") as json_file:
            json.dump(str_labels_dict, json_file)
