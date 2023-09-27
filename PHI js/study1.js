

/*
//별 반복해서 찍기
let star = ""
for (let i = 0; i < 28; i++){
    for (let j = 0; j < 28 - i; j++){
        if (j % 2 != 0){
            star += " "
        }
    }
    if (i % 2 != 0){
        for (let k = 0; k < i; k++){
            star += "*"
        }
        console.log(`${star}`)
    }
    star = ""
}
*/

/*
//if문
let score = parseInt(prompt("성적 입력(0~100): "));

if (score < 0 || isNaN(score) || score > 100){
    console.log("올바른 점수 입력")
} else if (score > 90){
    console.log("A")
} else if (score > 80){
    console.log("B")
} else if (score > 70){
    console.log("C")
} else if (score > 60){
    console.log("D")
} else {
    console.log("F")
}
*/

/*
//if문
let a = parseInt(prompt("나이 입력: "));

if (isNaN(a) || a < 0){
    console.log("숫자를 입력");
} else if (a < 19){
    console.log("성인 아님");
} else if (a <= 50){
    console.log("음주 가능");
} else if (a <= 80){
    console.log("운동 필요");
} else {
    console.log("알아서 관리");
}
*/

/*
//객체+함수
const cal = {
    plus : function (a, b){
        console.log(`${a + b}`);
        return a + b;
    },
    minus : function (a, b){
        console.log(`${a - b}`);
        return a - b;
    },
    mul : function (a, b){
        console.log(`${a * b}`);
        return a * b;
    },
    div : function (a, b){
        console.log(`${a / b}`);
        return a / b;
    },
    power : function (a, b){
        console.log(`${a ** b}`);
        return a ** b;
    }
};

const resplus = cal.plus(1, 2);
console.log(resplus);

let a = prompt();
console.log(a);
*/