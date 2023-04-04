import openai
import random

openai.api_key = "0xIyk2eK8eMWOMtQ6u"

# Function to generate a response from OpenAI's GPT-3 language model
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text
    message = message.strip()
    return message

# Function to analyze sentiment of a message using OpenAI's GPT-3 language model
def analyze_sentiment(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Sentiment analysis: {message}",
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.0,
    )

    sentiment = response.choices[0].text
    sentiment = sentiment.strip()
    return sentiment

# Function to personalize the chatbot's responses
def personalize_message(message, name):
    message = message.replace("[name]", name)
    return message

# Function to generate a kind response based on the sentiment of the user's input
def generate_kind_response(user_input, name):
    sentiment = analyze_sentiment(user_input)

    if sentiment == "Positive":
        prompts = ["That's great to hear!", "I'm so happy for you!", "Congratulations!"]
        response = random.choice(prompts)
    elif sentiment == "Neutral":
        prompts = ["I'm here to listen if you need someone to talk to.", "How can I help you today?"]
        response = random.choice(prompts)
    else:
        prompts = ["I'm sorry to hear that.", "That must be tough for you.", "I'm here for you."]
        response = random.choice(prompts)

    response = personalize_message(response, name)
    return response

# Main function to run the chatbot
def chatbot():
    print("Hi! My name is KindBot. What's your name?")
    name = input("Your name: ")

    print(f"Nice to meet you, {name}! How can I help you today?")
    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("KindBot: Goodbye!")
            break

        response = generate_kind_response(user_input, name)
        print(f"KindBot: {response}")

if __name__ == '__main__':
    chatbot()