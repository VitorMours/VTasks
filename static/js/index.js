import { task_name_handler, task_description_handler, create_task_modal } from './task.js';

const taskName = document.getElementById("task-name");
const taskDescription = document.getElementById("task-description");
const createTaskButton = document.getElementById("btn-create-task");

document.addEventListener("DOMContentLoaded", () => {
    taskName.addEventListener("input", task_name_handler);
    taskDescription.addEventListener("input", task_description_handler);
    createTaskButton.addEventListener("click", create_task_modal);
});