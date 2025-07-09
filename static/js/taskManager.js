// Creating utility functions and values
const todoCheckbox = document.querySelectorAll(".list-group-item");

todoCheckbox.forEach((checkbox) => {
  checkbox.children[0].addEventListener("change", () => {
    console.log("hi");
    // TODO: Preciso adicionar o binding par amodificar o estilo da tarefa, e talvez modificar ela de aba
  });
});

document.addEventListener("DOMContentLoaded", function () {
    console.log("\u2705 Script de GIT( Gerenciamento de Interatividade de Tasks ) carregado...")
});