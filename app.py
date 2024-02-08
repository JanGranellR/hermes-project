import sys

sys.path.insert(0, 'config')
sys.path.insert(0, 'test')
sys.path.insert(0, 'models')

import os
import json
import test
import fitz
import config
import requests
import numpy as np
import gradio as gr
from tensorflow import keras
from bs4 import BeautifulSoup
from model import CustomModel
from keras.utils import custom_object_scope

def run_text_analysis(text: str) -> dict:
    """
    Run text analysis models on the input text and return the result.
    
    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary containing the analysis result.
    """

    # Check if the input text has fewer than 20 words
    if len(text.split(" ")) < 20:
        return gr.Warning("The text should be at least 20 words long.")

    analysis_result = {}

    # Prepare text for analysis
    tokenized_text = loaded_tokenizer.texts_to_sequences([text])
    padded_text = keras.preprocessing.sequence.pad_sequences(tokenized_text, maxlen=100)
    predictions = loaded_model.predict(padded_text)

    # Iterate over predictions
    for prediction, label in zip(predictions[0].tolist(), labels_dict.values()):
        analysis_result[label] = prediction

    return analysis_result

def scrape_txt(txt) -> str:
    """
    Set the txt file content to the input textbox.
    
    Args:
        TXT File(File): File uploaded by user.

    Returns:
        str: The file content.
    """

    with open(txt.name, "r") as f:
        return f.read()
    

def set_example_text(example_value: str) -> str:
    """
    Set the example text to the input textbox.
    
    Args:
        example_value (str): The value of the example text to set.

    Returns:
        str: The example text.
    """

    return test.examples[example_value]

def scrape_web_content(selector: str, url: str) -> str:
    """
    Scrape web content based on the provided selector and URL.
    
    Args:
        selector (str): The selector used to extract content.
        url (str): The URL of the website to scrape.

    Returns:
        str: The scraped web content.
    """

    options = config_scraping[selector.replace(" ", "_").lower()]

    try:
        response = requests.get(url, headers=config.dataset["headers"])

        if response.status_code != 200:  # Check if the response status code is not 200
            raise gr.Error(f"The response status code was {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract elements
        content = soup.find(options["container"], attrs=options["container_attrs"])
        elements = content.find_all(options["elements_to_extract"])

        # Check if the last element needs to be ignored
        if options["elements_ignore_last"]:
            elements = elements[:-1]

        extracted_text = ""

        # Iterate over elements
        for element in elements:
            extracted_text += element.text

        return extracted_text

    except Exception as e:
        raise gr.Error("An error occurred while making the request.")

def extract_text_from_pdf_file(pdf_file) -> str:
    """
    Extract text from a PDF file.
    
    Args:
        pdf_file (_io.BufferedReader): The PDF file object to extract text from.

    Returns:
        str: The extracted text from the PDF file.
    """

    try:
        pdf_document = fitz.open(pdf_file.name)

        extracted_text = ""

        # Iterate over pages
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            extracted_text += page.get_text()

        pdf_document.close()

        return extracted_text

    except Exception as e:
        raise gr.Error("An error occurred while extracting the text from the PDF.")

if __name__ == "__main__":
    # Load the model and tokenizer
    model_path = os.path.join(config.model["path"], config.model["path_model"], config.model["nnet"]["path"], config.model["nnet"]["name"])
    tokenizer_path = os.path.join(config.model["path"], config.model["path_model"], config.model["nnet"]["path"], "tokenizer.json")
    labels_path = os.path.join(config.model["path"], config.model["path_model"], config.model["nnet"]["path"], "labels.json")

    try:
        with custom_object_scope({'CustomModel': CustomModel}):
            loaded_model = keras.models.load_model(model_path)

        with open(tokenizer_path) as tokenizer_file:
            loaded_tokenizer_json = tokenizer_file.read()
            loaded_tokenizer = keras.preprocessing.text.tokenizer_from_json(loaded_tokenizer_json)

        with open(labels_path) as labels_file:
            str_labels_dict = json.load(labels_file)
            labels_dict = {int(key): value for key, value in str_labels_dict.items()}

    except Exception as e:
        print("Error loading model or tokenizer:", e)
        sys.exit(1)

    # Load scraping configuration
    config_scraping = {}

    for web in config.dataset["webs"]:
        if "ignore" in web.keys():
            continue

        config_scraping[web["name"]] = web["options"]

    # Set up the Gradio interface
    with gr.Blocks() as interface:

        # Display a markdown heading
        with gr.Row():
            gr.Markdown("# Hermes Project")
        
        with gr.Row():
            gr.HTML("<div style='color: white; background-color: #007bff; padding: 8px; border-radius: 5px;'><strong>Notice</strong>: This website prioritizes user privacy and does not collect any personal data. We are committed to ensuring a secure and trustworthy browsing experience for all our visitors.</div>")
        
        # Create a textbox for input and an output label
        with gr.Row():
            input_textbox = gr.Textbox(label="Input", lines=12, max_lines=12)
            output_label = gr.Label(label="Output")
        
        # Create a submit button
        with gr.Row():
            submit_button = gr.Button(value="Submit", variant="primary")
            submit_button.click(run_text_analysis, inputs=[input_textbox], outputs=[output_label], api_name="predict")
        
        with gr.Row():
            gr.Markdown("## Options")

        with gr.Row():

            # Create a tab for examples
            with gr.Tab(label="Examples"):
                examples = list(test.examples.keys())

                with gr.Row():
                    # Iterate over examples
                    for i in range(int(len(examples) / 2)):
                            example_button = gr.Button(value=examples[i])
                            example_button.click(set_example_text, inputs=[example_button], outputs=[input_textbox], api_name=False)

                            examples.pop(i)

                with gr.Row():
                    for example in examples:
                            example_button = gr.Button(value=example)
                            example_button.click(set_example_text, inputs=[example_button], outputs=[input_textbox], api_name=False)

            # Create a tab for web scraping
            with gr.Tab(label="Scraper"):
                with gr.Row():
                    scraper_selector = gr.Dropdown(
                        label="Website",
                        choices=sorted(set([web.replace("_", " ").capitalize() for web in config_scraping.keys()])),
                        scale=0,
                        min_width=300
                    )

                    scraper_url = gr.Textbox(label="URL", lines=1, scale=1)
                
                with gr.Row():
                    scrape_button = gr.Button(value="Scrape", variant="secondary")
                    scrape_button.click(scrape_web_content, inputs=[scraper_selector, scraper_url], outputs=[input_textbox], api_name=False)
            
            # Create a tab for OCR
            with gr.Tab(label="OCR"):
                with gr.Row():
                    ocr_file_selector = gr.File(
                        file_count="single",
                        file_types=[".pdf"]
                    )
                
                with gr.Row():
                    ocr_button = gr.Button(value="Extract text", variant="secondary")
                    ocr_button.click(extract_text_from_pdf_file, inputs=[ocr_file_selector], outputs=[input_textbox], api_name=False)

            with gr.Tab(label="From File"):
                with gr.Row():
                    file_selector = gr.File(
                        file_count="single",
                        file_types=[".txt"]
                    )

                with gr.Row():
                    scrape_button = gr.Button(value="Extract", variant="secondary")
                    scrape_button.click(scrape_txt, inputs=[file_selector], outputs=[input_textbox], api_name=False)

    # Launch the Gradio interface
    interface.launch(server_name="0.0.0.0")