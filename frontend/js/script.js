const uploadBtn = document.getElementById("uploadBtn");
const recordBtn = document.getElementById("recordBtn");
const audioFile = document.getElementById("audioFile");
const languageSelect = document.getElementById("language");

const transcriptText = document.getElementById("transcriptText");
const emotionValue = document.getElementById("emotionValue");
const emotionLabel = document.getElementById("emotionLabel");
const intentBadges = document.getElementById("intentBadges");
const songCards = document.getElementById("songCards");

const canvas = document.getElementById("waveformCanvas");
const ctx = canvas.getContext("2d");

let songs = [];
let currentIndex = 0;

let mediaRecorder;
let audioChunks = [];
let isRecording = false;

let audioContext;
let analyser;
let dataArray;
let animationId;

/* ---------------- UPLOAD ---------------- */
uploadBtn.onclick = () => audioFile.click();
audioFile.onchange = () => {
  if (audioFile.files[0]) {
    sendAudioToBackend(audioFile.files[0]);
  }
};

/* ---------------- RECORD TOGGLE ---------------- */
recordBtn.onclick = async () => {
  if (!isRecording) startRecording();
  else stopRecording();
};

/* ---------------- START RECORDING ---------------- */
async function startRecording() {
  isRecording = true;
  recordBtn.innerHTML = `<i class="bi bi-stop-fill"></i> Stop Recording`;
  recordBtn.classList.add("recording-active");

  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

  audioChunks = [];
  mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.ondataavailable = e => audioChunks.push(e.data);

  mediaRecorder.onstop = () => {
    stopWaveform();
    const blob = new Blob(audioChunks, { type: "audio/wav" });
    sendAudioToBackend(new File([blob], "voice.wav"));

    stream.getTracks().forEach(t => t.stop());
    audioContext.close();
  };

  mediaRecorder.start();
  startWaveform(stream);
}

/* ---------------- STOP RECORDING ---------------- */
function stopRecording() {
  isRecording = false;
  recordBtn.innerHTML = `<i class="bi bi-mic-fill"></i> Speak Now`;
  recordBtn.classList.remove("recording-active");
  mediaRecorder.stop();
}

/* ---------------- WAVEFORM ---------------- */
function startWaveform(stream) {
  audioContext = new AudioContext();
  analyser = audioContext.createAnalyser();
  analyser.fftSize = 2048;

  const source = audioContext.createMediaStreamSource(stream);
  source.connect(analyser);

  dataArray = new Uint8Array(analyser.fftSize);
  canvas.classList.remove("hidden");

  drawWaveform();
}

function stopWaveform() {
  cancelAnimationFrame(animationId);
  canvas.classList.add("hidden");
}

function drawWaveform() {
  animationId = requestAnimationFrame(drawWaveform);
  analyser.getByteTimeDomainData(dataArray);

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.lineWidth = 2;
  ctx.strokeStyle = "#22c55e";
  ctx.beginPath();

  const sliceWidth = canvas.width / dataArray.length;
  let x = 0;

  for (let i = 0; i < dataArray.length; i++) {
    const v = dataArray[i] / 128.0;
    const y = (v * canvas.height) / 2;
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
    x += sliceWidth;
  }

  ctx.stroke();
}

/* ---------------- BACKEND ---------------- */
async function sendAudioToBackend(file) {
  const fd = new FormData();
  fd.append("audio", file);
  fd.append("preferred_language", languageSelect.value);

  const res = await fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    body: fd
  });

  const data = await res.json();

  renderAnalysis(data);

  songs = data.songs || [];


  currentIndex = 0;
  renderSongs();
}

/* ---------------- RENDER ANALYSIS ---------------- */
function renderAnalysis(d) {
  transcriptText.innerText = d.transcript_original || "N/A";

  emotionValue.innerText = Math.round((d.confidence || 0) * 100) + "%";
  emotionLabel.innerText = d.emotion || "Unknown";

  intentBadges.innerHTML = `
    <span class="badge-pill">${d.intent || "N/A"}</span>
    <span class="badge-pill">${d.final_category || "N/A"}</span>
  `;
}

/* ---------------- RENDER SONG (SINGLE CARD) ---------------- */
function renderSongs() {
  if (!songs.length) {
    songCards.innerHTML = "<p>No songs found.</p>";
    return;
  }

  const s = songs[currentIndex];

  songCards.innerHTML = `
    <div class="col-md-6 mx-auto">
      <div class="song-card text-center">
        <img src="${s.cover_url || 'assets/cover.png'}" class="mb-3">

        <h5>${s.title}</h5>
        <p class="song-artist">${s.artist}</p>

        ${
          s.preview_url
            ? `<audio src="${s.preview_url}" controls autoplay></audio>`
            : `<p class="text-muted">Preview not available for this song</p>`
        }

        <div class="d-flex justify-content-center gap-3 mt-3">
          <button class="vibe-btn" onclick="prevSong()">
            <i class="bi bi-skip-backward-fill"></i> Prev
          </button>

          <button class="vibe-btn" onclick="nextSong()">
            Next <i class="bi bi-skip-forward-fill"></i>
          </button>
        </div>
      </div>
    </div>
  `;
}


function nextSong() {
  if (!songs.length) return;
  currentIndex = (currentIndex + 1) % songs.length;
  renderSongs();
}

function prevSong() {
  if (!songs.length) return;
  currentIndex = (currentIndex - 1 + songs.length) % songs.length;
  renderSongs();
}

/* ---------------- LANGUAGE ---------------- */
function setLanguage(lang) {
  document.getElementById("languageDropdown").innerText = lang;
  languageSelect.value = lang;
}
