const formlogin = document.getElementById("formlogin");
const inputlogin = document.querySelector("#formlogin input");
const btnlogin = document.querySelector("#formlogin button");
const hello = document.getElementById("hello");


//로그인 버튼 클릭
function onclickloginbtn(event){
    event.preventDefault();                                                                         //f5 막음
    formlogin.classList.add("hidden");                                                              //add로 가리기 추가
    const username = inputlogin.value;
    localStorage.setItem("unm", username);
    hello.innerText = `${username}, 안녕`;                                                          //h1 안에 내용(넣기)
    hello.classList.remove("hidden");                                                               //remove로 가리기 없앰
}
formlogin.addEventListener("submit", onclickloginbtn);


//
const isusername = localStorage.getItem("unm");
if (isusername === null){
    formlogin.classList.remove("hidden");
    formlogin.addEventListener("submit", onclickloginbtn);
} else{
    hello.classList.remove("hidden");
    hello.innerText = `hello, ${isusername}`;
}













