from transformers import pipeline

class Speech2Text:
    def __init__(self,model_name="openai/whisper-medium",device='cuda'):
        try:
            self.pipe = pipeline("automatic-speech-recognition", model="openai/whisper-medium", device = 'cuda')
        except:
            print("No cuda found, falling back to cpu")
            self.pipe = pipeline("automatic-speech-recognition", model="openai/whisper-medium", device = 'cpu')
    
    def get_transcript(self,file_path):
        return self.pipe(file_path)['text']
