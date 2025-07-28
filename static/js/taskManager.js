 const allList = document.getElementById("todo-all-list");
const doneList = document.getElementById("todo-done-list");
const activeList = document.getElementById("todo-active-list");
const deleteIconPath = document.body.dataset.deleteIcon;

class TaskManager{
  /**
   * Loading the tasks received in the window object in the localStorage for better usage 
   * @param {list[dict]} tasks get a list of the tasks objects
   * @returns {boolean} return trues if the localstorage action was sucessfull
   */
  static loadTasksInLocalStorage(tasks){
    for(let i = 0; i < tasks.length; i++){
      const task = new Task(  
        taskName=tasks["task"], 
        taskDescription=tasks["task_description"],
        taskConclusion= tasks["task_conclusion"],
        id=tasks["id"],
        user_id=tasks["user_id"]
      );
      // TODO: Add the tasks to the local storage
    }
  }

  // TODO: Remake the addTasksToList function to a more specific and good function
  static addTaskToList(list) {
  
  }


  static refreshLists() {
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

  }

}




// TODO: Isso daqui tem que ser um event listener
function removeTaskFromList(list, listItemId) {
  const listItems = list.querySelectorAll("li");
  listItems.forEach((item) => {
    const checkbox = item.querySelector("input");
    if (checkbox && checkbox.id === listItemId) {
      list.removeChild(item);
    }
  });
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

document.addEventListener("DOMContentLoaded", function () {
  refreshLists();
  console.log("✅ Script de GIT (Gerenciamento de Interatividade de Tasks) carregado...");
});
