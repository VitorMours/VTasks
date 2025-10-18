/** 
 * @typedef {Object} Task
 * @property {string} id - ID da task que especifica ela dentro do banco de dados 
 * @property {string} task - Conteúdo principal da task para identificar ela
 * @property {boolean} task_conclusion - Status de conclusão da task
 * @property {string} task_description - Descrição detalhada da task
 * @property {string} user_id - ID do usuário responsável pela task
 */


const allTasksList = document.getElementById("todo-all-list");
const activeTasksList = document.getElementById("todo-active-list");
const doneTasksList = document.getElementById("todo-done-list");


function addInteractivityCustomization(list_){
    list_.addEventListener("click", (event) => {
        if(event.target.classList.contains("form-check-input")){
            
            const checkbox = event.target;
            const content = checkbox.nextElementSibling;

            if(!(checkbox.checked)){
                content.classList.remove("text-decoration-line-through", "text-secondary");
            }else{
                content.classList.add("text-decoration-line-through", "text-secondary");
            }
        }
    });
}

function createListItem(task, done = null){
    const checkedAttr = task.task_conclusion ? "checked" : "";
    const taskStructureString = 
        `
        <li class="list-group-item">
            <input type="checkbox" class="form-check-input me-1" id="${task.id}" ${checkedAttr}>
            <label class="form-check-label" for="${task.id}">
                <strong>${escapeHtml(task.task)}:</strong> ${escapeHtml(task.task_description)}
            </label> 
        </li>
        `;
    return taskStructureString;
}

function escapeHtml(str) {
    if (str === null || str === undefined) return "";
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

/**
 * @param {Task[]} tasks - Array de tasks para listar
 */
function ListateItems(tasks){
    if (!Array.isArray(tasks)) {
        return;
    }
    
    allTasksList.innerHTML = '';
    
    tasks.forEach((element, index) => {
        const listItem = createListItem(element);
        allTasksList.insertAdjacentHTML("beforeend", listItem);
        if(element.task_conclusion){
            const listItem = createListItem(element);
            doneTasksList.insertAdjacentHTML("beforeend", listItem);
        
        } else {
            const listItem = createListItem(element);
            activeTasksList.insertAdjacentHTML("beforeend", listItem);
        }
    
    });


}

document.addEventListener("DOMContentLoaded", () => {
    console.log("Carregando javascript...");
    if (typeof tasksJson === 'string') {
        ListateItems(JSON.parse(tasksJson));
    } else {
        ListateItems(tasksJson);
    }

    addInteractivityCustomization(allTasksList);
    addInteractivityCustomization(doneTasksList);
    addInteractivityCustomization(activeTasksList);

    console.log("Javascript carregado");
});