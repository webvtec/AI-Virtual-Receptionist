# Clara - AI Powered Virtual Receptionist

## Project Overview
Clara is an **AI-powered virtual receptionist** designed to handle real-time speech transcription, AI-driven responses, and text-to-speech synthesis. This project integrates **AssemblyAI**, **OpenAI GPT-3.5 Turbo**, and **ElevenLabs** to provide a seamless virtual receptionist experience.

Developed by **Kalyan Raja Kadari**, this project is designed to automate call handling, appointment scheduling, and intelligent conversation processing for businesses.

## Features
- **Real-time Speech Transcription** using AssemblyAI
- **AI-driven Response Generation** using OpenAI GPT-3.5 Turbo
- **Live Text-to-Speech Streaming** with ElevenLabs
- **Voice Assistant API** for handling receptionist tasks
- **Frontend UI** for user interaction
- **Docker Deployment** for easy hosting
- **Scalability and Cloud Deployment** with AWS/Kubernetes

## Technologies Used
- **Programming Language**: Python (FastAPI Backend)
- **AI Models**: OpenAI GPT-3.5 Turbo, FAISS, Sentence Transformers
- **Speech Processing**: AssemblyAI (Speech-to-Text), ElevenLabs (Text-to-Speech)
- **Web Framework**: FastAPI
- **Database**: SQLite (for logging interactions)
- **Deployment**: Docker, Kubernetes, AWS

## Installation and Setup

### Prerequisites
- Python 3.9+
- API Keys for AssemblyAI, OpenAI, ElevenLabs
- Docker (Optional for Deployment)

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Running the Application
```bash
uvicorn backend.api.voice_assistant:app --host 0.0.0.0 --port 8000 --reload
```

### Running with Docker
```bash
docker build -t clara-receptionist .
docker run -p 8000:8000 clara-receptionist
```

### Deployment with Kubernetes
```bash
kubectl apply -f deploy/kubernetes.yaml
```

## API Endpoints

### 1. Start Virtual Receptionist
**Endpoint:** `POST /api/start_voice_assistant`  
**Description:** Starts the real-time voice assistant.

### 2. Process AI Chat Query
**Endpoint:** `POST /api/chatbot/ask`  
**Description:** Processes user queries and returns AI-generated responses.

## Acknowledgments
This project was developed by **Kalyan Raja Kadari**. Special thanks to the OpenAI, AssemblyAI, and ElevenLabs teams for their APIs and contributions to AI-driven voice applications.

---
For any issues or contributions, feel free to reach out! 🚀
