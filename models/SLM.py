import ollama

class SLM:
    def __init__(self,model_name):
        self.model_name=model_name
    
    def prompt(self,chat_history,stream):
        return ollama.chat(model=self.model_name,messages=chat_history,stream=stream)
