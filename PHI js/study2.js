/* <h1 class="hi" style="color:red">hello</h1> */


const hi = document.querySelector(".hi")

function Click(){
    if (hi.style.color === "blue"){
        hi.style.color = "red"
    } else if (hi.style.color === "red"){
        hi.style.color = "blue"
    }
}
function Mouseon(){
    hi.textContent = "hi"
    console.log("mouse on")
}
function Mouseup(){
    hi.textContent = "hello"
}
hi.addEventListener("click", Click)
hi.addEventListener("mouseover", Mouseon)
hi.addEventListener("mouseout", Mouseup)


/*

    <!--<h1 id="title">doc</h1>
    <h2 class="cs">cs1</h2>
    <h2 class="cs">cs2</h2>
    <h2 class="cs">cs3</h2>

    <div class="dd"><h1>dd</h1></div>-->


const title = document.getElementById("title");
title.textContent = "docid";

const csz = document.getElementsByClassName("cs");
console.log(csz);
//여러개 element 가져올 때 사용, 배열 리턴

const d = document.querySelector(".dd h1");
console.log(d);
//<class><안></></> class 안에 있는 것에 간섭할 수 있음

console.dir()
*/