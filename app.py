from flask import Flask, render_template, request
import google.generativeai as genai
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder="static")

# Configure Google AI API key from environment variable
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to interact with Gemini AI model
def bot(prompt, model=model):
    try:
        full_prompt = (f"You are 'ChatBot', a chat assistant designed to answer users' queries. "
                       f"Always refer to yourself simply as 'ChatBot'. Never mention that you are a large language model "
                       f"or associated with any specific technology or company. Respond in short, plain text, without any "
                       f"special characters or symbols. Be concise and to the point:-  {prompt}")
        response = model.generate_content(full_prompt)
        text = response.text
        return text
    except Exception as e:
        return "Gemini AI Error: {}".format(e)

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
