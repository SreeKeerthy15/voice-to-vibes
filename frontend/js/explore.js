const songCards = document.getElementById("songCards");

let songs = [];
let currentIndex = 0;

async function loadMood(category) {
  songCards.innerHTML = "<p class='text-center'>Loading...</p>";

  const res = await fetch(
    `http://127.0.0.1:8000/explore?category=${category}`
  );

  const data = await res.json();
  songs = data.songs || [];
  currentIndex = 0;

  renderSong();
}

function renderSong() {
  if (!songs.length) {
    songCards.innerHTML = "<p>No songs available.</p>";
    return;
  }

  const s = songs[currentIndex];

  songCards.innerHTML = `
    <div class="col-md-6">
      <div class="song-card text-center">
        <img src="${s.cover_url || 'assets/cover.png'}" class="mb-3">

        <h4>${s.title}</h4>
        <p class="fw-bold text-light">${s.artist}</p>

        ${
          s.preview_url
            ? `<audio src="${s.preview_url}" controls autoplay></audio>`
            : `<p class="text-muted">Preview not available</p>`
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
  currentIndex = (currentIndex + 1) % songs.length;
  renderSong();
}

function prevSong() {
  currentIndex = (currentIndex - 1 + songs.length) % songs.length;
  renderSong();
}
