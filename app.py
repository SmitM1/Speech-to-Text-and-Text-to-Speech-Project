# app.py

from flask import Flask, render_template, request, jsonify
from model import transcribe_audio
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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

if __name__ == '__main__':
    app.run(debug=True)
