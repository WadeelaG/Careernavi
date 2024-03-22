function formValidation() {
    // Get form elements
    var firstName = document.getElementById("firstName");
    var lastName = document.getElementById("lastName");
    var email = document.getElementById("email");
    var phoneNumber = document.getElementById("phoneNumber");
    var password = document.getElementById("password");
    var confirmPassword = document.getElementById("confirmPassword");
    var gender = document.getElementsByName("gender");

    // Check if all fields are filled
    if (firstName.value == "" || lastName.value == "" || email.value == "" || phoneNumber.value == "" || password.value == "" || confirmPassword.value == "") {
        alert("Please fill in all fields.");
        return false;
    }

    // Check if email is valid
    var emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(email.value)) {
        alert("Please enter a valid email address.");
        return false;
    }

    // Check if phone number is valid
    var phoneNumberRegex = /^[+]?[0-9\s-]{8,15}$/;
    if (!phoneNumberRegex.test(phoneNumber.value)) {
        alert("Please enter a valid phone number.");
        return false;
    }

    // Check if passwords match
    if (password.value != confirmPassword.value) {
        alert("Passwords do not match.");
        return false;
    }

    // Check if gender is selected
    var genderSelected = false;
    for (var i = 0; i < gender.length; i++) {
        if (gender[i].checked) {
            genderSelected = true;
            break;
        }
    }
    if (!genderSelected) {
        alert("Please select a gender.");
        return false;
    }

    // If all checks pass, submit the form
    // Redirect to Home_Page.html
    window.location.href = "index.html";

     // Return false to prevent the form from being submitted
     return false;
}


