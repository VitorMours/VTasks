const { handleImageError } = require('./notes.js');
const task = require('./task.js');
document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.card-img-top');
    images.forEach(img => {
        img.onerror = img.classList.add("image-failed");
    });
});