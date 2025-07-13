const allList = document.getElementById("todo-all-list");
const doneList = document.getElementById("todo-done-list");
const activeList = document.getElementById("todo-active-list");


function addToAllList(tasks) {
  for(let i = 0; i < tasks.length; i++){
    const listItem = document.createElement("li");
    const taskStructure = `
      <input type="checkbox" class="form-check-input me-1" id="${tasks[i].id}" ${tasks[i].task_conclusion ? "checked" : "" }>
      <label class="form-check-label" for="${tasks[i].id}">
        <strong> ${tasks[i].task} :</strong> ${tasks[i].task_description} 
      </label>
    `
    listItem.classList.add("list-group-item");
    listItem.innerHTML += taskStructure;
    allList.appendChild(listItem);
  }
}




document.addEventListener("DOMContentLoaded", function () {
  const json = window.tasksJson;
  for(let i = 0; i < json.length; i++){}
  addToAllList(json);
  console.log("✅ Script de GIT (Gerenciamento de Interatividade de Tasks) carregado...");
});

