form = false;
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

function check_symbol(input_id,inputmessage) {
  var input =  document.getElementById(input_id);
  var regularExp =/[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/
  if (input.value.match(regularExp)){
    input.style.borderColor='red';
    document.getElementById(inputmessage).innerHTML="الرجاء عدم استخدام رموز مثل */+";
    form = false;
  }
  else{
    document.getElementById(inputmessage).innerHTML= null;
    input.style.borderColor = "#5399B5";
    form = true;
  }
}

function check_email(mail_id,mailmessage) {
  var input =  document.getElementById(mail_id);
  var regularExp = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
  if (!input.value.match(regularExp)){
    input.style.borderColor='red';
    document.getElementById(mailmessage).innerHTML="الرجاء التأكد من صحة البريد الالكتروني";
  }
  else{
    document.getElementById(mailmessage).innerHTML= null;
    input.style.borderColor = "#5399B5";
    form = true;
  }
}

//Checking password function
function check_pass(pass_id,passconfirm_id,message_id) {
  var pass = document.getElementById(pass_id);
  var passconfirm = document.getElementById(passconfirm_id);

  if (pass.value != passconfirm.value) {
    pass.style.borderColor = "red";
    passconfirm.style.borderColor = "red";
    document.getElementById(message_id).innerHTML =
      " كلمة المرور غير متطابقة";
  } else {
    if (pass.value == "" && passconfirm.value == "") {
      pass.style.borderColor = "red";
      passconfirm.style.borderColor = "red";
    } else {
      document.getElementById("passmessage").innerHTML = null;
      pass.style.borderColor = "#5399B5";
      passconfirm.style.borderColor = "#5399B5";
      form = true;
    }
  }
}

//function for edit button in page
function edit_func() {
  var profile = document.getElementById("profile").elements;
  for (var i = 2; i < profile.length; i++) {
    profile[i].removeAttribute("disabled");
  }
}
function check_form(){
  if (!form){
    
  }
}