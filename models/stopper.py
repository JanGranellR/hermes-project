from tensorflow import keras

class CustomStopper(keras.callbacks.Callback):
    """
    Custom Callback to stop training early if the performance metric does not improve.
    """
    
    def __init__(self):
        """
        Initializes the CustomStopper callback.
        """

        super(CustomStopper, self).__init__()
        
        # Initialize the best score to negative infinity and best weights to None
        self.best_score = float('-inf')
        self.best_weights = None

    def on_epoch_begin(self, epoch: int, logs: dict = None):
        """
        Callback at the beginning of each epoch.
        
        Args:
            epoch (int): The current epoch index.
            logs (dict or None): Dictionary of logs containing metrics for the current epoch.
        """

        # Perform testing and calculate the score using the model
        self.model.test()
        self.model.calculate_score()

        # Obtain the current F1 score
        current_score = self.model.f1_score

        # Update the best score and weights if the current score is greater or equal
        if current_score >= self.best_score:
            self.best_score = current_score
            self.best_weights = self.model.get_weights()
        else:
            # Stop training if the current score is less than the best score
            self.model.stop_training = True
            
            # Restore the best weights if available
            if self.best_weights is not None:
                self.model.set_weights(self.best_weights)
                        
    def on_train_end(self, logs: dict = None):
        """
        Callback at the end of training.

        Args:
            logs (dict or None): Dictionary of logs containing metrics at the end of training.
        """

        # Set the model weights to the best weights obtained during training
        self.model.set_weights(self.best_weights)