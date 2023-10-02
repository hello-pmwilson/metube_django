function menuList() {   
    console.log(window.innerWidth)
    if (window.innerWidth < 1200) {
      document.querySelectorAll('span').forEach(function(span){
        span.style.display = 'block';
      })
      
  } else {
      document.querySelectorAll('span').forEach(function(span){
        span.style.display = 'inline';
      })
  }
    
}

window.addEventListener('resize', menuList);
menuList();

// window.addEventListener('DOMContentLoaded', ()=>{
// const element = document.getElementById('arrow');
// //console.log("Arrow:", document.getElementById('arrow').getBoundingClientRect());

// const transparentRectangle = document.createElement('div');
// transparentRectangle.className = 'transparent-rectangle';
// const fadebutton = document.createElement('div');
// fadebutton.className = 'transparent-rectangle';
// const parentElement = document.getElementById('scrollable-buttons');
// parentElement.appendChild(fadebutton);
// })



