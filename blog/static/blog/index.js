lock = false;
//return style to defult
function setDefult(input, message) {
  message.innerHTML = null;
  input.style.borderColor = "#5399B5";
}

//change style when error ocurs
function setError(input,message) {
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
    message.innerHTML = null;
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
    setError(confirm_pass);
    message.innerHTML =" كلمة المرور غير متطابقة";
    lock = true;
  } else {
    if (pass.value == "" && confirm_pass.value == "") {
      setError(pass);
      setError(confirm_pass);
      lock = true;
    }
    else {
      setDefult(pass, message);
      setDefult(confirm_pass, message);
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
function check_arabic(event) {
  var regularExp = /[\u0600-\u06FF]/;
  var key = event.which;
  var str = String.fromCharCode(key);
  if(regularExp.test(str)){
    return true;
  }
  return false;
};

function check_letter(event) {
  var key = event.keyCode;
  return ((key >= 65 && key <= 90) || (key >= 97 && key <= 122));
}


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