const fmTodo = document.getElementById("formTodo");
const liTodo = document.getElementById("listTodo");


function nr(event){
    event.preventDefault();
};
fmTodo.addEventListener("submit", nr);  //입력 시 f5 발생 막음
