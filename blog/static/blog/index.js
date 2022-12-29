function check_singin() {
  document.getElementById("massege").innerText =
    "الرجاء تسجيل الدخول اولا أو انشئ حساب";
}

// Get the modal
var modal = [
  document.getElementById("id00"),
  document.getElementById("id01"),
  document.getElementById("id02"),
  document.getElementById("id03"),
  document.getElementById("id04"),
];

// When the user clicks anywhere outside of the modal, close it
window.onclick = function () {
  for (let index = 0; index < modal.length; index++) {
    if (modal[index].style.display == "block") {
      element.style.display = "none";
    }
  }
};


function check_symbol() {}

function check_email() {}

function check_pass() {}

//function for edit button in page
function edit_func() {
  var profile = document.getElementById("profile").elements;
  for (var i = 2; i < profile.length; i++) {
    profile[i].removeAttribute("disabled");
  }
}
