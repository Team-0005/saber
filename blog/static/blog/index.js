function checksingin() {
  document.getElementById("massege").innerText = "الرجاء تسجيل الدخول اولا أو انشئ حساب";
}

// Get the modal
var modal = [document.getElementById('id00'),document.getElementById('id01'),document.getElementById('id02'),document.getElementById('id03'),document.getElementById('id04')];;

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (modal.find(event.target)) {
    modal.style.display = "none";
  }
}


// Add active class to the current control button (highlight it)
// var btnContainer = document.getElementById("myBtnContainer");
// var btns = btnContainer.getElementsByClassName("btn");
// for (var i = 0; i < btns.length; i++) {
//   btns[i].addEventListener("click", function() {
//     var current = document.getElementsByClassName("active");
//     current[0].className = current[0].className.replace(" active", "");
//     this.className += " active";
//   });
// }

//function for edit button in cpp/dpp page
function edit_func() {
  var profile = document.getElementById("profile").elements;
  for (var i = 2; i < profile.length; i++) {
    profile[i].removeAttribute("disabled");
  }
}


