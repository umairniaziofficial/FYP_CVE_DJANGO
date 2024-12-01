// Function to show the sign-up modal
function openSignupPage() {
    document.getElementById('signup-modal').style.display = 'block';
}

// Function to close the sign-up modal
function closeSignupModal() {
    document.getElementById('signup-modal').style.display = 'none';
}

// Adding event listener to the "Explore the Platform" button
document.querySelector('.fade-in-box button').addEventListener('click', function() {
    // Redirecting to the sign-up page
    window.location.href = 'sign-up.html'; // Adjust the path if needed
});
