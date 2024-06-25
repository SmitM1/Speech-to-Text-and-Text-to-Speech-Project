<div align="center">

<h1>AI Voice to Text and Text to Voice</h1>

<a href="https://github.com/SmitM1/Speech-to-Text-and-Text-to-Speech-Project/tree/main/LICENSE">
<img alt="License" src="https://img.shields.io/github/license/SmitM1/Speech-to-Text-and-Text-to-Speech-Project?style=flat&color=eee&label="> </a>

<a href="https://github.com/SmitM1/Speech-to-Text-and-Text-to-Speech-Project/pulse">
<img alt="Last Updated" src="https://img.shields.io/github/last-commit/SmitM1/Speech-to-Text-and-Text-to-Speech-Project?style=flat&color=e06c75&label=Last+Updated"> </a>

<h3>Flask-based Web Application for Speech-to-Text and Text-to-Speech</h3>

<figure>
  <img src="path/to/your/screenshot.png" alt="Screenshot" style="width:100%">
  <br/>
  <figcaption>Screenshot of the application</figcaption>
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

## Setup

To run this project locally, follow these steps:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
# Set up virtual environment (optional but recommended)
python -m venv venv
# Activate virtual environment
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
# Install dependencies
pip install -r requirements.txt
# Run the application
python app.py
