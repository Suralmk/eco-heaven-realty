if (typeof window !== "undefined")
{

const fname = document.getElementById("fname")
const lname = document.getElementById("lname")
const email = document.getElementById("email")
const password = document.getElementById("password")
const confirmPassword = document.getElementById("confirm-password")
const form = document.getElementById("form")

form.addEventListener("submit", (e) =>{
    e.preventDefault();

    validateInputs();
});

    function validateInputs(){
        fnameValue = fname.value.trim()
        lnameValue = lname.value.trim()
        emailValue = email.value.trim()
        passwordValue = password.value.trim()
        confirmPasswordValue = confirmPassword.value.trim()

        //validating first name
        if (fnameValue === '' || fnameValue === null){
            setErrorFor(fname, "Enter your first name!");
        }else{
            setSuccessFor(fname);
        }

        //validating last name
        if (lnameValue === '' || lnameValue === null){
            setErrorFor(lname, "Enter your last name!");
        }else{
            setSuccessFor(lname);
        }

        //validating email
        if (emailValue === '' || emailValue === null){
            setErrorFor(email, "Enter your email!");
        }else if(!trueEmail(emailValue)){
            setErrorFor(email, "Enter a valid email!");
        }else{
            setSuccessFor(email);
        }

        //validating password
        if (passwordValue === '' || passwordValue === null) {
            setErrorFor(password, "Enter password!");
        }else if (passwordValue.length < 8){
            setErrorFor(password, "Password must be 8 charachter!")
        }
        else{
            setSuccessFor(password);
        }

        if (confirmPasswordValue === '' || confirmPasswordValue === null){
            setErrorFor(confirmPassword, "Confirm your password!");
        }else if (confirmPasswordValue !== passwordValue){
            setErrorFor(confirmPassword, "Password does not match!");
        }else{
            setSuccessFor(confirmPassword);
        }
    }

    function setErrorFor(input, message){
        const format = input.parentElement;
        const displayError = format.querySelector("#errormessage");

        //isplaying the message, passing the error meaasge
        displayError.innerText = message;

        //adding error class to format and removing success
        format.classList.remove("success");
        format.classList.add("error");
        
    }

    function setSuccessFor(input){
        const format = input.parentElement;
        const displayError = format.querySelectorAll("#errormessage");

        //displaying error message of empty string
        displayError.innerText = " new";

        //removing success class and removing  error class
        format.classList.remove("error");
        format.classList.add("success");
        
    }

    //testing if the emtered email is real email
    function trueEmail(email){
        return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
    }
















}
