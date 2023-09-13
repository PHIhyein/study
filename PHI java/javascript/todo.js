const fmTodo = document.getElementById("formTodo");
const liTodo = document.getElementById("listTodo");
const todoInput = document.querySelector("#formTodo input");


const Todo_key = "todos";

let todos = [];

function saveTodos(){
    localStorage.setItem(Todo_key, JSON.stringify(todos));
};


function delList(event){
    const li = event.target.parentElement;  //버튼의 부모 -> 리스트
    li.remove();    //삭제

    todos = todos.filter((newtodo) => newtodo.id !== parseInt(li.id));
    saveTodos();
}

function displayTodo(newtodo){
    const li = document.createElement("li");
    const span = document.createElement("span");
    li.id = newtodo.id;
    span.innerText = newtodo.text;

    const button = document.createElement("button");    //버튼 만듦
    button.innerText = "X"; //버튼 텍스트
    button.addEventListener("click", delList);  //삭제 기능

    li.appendChild(span);
    li.appendChild(button); //리스트에 버튼 넣음
    liTodo.appendChild(li);
};

function sblist(event){
    event.preventDefault(); //입력 시 f5 발생 막음
    const valueTodo = todoInput.value;
    todoInput.value = "";

    const nTodo = {
        text : valueTodo,
        id : Date.now(),
    };
    todos.push(nTodo);
    displayTodo(nTodo);
    saveTodos();
};
fmTodo.addEventListener("submit", sblist);


const saveTodo = localStorage.getItem(Todo_key);

if (saveTodo !== null){
  const parseTodo = JSON.parse(saveTodo);
  todos = parseTodo;
  parseTodo.forEach(displayTodo);
};
