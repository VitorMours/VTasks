const allList = document.getElementById("todo-all-list");
const doneList = document.getElementById("todo-done-list");
const activeList = document.getElementById("todo-active-list");
const tasksCheckbox = document.getElementsByClassName("form-check-input me-1");

// TODO: Isso daqui tem que ser um event listener
function removeTaskFromList(list, listItemId) {
  const listItems = list.querySelectorAll("li");
  listItems.forEach((item) => {
    const checkbox = item.querySelector("input")
    if(checkbox.id == listItemId) {
      list.removeChild(item);
    }
  });
}

function addTaskToList(list, listItemId){
  const taskData = window.tasksJson.find((task) => task.id === listItemId);
  const taskDataIndex = window.tasksJson.findIndex((task) => task.id === listItemId);
  // console.log(taskData);
  if(taskData.task_conclusion === true){
    taskData.task_conclusion = false;
    window.tasksJson[taskDataIndex] = taskData; 
    addToActiveList(taskData);
    refreshLists();
  } else if (taskData.task_conclusion === false) {
    taskData.task_conclusion = true;
    window.tasksJson[taskDataIndex] = taskData; 
    addToDoneList(taskData);
    refreshLists();
  }
}

function addCheckboxEventListener() {
  for(let index = 0; index < tasksCheckbox.length; index++){
    const checkbox = tasksCheckbox[index];
    checkbox.addEventListener("change", () => {
      const checkboxLabel = checkbox.nextElementSibling;
      const task = checkbox.parentElement;
      if(checkbox.checked){
        checkboxLabel.classList.add("text-decoration-line-through");
        addTaskToList(doneList, checkbox.id); 
        removeTaskFromList(activeList, checkbox.id); 
      } else {
        checkboxLabel.classList.remove("text-decoration-line-through");
        addTaskToList(activeList, checkbox.id); 
        removeTaskFromList(doneList, checkbox.id); 
      }
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

function cleanLists(){
  allList.innerHTML = "";
  doneList.innerHTML = "";
  activeList.innerHTML = "";
}


function refreshLists(){
  const json = window.tasksJson;
  cleanLists();
  addToAllList(json);
  for(let i = 0; i < json.length; i++){
    if(!(json[i].task_conclusion)){
      addToActiveList(json[i]);
    } else {
      addToDoneList(json[i]);
    }
  }
  addCheckboxEventListener();  
}

document.addEventListener("DOMContentLoaded", function () {
  refreshLists();
  console.log("✅ Script de GIT (Gerenciamento de Interatividade de Tasks) carregado...");

});




