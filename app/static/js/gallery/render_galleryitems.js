const galleryItems = document.querySelectorAll('.gallery-item');
const previewImage = document.getElementById('previewImage');
const previewVideo = document.getElementById('previewVideo');
const previewOverlay = document.querySelector('.preview-overlay');
const preview = document.querySelector('.preview');

galleryItems.forEach(item => {
    // Skip folder items to prevent preview
    if (item.classList.contains('is-folder')) return;

    item.addEventListener('click', (event) => {
        const targetElement = event.target;

        // Only proceed if an image or video is clicked
        if (targetElement.tagName !== 'IMG' && targetElement.tagName !== 'VIDEO') {
            return;
        }

        // Hide both preview elements initially
        previewImage.style.display = 'none';
        previewVideo.style.display = 'none';

        if (targetElement.tagName === 'IMG') {
            // Show the image preview
            previewImage.src = targetElement.src;
            previewImage.style.display = 'block';
        } else if (targetElement.tagName === 'VIDEO') {
            // Show the video preview
            previewVideo.src = targetElement.src;
            previewVideo.style.display = 'block';
        }

        // Display preview and overlay
        preview.style.display = 'block';
        previewOverlay.style.display = 'block';
    });
});

previewOverlay.addEventListener('click', () => {
    // Hide preview and overlay when clicked
    preview.style.display = 'none';
    previewOverlay.style.display = 'none';

    // Pause video and reset the source
    if (previewVideo.src) {
        previewVideo.pause();
        previewVideo.src = '';
    }
});
