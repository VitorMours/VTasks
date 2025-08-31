const allList = document.getElementById("todo-all-list");
const doneList = document.getElementById("todo-done-list");
const activeList = document.getElementById("todo-active-list");


async function requestTasks(){
  try{
    const tasks = await axios.get();


  }catch(error){
    throw error;
  }
}


function addCheckboxEventListener() {
  const tasksCheckbox = document.getElementsByClassName("form-check-input");
  for (let index = 0; index < tasksCheckbox.length; index++) {

    const checkbox = tasksCheckbox[index];
    checkbox.addEventListener("change", () => {
      const label = checkbox.nextElementSibling;
      const id = checkbox.id;

      if (checkbox.checked) {
        label.classList.add("text-decoration-line-through");
        addTaskToList(doneList, id);
        removeTaskFromList(activeList, id);
      } else {
        label.classList.remove("text-decoration-line-through");
        addTaskToList(activeList, id);
        removeTaskFromList(doneList, id);
      }

    });
  }
}

function removeTaskFromList(list, listItemId) {
  const listItems = list.querySelectorAll("li");
  listItems.forEach((item) => {
    const checkbox = item.querySelector("input");
    if (checkbox && checkbox.id === listItemId) {
      list.removeChild(item);
    }
  });
}

function addToAllList(tasks) {
  for (let i = 0; i < tasks.length; i++) {
    const task = tasks[i];
    const listItem = document.createElement("li");
    const checked = task.task_conclusion ? "checked" : "";
    const textDecoration = task.task_conclusion ? "text-decoration-line-through" : "";

    const taskStructure = `
      <div class="d-flex justify-content-between w-full align-baseline">
        <div>
          <input type="checkbox" class="form-check-input me-1" id="${task.id}" ${checked}>
          <label class="form-check-label ${textDecoration}" for="${task.id}">
            <strong>${task.task}:</strong> ${task.task_description}
          </label>
        </div>
        <img src="${deleteIconPath}" alt="Delete"></img>
      </div>
    `;

    listItem.classList.add("list-group-item");
    listItem.innerHTML = taskStructure;
    allList.appendChild(listItem);
  }
}

function addToActiveList(task) {
  const listItem = document.createElement("li");
  const taskStructure = `
    <input type="checkbox" class="form-check-input me-1" id="${task.id}">
    <label class="form-check-label" for="${task.id}">
      <strong>${task.task}:</strong> ${task.task_description}
    </label>
  `;
  listItem.classList.add("list-group-item");
  listItem.innerHTML = taskStructure;
  activeList.appendChild(listItem);
}

function addToDoneList(task) {
  const listItem = document.createElement("li");
  const taskStructure = `
    <input type="checkbox" class="form-check-input me-1" id="${task.id}" checked>
    <label class="form-check-label text-decoration-line-through" for="${task.id}">
      <strong>${task.task}:</strong> ${task.task_description}
    </label>
  `;
  listItem.classList.add("list-group-item");
  listItem.innerHTML = taskStructure;
  doneList.appendChild(listItem);
}

function cleanLists() {
  allList.innerHTML = "";
  doneList.innerHTML = "";
  activeList.innerHTML = "";
}

function refreshLists() {
  const json = window.tasksJson || [];
  cleanLists();
  addToAllList(json);

  json.forEach((task) => {
    if (task.task_conclusion) {
      addToDoneList(task);
    } else {
      addToActiveList(task);
    }
  });

  addCheckboxEventListener(); // Reaplica os event listeners após atualizar DOM
}

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
  TaskManager.loadTasksInLocalStorage(window.tasksJson);
  // location.reload();
  // TaskManager.loadTasksInLocalStorage(window.tasksJson);
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

function postAllTasks(){
  const tasks = window.tasksJson;
  console.log(tasks);
  fetch("http:localhost:5000/todo", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(tasks)
  }).then(response => {return response;})


}