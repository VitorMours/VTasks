// Making all the imports
import task from "../js/task.js";
import TaskManager from "../js/taskManager.js";
// Getting all the references
const allList = document.getElementById("todo-all-list");
const doneList = document.getElementById("todo-done-list");
const activeList = document.getElementById("todo-active-list");
const deleteIconPath = document.body.dataset.deleteIcon;


import addConclusionInteraction from "./task.js";

const allTasks = document.getElementById("todo-all-tab-content");
const doneTasks = document.getElementById("todo-done-tab-content");
const activeTasks = document.getElementById("todo-active-tab-content");


addConclusionInteraction(allTasks);
addConclusionInteraction(doneTasks);
addConclusionInteraction(activeTasks);
