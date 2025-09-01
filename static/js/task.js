import axios from "axios";
let newTaskName = "";
let newTaskDescription = "";

export function task_name_handler(event){
  newTaskName = event.target.value;
}

export function task_description_handler(event){
  newTaskDescription = event.target.value;
}

export function create_task_modal() {
  const userId = sessionStorage.getItem("user_id");
  postTask(newTaskName, newTaskDescription, userId);
}


async function postTask(name, description, userId){
  await axios.post("/api/todo/", {  
    task: name,
    task_description: description,
    user_id: userId
  });
}

