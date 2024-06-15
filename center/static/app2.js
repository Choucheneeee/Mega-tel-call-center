
document.addEventListener('DOMContentLoaded', function() {
    
    let toggle = document.querySelector(".toggle");
    let body = document.querySelector('body');
    let countInterval;
    let temps;
    let hours;
    let minutes;
    let secondes;
    let wth;
    let wtm;
    let wts ;
    let shortbreak;
    let sb ;



    toggle.addEventListener('click',() => {
        body.classList.toggle('open');
        
        
    
    });


function getvalue(){

        let sound = document.getElementById("soundoption").checked;
        console.log("sound : " + sound);

        let vibrate = document.getElementById("vibrateoption").checked;
        console.log("vibrate : " + vibrate);
        let wth = document.getElementById("worktimehour").value;
        console.log("hour")
        console.log(wth)
        let wtm = document.getElementById("worktimemin").value;
        console.log("minute")
        console.log(wtm)
        let wts = document.getElementById("worktimesec").value;
        console.log("Work session : " + wtm + " minutes" + " et " + wts + " secondes");

        let sb = document.getElementById("shortbreak").value;
        let lb = document.getElementById("longbreak").value;
        console.log("Short break : " + sb + " minutes");
        console.log("Long break : " + lb + " minutes");

        let hours = document.getElementById("hours");
        let minutes = document.getElementById("minutes");
        let secondes = document.getElementById("secondes");

        hours.innerHTML = wth;

        minutes.innerHTML = wtm;
        secondes.innerHTML = wts;
    };



    let play = document.getElementById("play");
    console.log("plaay")
    let pause = document.getElementById("pause");

        hours = document.getElementById("hours");
        minutes = document.getElementById("minutes");
        secondes = document.getElementById("secondes");
    play.addEventListener('click', function (){
        
        console.log(secondes)
        console.log("playy")
        play.style.display="none";
        pause.style.display="flex";C:
        var audio = new Audio("{% static 'bip.mp3'%}");
        audio.play();
        
        wth = hours.innerHTML;
        wtm = minutes.innerHTML;
        wts = secondes.innerHTML;
        shortbreak = document.getElementById("shortbreak").value;
        sb = shortbreak.innerHTML;
        console.log("hours")
        
        console.log(wts);
    
        if (!temps) {
            const departHours = wth;
            const departMinutes = wtm;
            const departSecondes = wts;
            temps = departHours * 3600 + departMinutes * 60;
            temps += departSecondes % 60;
        }
    
        const timerElement = document.getElementById("circle");
        
        countInterval = setInterval(() => {
            hours = parseInt(temps / 3600, 10);
            minutes = parseInt((temps % 3600) / 60, 10);
            seconds = parseInt(temps % 60, 10);
            
            hours = hours < 10 ? "0" + hours : hours;
            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;
            
            timerElement.innerText = `${hours}:${minutes}:${seconds}`;
            temps = temps <= 0 ? 0 : temps - 1;
        }, 1000);
        calculateWorkedTime();

    });
    

pause.addEventListener('click', () => {
        pause.style.display="none";
        play.style.display="flex";
        clearInterval(countInterval);
        console.log("pause");
        calculateWorkedTime();

});
})