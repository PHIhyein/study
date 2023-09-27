//weather key: 7ee9c6f9f97c5394634d0b2f50d112d5
// https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}


function onGeoOK(position){
    console.log(position);
    const lat = position.coords.latitude;   //위도 가져옴
    const lon = position.coords.longitude;  //경도 가져옴
    console.log(`위도: ${lat}, 경도: ${lon}`);

    const API_key = "7ee9c6f9f97c5394634d0b2f50d112d5";
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_key}&units=metric`;

    fetch(url).then(response => response.json()).then(data=>{
        console.log(data.name, data.weather[0].description, data.main.temp);
        const weather = document.querySelector("#weather span:first-child");
        const city = document.querySelector("#weather span:last-child");
        city.innerText = data.name;
        weather.innerText = data.weather[0].description;
    })
}

function onGeoError(){
    console.log("날씨 문제");
}

navigator.geolocation.getCurrentPosition(onGeoOK, onGeoError);

