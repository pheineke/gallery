const galleryItems = document.querySelectorAll('.gallery-item');
    const previewImage = document.getElementById('previewImage');
    const previewVideo = document.getElementById('previewVideo');
    const previewOverlay = document.querySelector('.preview-overlay');
    const preview = document.querySelector('.preview');

    galleryItems.forEach(item => {
        item.addEventListener('click', (event) => {
            // Prevent the icon from being clicked for preview
            const targetElement = event.target;

            // If the clicked element is not an image or video, do nothing
            if (targetElement.tagName !== 'IMG' && targetElement.tagName !== 'VIDEO') {
                return;
            }

            // Hide both preview elements initially
            previewImage.style.display = 'none';
            previewVideo.style.display = 'none';

            if (targetElement.tagName === 'IMG') {
                // If an image was clicked, display the image preview
                previewImage.src = targetElement.src;
                previewImage.style.display = 'block';
            } else if (targetElement.tagName === 'VIDEO') {
                // If a video was clicked, display the video preview
                previewVideo.src = targetElement.src;
                previewVideo.style.display = 'block';
            }

            // Show the preview and overlay
            preview.style.display = 'block';
            previewOverlay.style.display = 'block';
        });
    });

    previewOverlay.addEventListener('click', () => {
        // Hide the preview and overlay when clicked
        preview.style.display = 'none';
        previewOverlay.style.display = 'none';
    
        // Pause the video if it's playing
        if (previewVideo.src) {
            previewVideo.pause();
            previewVideo.src = '';  // Reset the source to prevent caching issues
        }
    });
    