function postNewTask(json) {
  fetch("http://localhost:5000/todo", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(json)
  })
    .then(response => {
      return response;
    });
  window.tasksJson.push(json);
  location.reload();
}
// Adding elements event listeners
const createTaskButton = document.querySelector("#createTask .btn-primary");
if (createTaskButton) {
  createTaskButton.addEventListener("click", function () {
    let taskName = document.getElementById("task-name")
    let taskDescription = document.getElementById("task-description");

    let json = JSON.stringify(
      {
        "task_name": taskName.value,
        "task_description": taskDescription.value
      }
    );
    postNewTask(json);
    taskName.value = "";
    taskDescription.value = "";
  });
}

document.addEventListener("DOMContentLoaded", function () {
  console.log("\u2705 Script de Criação de Tasks Carregado...");
});