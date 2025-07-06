// Creating utility functions and values

function postNewTask(json){


}

// Adding window event listener
document.addEventListener("DOMContentLoaded", function () {
  console.log("Elementos do DOM carregados...");
  taskName.value = "";
  taskDescription.value = "";
});

// Adding elements event listeners
const createTaskButton = document.querySelector("#createTask .btn-primary");

// Adding the interactivity
if(createTaskButton) {
  createTaskButton.addEventListener("click", function(){
    const taskName = document.getElementById("task-name")
    const taskDescription = document.getElementById("task-description");
    
    let json = JSON.stringify(
      {"task_name": taskName.value, 
       "task_description":taskDescription.value}
    );

    postNewTask() 



    taskName.value = "";
    taskDescription.value = "";
  });
}

