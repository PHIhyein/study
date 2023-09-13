const formlogin = document.querySelector("#formlogin");
const inputlogin = document.querySelector("#formlogin input");
const hello = document.getElementById("hello");

const HIDDEN_CLASSNAME = "hidden";
const KEY_USERNAME = "username";


//로그인 버튼 클릭
function onclickloginbtn(event){
    event.preventDefault(); //f5 막음
    formlogin.classList.add(HIDDEN_CLASSNAME);  //add로 가리기 추가
    const username = inputlogin.value;
    localStorage.setItem("username", username);
    displayHello(username);
}


function displayHello(argname){
    hello.innerText = `hello ${argname}`;
    hello.classList.remove(HIDDEN_CLASSNAME);
}


let isusername = localStorage.getItem("username");

if (isusername === null){   //비어있음
    formlogin.classList.remove(HIDDEN_CLASSNAME);   //숨기지 않음
    formlogin.addEventListener("submit", onclickloginbtn);
} else{
    displayHello(isusername);
}

