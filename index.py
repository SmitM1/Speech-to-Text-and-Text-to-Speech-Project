from flask import Flask, render_template, request, jsonify, send_from_directory, url_for, redirect, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from pymongo import MongoClient
from model import transcribe_audio, synthesize_text
import os
import uuid

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['AUDIO_FOLDER'] = 'generated_audio'
app.config['SESSION_TYPE'] = 'filesystem'

# Ensure the necessary folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)

# MongoDB configuration
# client = MongoClient("mongodb://localhost:27017/")
client = MongoClient("mongodb+srv://smitmstr1:RlwSAo3aZ8vw278t@cluster0.81zfbcz.mongodb.net/")
if client: 
    print("hello")
db = client['sttdb']

@app.route('/')
def index():
    # if 'user_id' in session:
    #     return render_template('index.html')
    # return redirect(url_for('signup'))
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'user_id' not in session:
        return jsonify({'redirect': url_for('login')})


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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        # User input validation
        if not email or not password or not confirmation:
            return render_template('signup.html', error="Please fill all the details")

        if password != confirmation:
            return render_template('signup.html', error="Passwords do not match")

        # Check if the email already exists
        if db.users.find_one({"email": email}):
            return render_template('signup.html', error="Email already exists")

        # Hash the password
        hash_password = generate_password_hash(password)

        # Insert the new user
        db.users.insert_one({"email": email, "hash": hash_password})
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Query database for email
        user = db.users.find_one({"email": email})

        # Ensure email exists and password is correct
        if user is None or not check_password_hash(user['hash'], password):
            return render_template('login.html', error="Invalid email or password")

        # Remember which user has logged in
        session["user_id"] = str(user["_id"])

        # Redirect user to home page
        return redirect(url_for('index'))
    else:
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    """Log user out"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
