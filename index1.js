function transcribeAndTranslate() {
    const targetLanguage = document.getElementById("targetLanguage").value;
    const audioFile = document.getElementById("audioFile").files[0];

    if (!targetLanguage || !audioFile) {
        alert("Please select a target language and upload an audio file.");
        return;
    }

    const formData = new FormData();
    formData.append("targetLanguage", targetLanguage);
    formData.append("audioFile", audioFile);

    fetch("/transcribe-and-translate", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const transcriptionResult = data.transcriptionResult;
        document.getElementById("transcriptionResult").textContent = transcriptionResult;
    })
    .catch(error => console.error("Error:", error));
}
