# ChatBot - A Conversational AI Chat Assistant

## Introduction

**ChatBot** is a conversational AI chat assistant built using Flask, Python, and the Google Gemini API. This application provides a simple and intuitive interface for users to interact with an AI chatbot. The chatbot responds to user queries with concise, plain text answers, and introduces itself as "ChatBot" without revealing any details about its underlying technology.

## Project Structure

```arduino
flask_chatbot/
├── assets/
│ └── Screenshot.png
├── static/
│ ├── script.js
│ └── styles.css
├── templates/
│ └── index.html
├── .env
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Directory Breakdown

- **assets/**: Contains static assets like screenshots.
- **static/**: Contains static files including JavaScript (`script.js`) and CSS (`styles.css`).
- **templates/**: Contains HTML templates, including `index.html`.
- **.env**: Stores environment variables, including the Google API key.
- **app.py**: Main Flask application file that handles routing and interaction with the Gemini API.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **README.md**: This file, providing an overview of the project.
- **.gitignore**: Specifies files and directories to be ignored by Git (e.g., `venv/`, `.env`).

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **Google Gemini API**: For natural language processing and generating responses.
- **HTML/CSS/JavaScript**: For frontend development.
- **dotenv**: For managing environment variables.

## Working Screenshot

- **Home Page**
  ![ChatBot](/assets/Screenshot.png)

## Installation and Running the App

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Gitkakkar1597/ChatBot.git
   cd chatbot-project

2. **Create a Virtual Environment**

   ```bash
   Copy code
   python -m venv venv
   
3. **Activate the Virtual Environment**

   On Windows:

   ```bash
   Copy code
   venv\Scripts\activate
   
   On macOS/Linux:

   ```bash
   Copy code
   source venv/bin/activate
   
4. **Install Dependencies**

   ```bash
   Copy code
   pip install -r requirements.txt
   
5. **Configure Environment Variables**

    Create a `.env` file in the root directory and add your Google API key:

   ```makefile
   GOOGLE_API_KEY=your_google_api_key_here
   
6. **Run the Application**

   ```bash
   python app.py
   
The application will be available at http://127.0.0.1:5000.

## Requirements
- Flask==3.0.3
- google-generativeai==0.7.2
- python-dotenv==1.0.0 (for managing environment variables)

## Notes
- This project uses the Google Gemini API for generating responses. Make sure to obtain and configure your own API key.
- The application is designed to be run locally. Ensure all dependencies are installed and environment variables are set up correctly before running the app.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

