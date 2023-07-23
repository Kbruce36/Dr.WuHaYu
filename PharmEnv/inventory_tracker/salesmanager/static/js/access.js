// Assign all elements
//these methodds are used to select elements from the html documentby their ID, class, tag name or css
const demoId = document.getElementById('demo');
const demoClass = document.getElementsByClassName('demo');
const demoTag = document.getElementsByTagName('article');
const demoQuery = document.querySelector('#demo-query');
const demoQueryAll = document.querySelectorAll('.demo-query-all');

// Change border of ID demo to purple
//once selected, the code changes their border color to a different color for each group of elements
demoId.style.border = '1px solid purple';

// Change border of class demo to orange
//demo class elements border changed to orange
for (i = 0; i < demoClass.length; i++) {
  demoClass[i].style.border = '1px solid orange';
}

// Change border of tag demo to blue
// demo class elements assigned to  a blue border
for (i = 0; i < demoTag.length; i++) {
  demoTag[i].style.border = '1px solid blue';
}

// Change border of ID demo-query to red
demoQuery.style.border = '1px solid red';

// Change border of class query-all to green
demoQueryAll.forEach(query => {
  query.style.border = '1px solid green';
});


//Carousel functionality
$(document).ready(function(){
  // Activate Carousel
  $("#demo").carousel();
  
  // Enable Carousel Indicators
  $(".carousel-indicators li").click(function(){
    $("#demo").carousel(parseInt($(this).attr('data-slide-to')));
  });
  
  // Enable Carousel Controls
  $(".carousel-control-prev").click(function(){
    $("#demo").carousel("prev");
  });
  $(".carousel-control-next").click(function(){
    $("#demo").carousel("next");
  });
});

function hide(target){
  var target = document.getElementById(target);
  target.setAttribute("style", "display:none;");

}