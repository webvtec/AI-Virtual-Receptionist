from fastapi import FastAPI
from backend.api import twilio_webhooks

app = FastAPI()

# Include Twilio webhook routes
app.include_router(twilio_webhooks.router)
