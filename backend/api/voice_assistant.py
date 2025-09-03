from backend.ai.speech_transcription import SpeechTranscriber
from backend.ai.text_generation import TextGenerator
from backend.ai.text_to_speech import TextToSpeech
from backend.utils.constants import GREETING_MESSAGE

class VoiceAssistant:
    def __init__(self, assemblyai_key, openai_key, elevenlabs_key):
        self.transcriber = SpeechTranscriber(assemblyai_key)
        self.generator = TextGenerator(openai_key)
        self.speech_synthesizer = TextToSpeech(elevenlabs_key)
        self.conversation_history = [{"role": "system", "content": "You are a receptionist at webvtec a website generation company."}]

    def handle_transcription(self, transcript):
        if not transcript.text:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            self.process_user_input(transcript.text)
        else:
            print(transcript.text, end="\r")

    def process_user_input(self, user_text):
        self.conversation_history.append({"role": "user", "content": user_text})
        response = self.generator.generate_response(self.conversation_history)
        self.conversation_history.append({"role": "assistant", "content": response})
        self.speech_synthesizer.generate_audio(response)

    def start_assistant(self):
        self.speech_synthesizer.generate_audio(GREETING_MESSAGE)
        self.transcriber.start_transcription(self.handle_transcription)
