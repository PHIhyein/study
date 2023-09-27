const quotes = [
    {
        quote : "나는 별 하나에 아름다운 말 한 마디씩 불러 봅니다.",
        author : "\n-윤동주 <별 헤는 밤>"
    },
    {
        quote : "가장 뛰어난 예언자는 과거이다.",
        author : "\n-바이런"
    },
    {
        quote : "나는 생각한다. 고로 존재한다.",
        author : "\n-데카르트"
    },
    {
        quote : "말은 행동의 거울이다.",
        author : "\n-솔론"   
    },
    {
        quote : "영원히 살 것처럼 꿈을 꾸고 내일 죽을 것처럼 오늘을 살아라.",
        author : "\n-제임스딘"
    },
    {
        quote : "사막이 아름다운 것은 어딘가에 샘을 숨기고 있기 때문이다.",
        author : "\n-생택쥐베리"
    },
    {
        quote : "인간은 생각하는 갈대이다.",
        author : "\n-파스칼"
    },
    {
        quote : "인생의 어려움은 선택에 있다.",
        author : "\n-무어"
    },
    {
        quote : "그립다고 써보니 차라리 말을 말자 \n그냥 긴 세월이 지났노라고만 쓰자",
        author : "\n-윤동주 <편지>"
    },
    {
        quote : "죽는 날까지 하늘을 우러러 \n한 점 부끄러움이 없기를",
        author : "\n-윤동주 <서시>"
    }
];  //명언/작가 목록

const quote = document.querySelector("#quote span:first-child");    //div 첫 번째
const author = document.querySelector("#quote span:last-child");    //div 마지막 번째

const dailyquote = quotes[Math.floor(Math.random()*quotes.length)]; //명언 랜덤으로 뽑음
quote.innerText = dailyquote.quote;
author.innerText = dailyquote.author;