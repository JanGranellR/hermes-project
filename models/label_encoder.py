import numpy as np

class LabelEncoder:
    """
    Class for encoding categorical labels into numerical values.
    """

    def __init__(self, labels: np.ndarray) -> None:
        """
        Initialize LabelEncoder.

        Parameters:
        - labels (np.ndarray): Array of labels to be encoded.
        """

        self.labels = labels        

    def fit_transform(self) -> np.ndarray:
        """
        Fit the encoder to the labels and transform them into numerical values.

        Returns:
        - np.ndarray: Transformed labels as an array of integers.
        """
        
        label_map = {}  # Store label mappings
        unique_labels = set(self.labels)  # Get unique labels

        # Create a mapping
        for i, label in enumerate(unique_labels):
            label_map[label] = i

        # Transform labels
        transformed_labels = np.zeros(len(self.labels), dtype = np.int32)
        
        for i, label in enumerate(self.labels):
            transformed_labels[i] = label_map[label]

        return transformed_labels
