import axios from "axios";

function getAllTasks(taskList){
    const tasks = taskList;
    const list = tasks.childNodes[1].children;
    return list;
}

function addConclusionInteraction(tasksList) {
  const tasks = getAllTasks(tasksList);
  [...tasks].forEach((task) => {
    const task_division = task.children;
    const checkbox = task_division[0].children[0];
    const textElement = task_division[0];

    checkbox.addEventListener("change", (event) => {
      if (event.target.checked) {
        textElement.className = "text-decoration-line-through";
        console.log(`Checkbox for task "${textElement.innerText}" is checked.`);
      } else {
        textElement.className = ""; // remove estilo quando desmarcar
        console.log(`Checkbox for task "${textElement.innerText}" is unchecked.`);
      }
    });
  });
}


export default addConclusionInteraction;