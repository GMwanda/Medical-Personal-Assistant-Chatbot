import os
import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext

# Set the environment variable within the script
os.environ["API_KEY"] = "AIzaSyALPP_BlktYkD6z1VEEUr_7FuMZCsRNFTY"
genai.configure(api_key=os.environ["API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(history=[])


def chat_with_bot(prompt):
    response = chat_session.send_message(prompt)
    return response.text


def send_message():
    user_input = user_input_entry.get()
    if user_input.lower() in ["quit", "exit", "bye"]:
        root.quit()
    else:
        chat_history.insert(tk.END, "You: " + user_input + "\n")
        response = chat_with_bot(user_input)
        chat_history.insert(tk.END, "Bot: " + response + "\n")
        user_input_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Create the chat history text area
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_history.pack(padx=10, pady=10)

# Create the user input entry box
user_input_entry = tk.Entry(root, width=50)
user_input_entry.pack(side=tk.LEFT, padx=(10, 0), pady=10)

# Create the send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
