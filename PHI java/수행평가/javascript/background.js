const imgs = ["cat_ice_cream.jpg", "ice_cream.jpg", "ice_cream2.jpg", "library.jpg", "melting_love.jpg"];   //이미지 목록

const dailyimg = imgs[Math.floor(Math.random()*imgs.length)];   //이미지 랜덤으로 정함

const bgimg = document.createElement("img");    //태그부여

bgimg.src = `js_img/${dailyimg}`;   //이름 합침

//document.body.append(bgimg);    //이미지 추가

const pickbg = document.querySelector("#bg");
pickbg.append(bgimg);
//이미지를 div에 추가