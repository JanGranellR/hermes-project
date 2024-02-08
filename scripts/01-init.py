import sys

sys.path.insert(0, 'config')
sys.path.insert(0, 'utils')

import os
import nltk
import config
from utils import create_path

def main() -> None:
    create_path(config.dataset["path"])
    create_path(os.path.join(config.dataset["path"], config.dataset["path_raw"]))
    create_path(os.path.join(config.dataset["path"], config.dataset["path_processed"]))
    create_path(os.path.join(config.dataset["path"], config.dataset["path_cache"]))

    nltk.download('punkt')
    nltk.download('stopwords')

if __name__ == "__main__":
    main()