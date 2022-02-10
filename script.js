const daysEL = document.getElementById("days");
const hoursEL = document.getElementById("hours");
const minutesEL = document.getElementById("minutes");
const secondsEL = document.getElementById("seconds");

const elden = "11 Feb 2022 14:00:00";

function countdown(){
    const eldenDate = new Date(elden);
    const currentDate = new Date();

    const totalseconds = (eldenDate - currentDate) / 1000;

    const days = Math.floor(totalseconds/3600/24);
    const hours = Math.floor(totalseconds/3600) % 24;
    const minutes = Math.floor(totalseconds/60) % 60;
    const seconds = Math.floor(totalseconds) % 60 + 1;

    daysEL.innerHTML = formatTime(days);
    hoursEL.innerHTML = formatTime(hours);
    minutesEL.innerHTML = formatTime(minutes);
    secondsEL.innerHTML = formatTime(seconds);

}

function formatTime(time) {
    return time < 10 ? (`0${time}`) : time;
}
// initial call
countdown();

setInterval(countdown, 1000);

