document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ Script de GIT (Gerenciamento de Interatividade de Tasks) carregado...");

  const todoCheckboxList = document.querySelectorAll(".list-group-item");
  console.log(todoCheckboxList);
  // TODO: Aqui dentro, preciso ver uma forma de adicionar um listener para cada uma das checkbox, de forma que quando modificada, ele fique tracado, e modifique o local storage, permitindo que ele avise tambem o backend

});