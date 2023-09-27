const fmTodo = document.getElementById("formTodo");
const liTodo = document.getElementById("listTodo");
const todoInput = document.querySelector("#formTodo input");


const Todo_key = "todos";

let todos = [];

function saveTodos(){
    localStorage.setItem(Todo_key, JSON.stringify(todos));  //json.stringify: 오브젝트를 문자열로 바꿈
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
    li.id = newtodo.id; //넣은 리스트 내용 아이디
    span.innerText = newtodo.text;  //넣은 리스트 내용

    const button = document.createElement("button");    //버튼 만듦
    button.innerText = "X"; //버튼 텍스트
    button.addEventListener("click", delList);  //삭제 기능

    li.appendChild(span);   //넣은 리스트 내용 넣음
    li.appendChild(button); //리스트에 버튼 넣음
    liTodo.appendChild(li); //화면에 리스트 내용과 버튼 표시
};

function sblist(event){
    event.preventDefault(); //입력 시 f5 발생 막음
    const valueTodo = todoInput.value;  //input에 넣은거 넣음
    todoInput.value = "";   //input 초기화

    const nTodo = {
        text : valueTodo,
        id : Date.now(),    //아이디 현재날짜
    };
    todos.push(nTodo);  //리스트에 넣음
    displayTodo(nTodo);
    saveTodos();
};
fmTodo.addEventListener("submit", sblist);


const saveTodo = localStorage.getItem(Todo_key);

if (saveTodo !== null){
  const parseTodo = JSON.parse(saveTodo);   //json.parse:문자열을 오브젝트로 바꿈
  todos = parseTodo;
  parseTodo.forEach(displayTodo);
};
