import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, AutoTokenizer, AutoModelWithLMHead
import torchaudio
import os
import uuid

# Load the pre-trained Wav2Vec2 model and processor for speech-to-text
stt_processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
stt_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

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
