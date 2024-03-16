

document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Show "signed in successfully" message
    var messageDiv = document.getElementById("message");
    messageDiv.innerHTML = '<div class="alert alert-success" role="alert">Signed in successfully</div>';

    // Redirect to index.html after a short delay
    setTimeout(function() {
        window.location.href = "index.html";
    }, 2000); // Delay for 2 seconds before redirecting
}); 


