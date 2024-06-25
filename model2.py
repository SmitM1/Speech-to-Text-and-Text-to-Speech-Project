from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

def synthesize_text_to_audio(text, output_file):
    try:
        inputs = processor(text=text, return_tensors="pt")
        
        # Load xvector containing speaker's voice characteristics from a dataset (example)
        embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
        speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

        # Generate speech with the SpeechT5 model
        speech = model.generate_speech(inputs.input_ids, speaker_embeddings, vocoder=vocoder)

        # Save the speech to a file
        sf.write(output_file, speech.numpy(), samplerate=16000)
        
        return True, None
    except Exception as e:
        return False, str(e)
