const allList = document.getElementById("todo-all-list");
const doneList = document.getElementById("todo-done-list");
const activeList = document.getElementById("todo-active-list");
const tasksCheckbox = document.getElementsByClassName("form-check-input me-1");

// TODO: Isso daqui tem que ser um event listener
function removeTaskFromList(list, listItem) {
  console.log(list);
  console.log(listItem);
}

function addTaskToList(list, listItem){
  console.log("PASS AND IGNORE");
}

function addCheckboxEventListener() {
  for(let index = 0; index < tasksCheckbox.length; index++){
    const checkbox = tasksCheckbox[index];
    checkbox.addEventListener("change", () => {
      checkboxLabel = checkbox.nextElementSibling;
      if(checkbox.checked){
        checkboxLabel.classList.add("text-decoration-line-through");
      } else {
        checkboxLabel.classList.remove("text-decoration-line-through");
      }
      removeTaskFromList(allList, checkbox.parentElement);
    });
  }
}
// TODO: Preciso adicionar a interatividade entre as abas

function addToAllList(tasks) {
  for(let i = 0; i < tasks.length; i++){
    const listItem = document.createElement("li");
    const taskStructure = `
      <input type="checkbox" class="form-check-input me-1" id="${tasks[i].id}" ${tasks[i].task_conclusion ? "checked" : "" }>
      <label class="form-check-label ${ (tasks[i].task_conclusion == true) ? "text-decoration-line-through" : "" }" for="${tasks[i].id}">
        <strong> ${tasks[i].task} :</strong> ${tasks[i].task_description} 
      </label>
    `
    listItem.classList.add("list-group-item");
    listItem.innerHTML += taskStructure;
    allList.appendChild(listItem);
  }
}

function addToActiveList(task){
    const listItem = document.createElement("li");
    const taskStructure = `
      <input type="checkbox" class="form-check-input me-1" id="${task.id}" ${task.task_conclusion ? "checked" : "" }>
      <label class="form-check-label" for="${task.id}">
        <strong> ${task.task} :</strong> ${task.task_description} 
      </label>
    `
    listItem.classList.add("list-group-item");
    listItem.innerHTML += taskStructure;
    activeList.appendChild(listItem);
}

function addToDoneList(task){
    const listItem = document.createElement("li");
    const taskStructure = `
      <input type="checkbox" class="form-check-input me-1" id="${task.id}" ${task.task_conclusion ? "checked" : "" }>
      <label class="form-check-label ${task.task_conclusion ? "text-decoration-line-through" : "" }" for="${task.id}" >
        <strong> ${task.task} :</strong> ${task.task_description} 
      </label>
    `
    listItem.classList.add("list-group-item");
    listItem.innerHTML += taskStructure;
    doneList.appendChild(listItem);
}

document.addEventListener("DOMContentLoaded", function () {
  const json = window.tasksJson;
  addToAllList(json);
  for(let i = 0; i < json.length; i++){
    if(!(json[i].task_conclusion)){
      addToActiveList(json[i]);
    } else {
      addToDoneList(json[i]);
    }
  }


  addCheckboxEventListener();  
  console.log("✅ Script de GIT (Gerenciamento de Interatividade de Tasks) carregado...");

});




