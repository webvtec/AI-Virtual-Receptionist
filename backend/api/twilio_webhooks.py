from fastapi import APIRouter, Request, Form, Response
from twilio.twiml.voice_response import VoiceResponse
import os
import requests
from backend.api.voice_assistant import TextGenerator
from backend.api.text_to_speech import TextToSpeech

router = APIRouter()

text_generator = TextGenerator()
tts = TextToSpeech()

@router.post("/incoming_call")
async def incoming_call(request: Request):
    form = await request.form()
    from_number = form.get("From")
    response = VoiceResponse()
    
    # Greet caller
    response.say(os.getenv("GREETING_MESSAGE", "Hello! AI receptionist here."), voice="alice")

    # Record caller message and send to /process_call
    response.record(
        action="/process_call",
        method="POST",
        max_length=30,
        play_beep=True
    )

    return Response(content=str(response), media_type="application/xml")


@router.post("/process_call")
async def process_call(RecordingUrl: str = Form(...)):
    # Download caller audio
    audio_data = requests.get(RecordingUrl).content

    # Transcribe audio (use AssemblyAI or Whisper)
    transcription = "Simulated transcription here"  # Replace with actual transcription logic

    # GPT-4 response
    ai_response = text_generator.generate_response([{"role": "user", "content": transcription}])

    # TTS audio
    tts.generate_audio(ai_response)

    # Respond to Twilio (simple goodbye)
    twilio_response = VoiceResponse()
    twilio_response.say("Thank you. Goodbye!", voice="alice")
    return Response(content=str(twilio_response), media_type="application/xml")
