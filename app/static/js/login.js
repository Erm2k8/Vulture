var user_or_email = document.getElementById("user-or-email");
var password = document.getElementById("password")

const regexName = /^[a-zA-Z\s_.-]+$/;
const regexEmail = /^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$/;
const regexPassword = /^(?=.*[a-zA-Z])(?=.*\d).{6,}$/;

var lineBreak = document.createElement("br");

