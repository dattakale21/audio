// Replace 'YOUR_API_KEY' and 'YOUR_AUDIO_DATA' with the actual values

const apiKey = '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';
const audioData = 'audio3.mp3'; // Should be base64 encoded

const url = 'https://api.whisper.com/convert'; // Replace with the actual endpoint URL

const data = {
  apiKey: apiKey,
  audio: audioData
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
.then(response => response.json())
.then(result => {
  console.log('Transcription result:', result);
  // Handle the transcription result here
})
.catch(error => {
  console.error('Error:', error);
});
