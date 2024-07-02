import openai
import time

openai.api_key = "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"


def chat_with_bot(prompt):
    max_retries = 5
    retry_delay = 1  # Initial delay before retrying (in seconds)

    for attempt in range(max_retries):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message['content']
        except openai.error.RateLimitError:
            print(
                f"Rate limit exceeded. Waiting {retry_delay} seconds before retrying... (Attempt {attempt + 1}/{max_retries})")
            time.sleep(retry_delay)
            retry_delay *= 2  # Exponential backoff
        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")
            return None

    print("Max retries exceeded. Please try again later.")
    return None


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_bot(user_input)
        if response:
            print("Bot: ", response)
        else:
            print("Bot: Unable to process your request at the moment.")
