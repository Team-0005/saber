lock = false;

//4
//force user to enter only number
function check_number(event) {
  var key = event.keyCode;
  return (key <= 57 && key >= 48);
}

//5
//force user to enter only letters
function check_letter(event) {
  var regularExp = /[\u0600-\u06FF]/;
  var key = event.which;
  var str = String.fromCharCode(key);
  if(regularExp.test(str)){
    return true;
  }
  return false;
};


$('#signin,#signup,#FG_pass,#profile,#patient').submit(function (evt) {
  if (lock) {
    evt.preventDefault();
  }
});

//function for edit button in page
function edit_func() {
  document.getElementById('save').type = 'submit';
  document.getElementById('edit').style.display = 'none';
  document.getElementById('cancel').style.display = 'inline-block';
  var profile = document.getElementById("profile").elements;
  for (var i = 0; i < profile.length - 1; i++) {
    if (profile[i].hasAttribute("value")) {
      profile[i].removeAttribute("disabled");
    }
    // profile[i].removeAttribute("disabled");
  }
}

//function for edit button in page
function cancel_func() {
  location.reload(); 
}