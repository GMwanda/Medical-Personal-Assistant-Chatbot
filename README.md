# Medical Personal Assistant Chatbot

This project is a medical personal assistant chatbot built using TensorFlow, NLTK, and Flask. The chatbot is trained to recognize various intents and provide appropriate responses. The user interface is a simple web-based UI created with HTML, CSS, and JavaScript.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Training the Model](#training-the-model)
- [Running the Application](#running-the-application)
- [Credits](#credits)
- [License](#license)

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/your-username/medical-personal-assistant-chatbot.git
cd medical-personal-assistant-chatbot
```

## Project Structure

```
Medical-Personal-Assistant-Chatbot/
│
├── chatbot.py
├── training.py
├── intents.json
├── words.pkl
├── classes.pkl
├── chatbot_model.keras
├── templates/
│   └── index.html
└── static/
    └── styles.css
```

- `training.py`: Contains the main logic for the chatbot.
- `chatbot.py`: Contains the main logic for the chatbot.
- `intents.json`: Contains the training data for the chatbot.
- `words.pkl` and `classes.pkl`: Serialized word and class lists used during training.
- `chatbot_model.keras`: The trained model.
- `templates/index.html`: HTML file for the web UI.
- `static/styles.css`: CSS file for the web UI.

## Usage

To use the chatbot, follow these steps:

1. Train the model (if not already trained) by running `chatbot.py`.
2. Start the Flask application by running `app.py`.
3. Open your web browser and go to `http://127.0.0.1:5000/` to interact with the chatbot.

## Training the Model

To train the chatbot model, make sure you have your training data in `intents.json` and run the following command:

```sh
python training.py
```

This will preprocess the data, train the model, and save the necessary files (`words.pkl`, `classes.pkl`, and `chatbot_model.keras`).

## Running the Application

To start the web application, run:

```sh
python app.py
```

Open your web browser and go to `http://127.0.0.1:5000/` to interact with the chatbot through the web UI.
