# Hermes Project

Hermes Project is an AI classification model designed to accurately classify text into 12 categories.

## Installation

> 👀 Ensure you have Docker installed on your system.

Clone the GitHub repository to your local machine using this command:

``` bash
git clone https://github.com/JanGranellR/hermes-project.git
```

Visit the [Releases](https://github.com/JanGranellR/hermes-project/releases) tab and download the latest trained model. Uncompress the downloaded `.zip` file and place it inside a new folder named `data/model/nnet`.

Finally, run the project and its dependencies with Docker Compose:

``` bash
docker-compose up -d --build
```

## Usage
Access the web interface with a browser:

``` bash
http://localhost:7860
```