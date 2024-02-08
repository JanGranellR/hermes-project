import sys

sys.path.insert(0, 'config')

import os
import nltk
import config
from collections import Counter
from nltk.corpus import stopwords

def count_files() -> None:
    """
    Counts the number of files in each category and web within the dataset.
    """
    
    stats = {}  # Dictionary to store statistics

    for web in config.dataset["webs"]:
        # Initialize the inner dictionary if the category does not exist
        if web["category"] not in stats:
            stats[web["category"]] = {"total": 0}  # Initialize with a 'total' count

        if web["name"] not in stats[web["category"]]:
            # Updates the total count of files in the category
            stats[web["category"]]["total"] += len(os.listdir(os.path.join(config.dataset["path"], config.dataset["path_cache"], web["category"], web["name"]))) - 2

        # Stores count for each web within the category
        stats[web["category"]][web["name"]] = len(os.listdir(os.path.join(config.dataset["path"], config.dataset["path_cache"], web["category"], web["name"]))) - 2

    for category, category_stats in stats.items():
        print(f"Category: {category}")
        print(f"Total: {category_stats['total']}")
        
        for web_name, web_count in category_stats.items():
            if web_name != "total":
                print(f"- {web_name}: {web_count}")
        
        print()

def count_words() -> None:
    """
    Counts the total number of words across all categories and prints the result.
    """

    data = load_files_by_category()

    # Set stopwords for the Spanish language
    stop_words = set(stopwords.words("spanish"))

    # Counter to store the count of each word
    counter = Counter()

    for key in data.keys():
        # Tokenize the text and convert to lowercase
        words = nltk.word_tokenize(data[key].lower())

        # Filter out non-alphabetic words and stopwords
        words = [word for word in words if word.isalpha() and word not in stop_words]

        # Update the total word count
        counter.update(words)

    print("Total Word Count:", sum(counter.values()), "-", "Unique words:", sum(set(counter.values())))

def load_files_by_category() -> dict[str, str]:
    """
    Loads files from each category and returns a dictionary where keys are category names and values are concatenated text from all files in that category.

    Returns:
    - dict[str, str]: A dictionary where keys are category names and values are concatenated text.
    """

    data = {}

    for web in config.dataset["webs"]:
        text = ""

        for f in os.listdir(os.path.join(config.dataset["path"], config.dataset["path_cache"], web["category"], web["name"])):
            # Excludes response.txt and urls.txt files
            if not (f == "response.txt" or f == "urls.txt"):
                # Reads content from the file and appends to text
                with open(os.path.join(config.dataset["path"], config.dataset["path_cache"], web["category"], web["name"], f), "r") as r:
                    text += r.read()

        if web["category"] in data.keys():
            # Appends text if category already exists in the data dictionary
            data[web["category"]] = data[web["category"]] + text
        else:
            data[web["category"]] = text
    
    return data

def top_x_words(top: int = 10) -> None:
    """
    Prints the top 'top' words from each category after removing stopwords.

    Parameters:
    - top (int): Number of top words to print. Default is 10.
    """

    data = load_files_by_category()

    # Set stopwords for the Spanish language
    stop_words = set(stopwords.words("spanish"))

    for key in data.keys():
        # Tokenize the text and convert to lowercase
        words = nltk.word_tokenize(data[key].lower())

        # Filter out non-alphabetic words and stopwords
        words = [word for word in words if word.isalpha() and word not in stop_words]

        # Count the occurrences of each word and sort them in descending order
        words = sorted(Counter(words).items(), key = lambda x: x[1], reverse = True)

        print(key, ":", words[:top], end = "\n\n")

def main() -> None:
    """
    Main function that executes the program.
    """

    count_files()
    print("--------------------------------")

    top_x_words(10)
    print("--------------------------------")

    count_words()

if __name__ == "__main__":
    main()