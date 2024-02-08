import sys

sys.path.insert(0, 'config')
sys.path.insert(0, 'utils')
sys.path.insert(0, 'models')

import os
import config
from algorithm import Algorithm
from utils import import_data_as_pandas_dataframe


if __name__ == '__main__':
    f1_score_best = 0

    # Loop for training and testing the algorithm
    for iteration in range(0, 500):
        
        # Initialize the algorithm object with the specified parameters
        algorithm = Algorithm(
            train_data      = import_data_as_pandas_dataframe(os.path.join(config.dataset["path"], config.dataset["path_processed"]), config.dataset["path_train"]),
            test_data       = import_data_as_pandas_dataframe(os.path.join(config.dataset["path"], config.dataset["path_processed"]), config.dataset["path_test"]),
            vocab_size      = 100_000,
            embedding_dim   = 64,
            max_length      = 100,
            trunc_type      = "post",
            padding_type    = "post",
            oov_tok         = "<OOV>",
            optimizer       = "adam",
            loss            = "sparse_categorical_crossentropy",
            metric_names    = ["accuracy"],
            epochs          = 20,
            batch_size      = 64,
            model_path      = os.path.join(config.model["path"], config.model["path_model"], config.model["nnet"]["path"]),
            model_name      = config.model["nnet"]["name"]
        )

        # Train the algorithm
        algorithm.train()

        # Test the algorithm
        algorithm.model.test()
        algorithm.model.calculate_score()

        print(f"[INFO] Model with F1-Score: {algorithm.model.f1_score}")

        # Save the model if the F1-score is improved
        if algorithm.model.f1_score >= f1_score_best:
            algorithm.model.show_matrix()
            algorithm.save()
            
            f1_score_best = algorithm.model.f1_score
            
            print(f"[INFO] Saving model with F1-Score: {algorithm.model.f1_score}")