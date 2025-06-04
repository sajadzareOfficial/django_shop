var second_element = document.getElementById("second")
var min_element = document.getElementById("min_element")
var hour_element = document.getElementById("hour_element")
var second=60
var min=60
var hour = 3

setInterval(function(){
    second --
    if (hour===0 && min===0 ){
        second=0
        return 
    }
    if(min===0){
        hour--
        min=1

    };
    if (second===0){
        min--
        second=5

    }
    hour_element.textContent=hour+"h"

    min_element.textContent=min+"m"

    second_element.textContent=second+"s"
},1000)