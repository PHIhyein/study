const quotes = [
    {
        quote : "q1",
        author : "a1"
    },
    {
        quote : "q2",
        author : "a2"
    },
    {
        quote : "q3",
        author : "a3"
    },
    {
        quote : "q4",
        author : "a4"   
    },
    {
        quote : "q5",
        author : "a5"
    },
    {
        quote : "q6",
        author : "a6"
    },
    {
        quote : "q7",
        author : "a7"
    },
    {
        quote : "q8",
        author : "a8"
    },
    {
        quote : "q9",
        author : "a9"
    },
    {
        quote : "q10",
        author : "a10"
    }
];  //명언/작가 목록

const quote = document.querySelector("#quote span:first-child");    //div 첫 번째
const author = document.querySelector("#quote span:last-child");    //div 마지막 번째

const dailyquote = quotes[Math.floor(Math.random()*quotes.length)]; //명언 랜덤으로 뽑음
quote.innerText = dailyquote.quote;
author.innerText = dailyquote.author;