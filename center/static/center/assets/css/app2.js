
let toggle = document.querySelector(".toggle");
let body = document.querySelector('body');

toggle.addEventListener('click',() => {
    body.classList.toggle('open');
    
  
});


function getvalue(){

    let sound = document.getElementById("soundoption").checked;
    console.log("sound : " + sound);

    let vibrate = document.getElementById("vibrateoption").checked;
    console.log("vibrate : " + vibrate);

    let wtm = document.getElementById("worktimemin").value;
    let wts = document.getElementById("worktimesec").value;
    console.log("Work session : " + wtm + " minutes" + " et " + wts + " secondes");

    let sb = document.getElementById("shortbreak").value;
    let lb = document.getElementById("longbreak").value;
    console.log("Short break : " + sb + " minutes");
    console.log("Long break : " + lb + " minutes");


    let minutes = document.getElementById("minutes");
    let secondes = document.getElementById("secondes");

    minutes.innerHTML = wtm;
    secondes.innerHTML = wts;
};



let play = document.getElementById("play");
    console.log("plaay")
let pause = document.getElementById("pause");


play.addEventListener('click', function (){
    play.style.display="none";
    pause.style.display="flex";

    
        
        var audio = new Audio('bip.mp3');
        audio.play();
    
    let minutes = document.getElementById("minutes");
    let secondes = document.getElementById("secondes");
    let wtm = minutes.innerHTML;
    let wts = secondes.innerHTML;
    let shortbreak = document.getElementById("shortbreak").value;
    let sb = shortbreak.innerHTML;
     console.log(wts);


    if (wtm > 0 && wts >= 0) {
        const departMinutes = wtm;
        const departSecondes = wts;
        let temps = departMinutes * 60;
        temps += departSecondes % 60;
        
        const timerElement = document.getElementById("circle");
        
        let countInterval = setInterval(() => {
          let minutes = parseInt(temps / 60, 10);
          let secondes = parseInt(temps % 60, 10);
        
          minutes = minutes < 10 ? "0" + minutes : minutes;
          secondes = secondes < 10 ? "0" + secondes : secondes;
        
          timerElement.innerText = `${minutes}:${secondes}`;
          temps = temps <= 0 ? 0 : temps - 1;
        }, 1000);
    }else{

        if (minutes = "0") {
        
        var audio = new Audio('bip.mp3');
        audio.play();
    }else{

    };
        const departMinutes = sb;
        let temps = departMinutes * 60;
        let title = document.getElementById("taskname");
        
        title.innerHTML = "Pause time";
        const timerElement = document.getElementById("circle");
        
        let countInterval = setInterval(() => {
          let minutes = parseInt(temps / 60, 10);
          let secondes = parseInt(temps % 60, 10);
        
          minutes = minutes < 10 ? "0" + minutes : minutes;
          secondes = secondes < 10 ? "0" + secondes : secondes;
        
          timerElement.innerText = `${minutes}:${secondes}`;
          temps = temps <= 0 ? 0 : temps - 1;
        }, 1000);
    };
});


pause.addEventListener('click', () => {
    pause.style.display="none";
    play.style.display="flex";
    clearInterval(countInterval);
    console.log("test");
});


