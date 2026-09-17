#  Sugar AI - Intelligent Voice Assistant

Sugar is a simple AI-powered voice assistant that I built using Python to explore speech recognition, text-to-speech, and AI integration. It can understand voice commands, open websites, play music, tell jokes, read the latest news, and answer general questions using Google's Gemini API.
This project helped me learn how different Python libraries work together to create a voice-controlled assistant.

##  Features

-  Voice command recognition
-  AI responses using Google Gemini
-  Open websites like:
  - Google
  - YouTube
  - Instagram
  - LinkedIn
  - Spotify
-  Play songs from a custom music library
-  Read the latest news headlines
-  Tell random jokes
-  Speak responses using Text-to-Speech
-  Colored terminal output for better readability


##  Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- Google Gemini API
- Requests
- PyJokes
- Colorama
- python-dotenv

##  Project Structure

```
Sugar AI Intelligent Voice Assistant/
│
├── main.py
├── musicLibrary.py
├── test.py
├── .gitignore
├── .env
└── README.md
```

##  Getting Started

### Clone the repository

```bash
git clone https://github.com/Smirti-Pundir/Sugar-AI-Intelligent-Voice-Assistant.git
```

### Go to the project folder

```bash
cd Sugar-AI-Intelligent-Voice-Assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install the required packages

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file and add your Gemini API key:

```env
API_KEY_=YOUR_GEMINI_API_KEY
```

Also add your News API key in the project before running the assistant.

---

##   Run the Project

```bash
python main.py
```

Wake up the assistant by saying:

```
Sugar
```

Example commands:

- Open Google
- Open YouTube
- Play Believer
- Tell me a joke
- Read the news
- Exit

##  What I Learned

While building this project, I learned about:

- Speech recognition in Python
- Text-to-speech using pyttsx3
- Working with REST APIs
- Using environment variables securely
- Integrating Google's Gemini AI
- Organizing a Python project

##  Future Improvements

Some features I'd like to add in the future:

-  Face recognition
-  Hand gesture control
-  Weather updates
-  Email support
-  WhatsApp integration
-  GUI version
-  Chat history
-  Smart home control

##   About Me

I'm Smirti Pundir, and I'm learning Python by building real-world projects like this one.
I'm always looking to improve my skills and explore new technologies.

##   Support

If you found this project helpful or interesting, consider giving it a star on GitHub. It motivates me to keep building and sharing more projects.
Thank you for visiting my repository! 
