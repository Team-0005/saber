lock = false;
// Get the modal
var modal = [
  document.getElementById("id00"),
  document.getElementById("id01"),
  document.getElementById("id02"),
  document.getElementById("id03"),
  document.getElementById("id04"),
];

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  for (let index = 0; index < modal.length; index++) {
    if (event.target == modal[index]) {
      modal[index].style.display = "none";
    }
  }
};
// control modal
function get_modal(x) {
  modal[x].style.display = 'block';
}

function close_modal(x) {
  modal[x].style.display = 'none';
}

function change_modal(x, y) {
  close_modal(x);
  get_modal(y);
}



//return style to defult
function setDefult(input, message) {
  message.innerHTML = null;
  input.style.borderColor = "#5399B5";
}

//change style when error ocurs
function setError(input) {
  input.style.borderColor = "red";
}


//functions for check forms
//1
function check_symbol(input_id, message_id) {
  var regularExp = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/
  var input = document.getElementById(input_id);
  var message = document.getElementById(message_id);
  if (input.value.match(regularExp)) {
    setError(input);
    message.innerHTML = "الرجاء عدم استخدام رموز مثل */+";
    lock = true;
  }
  else {
    setDefult(input, message);
    lock = false;
  }
}

//2
function check_email(email_id, message_id) {
  var regularExp = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
  var email = document.getElementById(email_id);
  var message = document.getElementById(message_id);
  if (!email.value.match(regularExp)) {
    setError(email, message);
    message.innerHTML = "الرجاء التأكد من صحة البريد الالكتروني";
    lock = true;
  }
  else {
    setDefult(email, message);
    lock = false;
  }
}

//3
function check_pass(pass_id, confirm_pass_id, message_id) {
  var pass = document.getElementById(pass_id);
  var confirm_pass = document.getElementById(confirm_pass_id);
  var message = document.getElementById(message_id);
  if (pass.value != confirm_pass.value) {
    setError(pass);
    setError(passconfirm);
    message.innerHTML =
      " كلمة المرور غير متطابقة";
    lock = true;
  } else {
    if (pass.value == "" && passconfirm.value == "") {
      setError(pass);
      setError(confirm_pass);
      lock = true;
    }
    else {
      setDefult(pass, message);
      setDefult(passconfirm, message);
      lock = false;
    }
  }
}

//4
//force user to enter only number
function check_number(event) {
  var key = event.keyCode;
  return (key <= 57 && key >= 48);
}

//5
//force user to enter only letters
function check_letter(event) {
  var key = event.keyCode;
  return ((key >= 65 && key <= 90) || (key >= 97 && key <= 122));
};


$('#signin,#signup,#FG_pass,#profile').submit(function (evt) {
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
  for (var i = 0; i < profile.length - 6; i++) {
    profile[i].removeAttribute("disabled");
  }
}

//function for edit button in page
function cancel_func() {
  location.reload(); 
}