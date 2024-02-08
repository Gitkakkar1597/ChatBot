# Import necessary modules
from flask import Flask, render_template, request
import os
import openai
import time

# Initialize Flask app
app = Flask(__name__, static_folder="static")

# Configure OpenAI API key
openai.api_key = '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'

# Function to interact with OpenAI's GPT-3.5 model
def bot(prompt, model='gpt-3.5-turbo', temperature=0.9, max_tokens=100, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.9, stop=[" User:", " AI:"]):
    try:
        # Request completion from OpenAI's API
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop
        )
        # Extract response text from the API response
        text = response.choices[0].message.content
        return text
    except Exception as e:
        # Handle errors during interaction with the OpenAI API
        return "GPT-3 Error: {}".format(e)

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle user requests and get bot responses
@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    start_time = time.time()
    bot_response = bot(prompt=user_text)
    response_time = time.time() - start_time
    return str(bot_response)

# Main execution point
if __name__ == "__main__":
    app.run(debug=True)
