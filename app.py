from flask import Flask, render_template, request, jsonify, session
import random
import json
import pickle
import numpy as np
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

# Load necessary NLTK data
nltk.download('wordnet')
nltk.download('punkt')

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.keras')

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load dataset
data = pd.read_csv('Disease_symptom_and_patient_profile_dataset.csv')


# Function to match symptoms to diseases
def match_symptoms_to_disease(symptoms):
    possible_diseases = []
    for index, row in data.iterrows():
        match = all(row[symptom.capitalize()] == 'Yes' for symptom in symptoms if symptom.capitalize() in row)
        if match:
            possible_diseases.append(row['Disease'])
    return possible_diseases


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list, intents_json, symptoms=[]):
    if not intents_list and not symptoms:
        return "Sorry, I don't understand."

    # Check if symptoms are provided
    if symptoms:
        diseases = match_symptoms_to_disease(symptoms)
        if diseases:
            return f"Based on the symptoms you provided, it might be {' or '.join(diseases[:5])}. Please consult a healthcare professional for a proper diagnosis."
        else:
            return "I'm not sure what disease you might have based on those symptoms. Please provide more symptoms."

    # Process intents if no symptoms provided
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses']).replace("[DISEASE]", "an unknown disease")
            break
    return result


def extract_symptoms(message):
    symptoms_list = ["fever", "cough", "fatigue", "difficulty breathing"]
    symptoms = [symptom for symptom in symptoms_list if symptom in message.lower()]
    return symptoms


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_bot_response():
    message = request.form["message"]
    symptoms = extract_symptoms(message)

    # Retrieve session state
    if 'conversation_state' not in session:
        session['conversation_state'] = {'symptoms': [], 'awaiting_symptom': False}

    state = session['conversation_state']

    # If awaiting a symptom response, add to symptoms and check for diseases
    if state['awaiting_symptom']:
        state['symptoms'].append(message.lower())
        session['conversation_state'] = state
        diseases = match_symptoms_to_disease(state['symptoms'])
        if diseases:
            response = f"Based on the symptoms you provided, it might be {' or '.join(diseases[:5])}. Please consult a healthcare professional for a proper diagnosis."
            state['awaiting_symptom'] = False  # Reset state
        else:
            response = "I'm not sure what disease you might have based on those symptoms. Please provide more symptoms."
    else:
        ints = predict_class(message)
        response = get_response(ints, intents, symptoms)
        if 'medical_inquiry' in [intent['intent'] for intent in ints]:
            if not symptoms:
                response = "Can you provide more symptoms? For example, do you have fever, cough, fatigue, or difficulty breathing?"
                state['awaiting_symptom'] = True

    session['conversation_state'] = state
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
