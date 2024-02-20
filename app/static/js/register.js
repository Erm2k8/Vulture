var realName = document.getElementById("name");
var username = document.getElementById("username");
var email = document.getElementById("email");
var password = document.getElementById("password");
var confirmPassword = document.getElementById("confirm_password");

const regexUsername = /^[a-zA-Z0-9_.-]+$/;
const regexName = /^[a-zA-Z\s_.-]+$/;
const regexEmail = /^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$/;
const regexPassword = /^(?=.*[a-zA-Z])(?=.*\d).{6,}$/;

const fields = document.querySelectorAll('.form-item');
var lineBreak = document.createElement("br");

var nameIsValid = false;
var usernameIsValid = false;
var emailIsValid = false;
var passwordIsValid = false;
var confirmPasswordIsValid = false;

function setError(index) {
    fields[index].style.outline = "2px solid red";
}

function clearError(errorName, index) {
    fields[index].style.outline = "";
    if (lineBreak && lineBreak.parentNode === errorName) {
        errorName.removeChild(lineBreak);
    }
    errorName.textContent = "";
}

function nameValidate() {
    const nameError = document.getElementById('name-error');

    if (fields[0].value.length < 3) {
        nameError.style.display = "block";
        nameError.textContent = "Name's too short.";
        nameError.appendChild(lineBreak);
        nameIsValid = false;
        setError(0);
    } else if (fields[0].value.length > 120) {
        nameError.style.display = "block";
        nameError.textContent = "Name's too long.";
        nameError.appendChild(lineBreak);
        nameIsValid = false;
        setError(0);
    } else if (!regexName.test(fields[0].value)) {
        nameError.style.display = "block";
        nameError.textContent = "Invalid name.";
        nameError.appendChild(lineBreak);
        nameIsValid = false;
        setError(0);
    } else {
        clearError(nameError, 0);
        nameIsValid = true;
    }
}

function usernameValidate() {
    const usernameError = document.getElementById('username-error');

    if (fields[1].value.length < 3) {
        usernameError.style.display = "block";
        usernameError.textContent = "Username's too short.";
        usernameError.appendChild(lineBreak);
        usernameIsValid = false;
        setError(1);
    } else if (fields[1].value.length > 20) {
        usernameError.style.display = "block";
        usernameError.textContent = "Username's too long.";
        usernameError.appendChild(lineBreak);
        usernameIsValid = false;
        setError(1);
    } else if (!regexUsername.test(fields[1].value)) {
        usernameError.style.display = "block";
        usernameError.textContent = "Invalid username.";
        usernameError.appendChild(lineBreak);
        usernameIsValid = false;
        setError(1);
    } else {
        clearError(usernameError, 1);
        usernameIsValid = true;
    }
}

function emailValidate() {
    const emailError = document.getElementById('email-error');

    if (!regexEmail.test(fields[2].value)) {
    emailError.style.display = "block";
    emailError.textContent = "Invalid email.";
    emailError.appendChild(lineBreak);
    emailIsValid = false;
    setError(2);
    } else {
        clearError(emailError, 2);
        emailIsValid = true;
    }
}

function passwordValidate() {
    const passwordError = document.getElementById('password-error');

    if (!regexPassword.test(fields[3].value)) {
        passwordError.style.display = "block";
        passwordError.textContent = "At least 6 characters of letters and numbers.";
        passwordError.appendChild(lineBreak);
        passwordIsValid = false;
        setError(3);
    } else {
        clearError(passwordError, 3);
        passwordIsValid = true;
    }
}

function confirmPasswordValidate() {
    const confirmPassword = document.getElementById('confirm-password')
    const confirmPasswordError = document.getElementById('confirm-password-error');

    if (confirmPassword.value !== password.value) {
        confirmPasswordError.style.display = 'block';
        confirmPasswordError.textContent = "Passwords do not match.";
        confirmPasswordError.appendChild(lineBreak);
        confirmPasswordIsValid = false;
        setError(4);
    } else {
        clearError(confirmPasswordError, 4)
        confirmPasswordIsValid = true;
    }
}   

function formIsValid(event) {
    if (!nameIsValid || !usernameIsValid || !emailIsValid || !passwordIsValid || !confirmPasswordIsValid) {
        event.preventDefault();
        console.log('erro');
    } else {
        console.log("ué porra");
    }
}
