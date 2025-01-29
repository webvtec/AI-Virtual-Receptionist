async function startVoiceAssistant() {
    document.getElementById("status").innerText = "Connecting...";

    let response = await fetch("/api/start_voice_assistant", {
        method: "POST"
    });

    let result = await response.json();
    document.getElementById("status").innerText = result.status;
}
