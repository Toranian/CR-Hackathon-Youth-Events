// window.scrollBy({ 
//   top: 100, // could be negative value
//   left: 0, 
//   behavior: 'smooth' 
// });

// console.log("Working");

// function scrollTo(element) {
//   document.querySelector("#" + element).scrollIntoView(
//     {
//       behavior: 'smooth'
//   }
//   );

// }

var toggle = 1;
console.log(toggle);


function newsToggle() {
  
  toggle *= -1;
  return toggle;
  
}

if (toggle == 1) {
  document.getElementById("newsletter").style["left"] = "0px";
}


console.log(toggle);