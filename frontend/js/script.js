const uploadBtn = document.getElementById("uploadBtn");
const recordBtn = document.getElementById("recordBtn");
const audioFile = document.getElementById("audioFile");
const languageSelect = document.getElementById("language");
const waveform = document.getElementById("waveform");

const transcriptText = document.getElementById("transcriptText");
const emotionValue = document.getElementById("emotionValue");
const emotionLabel = document.getElementById("emotionLabel");
const intentBadges = document.getElementById("intentBadges");
const songCards = document.getElementById("songCards");

let lastAnalysis = null;
let songs = [];
let currentIndex = 0;
let mediaRecorder;
let audioChunks = [];

/* UPLOAD */
uploadBtn.onclick = () => audioFile.click();
audioFile.onchange = () => sendAudioToBackend(audioFile.files[0]);

/* RECORD */
recordBtn.onclick = async () => {
  waveform.classList.remove("hidden");
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

  audioChunks = [];
  mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.ondataavailable = e => audioChunks.push(e.data);

  mediaRecorder.onstop = async () => {
    waveform.classList.add("hidden");
    const blob = new Blob(audioChunks, { type: "audio/wav" });
    sendAudioToBackend(new File([blob], "voice.wav"));
    stream.getTracks().forEach(t => t.stop());
  };

  mediaRecorder.start();
  setTimeout(() => mediaRecorder.stop(), 5000);
};

/* BACKEND */
async function sendAudioToBackend(file) {
  const fd = new FormData();
  fd.append("audio", file);
  fd.append("preferred_language", languageSelect.value);

  const res = await fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    body: fd
  });

  lastAnalysis = await res.json();
  songs = lastAnalysis.songs || [];
  currentIndex = 0;

  renderAnalysis(lastAnalysis);
  renderSongs();
}

/* RENDER */
function renderAnalysis(d) {
  transcriptText.innerText = d.transcript_original || "N/A";
  emotionValue.innerText = Math.round(d.confidence * 100) + "%";
  emotionLabel.innerText = d.emotion;

  intentBadges.innerHTML = `
    <span class="badge-pill">${d.intent || "N/A"}</span>
    <span class="badge-pill">${d.final_category}</span>
  `;
}

function renderSongs() {
  songCards.innerHTML = "";

  songs.forEach((s, i) => {
    songCards.innerHTML += `
      <div class="col-md-4">
        <div class="song-card">
          <img src="${s.cover_url || 'assets/cover.png'}">
          <h6 class="mt-2">${s.title}</h6>
          <p class="text-muted">${s.artist}</p>
          <audio src="${s.preview_url}" controls></audio>
        </div>
      </div>
    `;
  });
}
