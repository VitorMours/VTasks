import addConclusionInteraction from "./task.js";

const allTasks = document.getElementById("todo-all-tab-content");
const doneTasks = document.getElementById("todo-done-tab-content");
const activeTasks = document.getElementById("todo-active-tab-content");


addConclusionInteraction(allTasks);
addConclusionInteraction(doneTasks);
addConclusionInteraction(activeTasks);
