let imageNumber = 0;
let time = 6000;
let timer;
let sliderLine;


function goLeft(){
    sliderLine.style.left = -(sliderLine.offsetWidth / 6 * imageNumber) + "px";
    imageNumber++;
    if(imageNumber > 5){
        imageNumber = 0;
    }

    autoSlider();
}

function autoSlider(){
    timer = setTimeout(goLeft, time);
}

document.addEventListener("DOMContentLoaded", function(event) {
    sliderLine = document.querySelector(".sliderLine");
    autoSlider();
    document.querySelector(".slider").addEventListener('mouseenter', function(){
        clearTimeout(timer);
    });
    document.querySelector(".slider").addEventListener('mouseleave', function(){
        timer = setTimeout(goLeft, time);
    });
});