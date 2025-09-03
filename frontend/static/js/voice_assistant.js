async function startVoiceAssistant() {
    const statusEl = document.getElementById("status");
    statusEl.innerText = "Connecting...";

    try {
        const response = await fetch("/api/start_voice_assistant", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                clientName: process.env.REACT_APP_CLIENT_NAME || "AI Receptionist"
            })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const result = await response.json();
        statusEl.innerText = `${result.status} for ${process.env.REACT_APP_CLIENT_NAME || "AI Receptionist"}`;
    } catch (error) {
        console.error("Error starting voice assistant:", error);
        statusEl.innerText = "❌ Failed to connect. Please try again.";
    }
}
