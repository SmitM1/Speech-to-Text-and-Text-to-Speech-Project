<div align="center">

<h1>AI Voice to Text and Text to Voice</h1>

<a href="https://github.com/SmitM1/Speech-to-Text-and-Text-to-Speech-Project/tree/main/LICENSE">
<img alt="License" src="https://img.shields.io/github/license/SmitM1/Speech-to-Text-and-Text-to-Speech-Project?style=flat&color=eee&label="> </a>

<a href="https://github.com/SmitM1/Speech-to-Text-and-Text-to-Speech-Project/pulse">
<img alt="Last Updated" src="https://img.shields.io/github/last-commit/SmitM1/Speech-to-Text-and-Text-to-Speech-Project?style=flat&color=e06c75&label=Last+Updated"> </a>

<h3>Flask-based Web Application for Speech-to-Text and Text-to-Speech</h3>

<figure>
  <img src="static\img\ss.jpg" alt="Screenshot" style="width:100%">
  <br/>
  <figcaption>Landing Page Voice to Text</figcaption>
</figure>

</div>

## Introduction

This project is a web application built using Flask that provides both speech-to-text and text-to-speech functionalities. It integrates Hugging Face's Wav2Vec2 model for speech-to-text and SpeechT5 model for text-to-speech capabilities. Users can upload audio files for transcription and enter text to convert to speech.

## Motivation

The motivation behind this project was to create a user-friendly tool for converting speech to text and vice versa using state-of-the-art models. It aims to provide a seamless experience for users needing quick and accurate transcription and synthesis of audio and text.

## Features

- **Speech-to-Text Conversion:** Upload audio files for transcription.
- **Text-to-Speech Synthesis:** Enter text to generate synthesized speech.
- **User Authentication:** Secure login and signup functionality.
- **Responsive Web Interface:** Accessible across devices.

## Technologies Used

- **Flask:** Web framework for Python.
- **Hugging Face Transformers:** Utilized for Wav2Vec2 and SpeechT5 models.
- **HTML/CSS:** Front-end development.
- **JavaScript:** Enhancing user interactions.

## Usage

1. **Speech-to-Text:**
   - Navigate to the speech-to-text section.
   - Upload an audio file for transcription.
   - Wait for the transcription results.

2. **Text-to-Speech:**
   - Go to the text-to-speech section.
   - Enter text to be converted into speech.
   - Click the "Synthesize" button to generate speech.

## Setup

To set up this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Set up environment variables:**

    - Create a '.env' file in the root directory.
    - Add the following variables to the '.env' file:

    ```bash
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key_here

4. **Start the Flask application:**

    ```bash
    flask run

- The application will start running locally at 'http://localhost:5000'.

## License

- This project is licensed under the MIT License. See the LICENSE file for more details.