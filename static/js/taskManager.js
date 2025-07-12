document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ Script de GIT (Gerenciamento de Interatividade de Tasks) carregado...");

  const todoCheckbox = document.querySelectorAll(".list-group-item");
  todoCheckbox.forEach((checkbox) => {
    checkbox.children[0].addEventListener("change", () => {
      console.log("hi");
      // TODO: modificar estilo da tarefa ou mover de aba
    });
  });

});