const { handleImageError } = require('./notes.js');
const task = require('../js/task.js');
const TaskManager = require('../js/taskManager.js');


const allList = document.getElementById("todo-all-list");
const doneList = document.getElementById("todo-done-list");
const activeList = document.getElementById("todo-active-list");

const deleteIconPath = document.body.dataset.deleteIcon;

document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.card-img-top');

    images.forEach(img => {
        img.onerror = img.classList.add("image-failed");
    });
});