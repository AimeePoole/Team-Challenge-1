//let video = document.getElementById("video-player");

// console.log(video.src); // Will print "videos/walter-lewin-pendulum-experiment.webm"
// video.src = "videos/new-video.mp3";
//video.play(); // Start playing the video
//video.pause(0.5); // Pause the video at the current moment
//console.log(video.currentTime); // Will print the current playback time in seconds
//video.currentTime = 0; // Will take the video back to the beginning

<button id="press-me" type="button"> </button>

let pressMe = document.getElementById("pressme");

function pressMeClicked() {
    //console.log("Howdy!")
    video.play();
}

pressMe.addEventListener("click", pressmeClicked)

