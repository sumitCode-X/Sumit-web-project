// Intro loading script: animate the progress bar and then dispatch an event
// Run immediately when the script is executed (script is appended after main.js is ready)
const loadingScreen = document.getElementById("loading-screen");
const progressFill = document.querySelector('.progress-fill');
const progressText = document.querySelector('.progress-text');

if (loadingScreen && progressFill) {
    let progress = 0;
    const progressInterval = setInterval(() => {
        progress = Math.min(100, progress + 3);
        progressFill.style.width = `${progress}%`;

        if (progress <= 30) progressText && (progressText.textContent = "Loading Portfolio...");
        else if (progress <= 60) progressText && (progressText.textContent = "Initializing Components...");
        else if (progress <= 90) progressText && (progressText.textContent = "Finalizing Setup...");
        else progressText && (progressText.textContent = "Ready!");

        if (progress >= 100) {
            clearInterval(progressInterval);
            setTimeout(() => {
                loadingScreen.style.transition = 'opacity 0.8s ease';
                loadingScreen.style.opacity = '0';
                setTimeout(() => {
                    loadingScreen.style.display = 'none';
                    window.dispatchEvent(new Event('introDone'));
                }, 800);
            }, 400);
        }
    }, 40);
}