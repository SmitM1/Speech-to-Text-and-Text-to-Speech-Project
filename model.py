# model.py

import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
import torchaudio
import os
import uuid

# Load the pre-trained Wav2Vec2 model and processor for speech-to-text
stt_processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
stt_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Load the pre-trained SpeechT5 model and processor for text-to-speech
tts_processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
tts_model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

# Example random speaker embedding for demonstration purposes
speaker_embedding = torch.randn((1, tts_model.config.speaker_embedding_dim))

def transcribe_audio(audio_file_path):
    # Load the audio file
    waveform, sample_rate = torchaudio.load(audio_file_path)
    
    # Resample if needed (Wav2Vec2 expects 16kHz audio)
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)
    
    # Process the audio file
    input_values = stt_processor(waveform.squeeze().numpy(), return_tensors="pt", sampling_rate=16000).input_values

    # Perform inference
    with torch.no_grad():
        logits = stt_model(input_values).logits

    # Get the predicted IDs
    predicted_ids = torch.argmax(logits, dim=-1)

    # Decode the IDs to text
    transcription = stt_processor.batch_decode(predicted_ids)[0]
    
    return transcription

def synthesize_text(text, output_file_path):
    print(f"Received text: {text}")  # Debug print
    
    # Process the text input
    inputs = tts_processor(text, return_tensors="pt")
    input_ids = inputs.input_ids

    try:
        # Generate speech with the SpeechT5 model
        with torch.no_grad():
            speech = tts_model.generate_speech(input_ids, speaker_embeddings=speaker_embedding)

        # Use the vocoder to convert the generated speech to waveform
        waveform = vocoder(speech)

        # Save the waveform to a file
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)  # Ensure directory exists
        torchaudio.save(output_file_path, waveform.squeeze(), 16000)

        print(f"Saved audio to: {output_file_path}")  # Debug print
    except Exception as e:
        print(f"Error synthesizing text: {str(e)}")
        raise  # Raise the exception to propagate it to the caller
