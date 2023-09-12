const clock = document.querySelector("h2#clock");   //h2 clock 연결
//const clock = document..getElementById("clock");


function timeclock(){
    const date = new Date();

    const hour = String(date.getHours()).padStart(2, "0");
    const minute = String(date.getMinutes()).padStart(2, "0");
    const second = String(date.getSeconds()).padStart(2, "0");

    clock.innertext = (`${hour}:${minute}:${second}`);  //표시
}

timeclock();

setInterval(timeclock, 1000);    //코드를 일정 시간마다 반복