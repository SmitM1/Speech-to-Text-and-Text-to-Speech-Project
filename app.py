# app.py

from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from model import transcribe_audio, synthesize_text
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['AUDIO_FOLDER'] = 'generated_audio'

# Ensure the necessary folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        audio_file = request.files['audio_file']
        if audio_file:
            # Save the audio file to the uploads folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
            audio_file.save(file_path)
            
            # Transcribe the audio file
            transcription = transcribe_audio(file_path)
            
            return jsonify({'transcription': transcription})
        else:
            return jsonify({'error': 'No audio file uploaded'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/synthesize', methods=['POST'])
def synthesize():
    try:
        text = request.form['text']
        if text:
            # Synthesize the text to speech
            audio_path = os.path.join(app.config['AUDIO_FOLDER'], f"{uuid.uuid4()}.wav")
            synthesize_text(text, audio_path)
            
            return jsonify({'audio_url': f'/audio/{os.path.basename(audio_path)}'})
        else:
            return jsonify({'error': 'No text provided'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/audio/<filename>')
def audio(filename):
    return send_from_directory(app.config['AUDIO_FOLDER'], filename)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
