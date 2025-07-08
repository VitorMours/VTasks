// Creating utility functions and values
const todoCheckbox = document.querySelectorAll(".list-group-item");

todoCheckbox.forEach((checkbox) => {
  checkbox.children[0].addEventListener("change", () => {
    console.log("hi");
    // TODO: Preciso adicionar o binding par amodificar o estilo da tarefa, e talvez modificar ela de aba
  });
});


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
}

document.addEventListener("DOMContentLoaded", function () {
  console.log("Elementos do DOM carregados...");
});

// Adding elements event listeners
const createTaskButton = document.querySelector("#createTask .btn-primary");

// Adding the interactivity
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

