document.addEventListener('DOMContentLoaded', () => {
    const emailInput = document.getElementById('loginEmail');
    const passwordInput = document.getElementById('loginPassword');

    emailInput.addEventListener('input', () => {
        const emailError = document.getElementById('emailError');
        if (emailInput.validity.typeMismatch) {
            emailError.textContent = 'Please enter a valid email address.';
            emailError.style.display = 'block';
        } else {
            emailError.textContent = '';
            emailError.style.display = 'none';
        }
    });

    passwordInput.addEventListener('input', () => {
        const passwordError = document.getElementById('passwordError');
        if (passwordInput.value.length < 6) {
            passwordError.textContent = 'Password must be at least 6 characters.';
            passwordError.style.display = 'block';
        } else {
            passwordError.textContent = '';
            passwordError.style.display = 'none';
        }
    });
});

// Form validation before submission
function validateLoginForm() {
    const emailInput = document.getElementById('loginEmail');
    const passwordInput = document.getElementById('loginPassword');

    if (!emailInput.validity.valid) {
        alert('Please enter a valid email.');
        return false;
    }

    if (passwordInput.value.length < 6) {
        alert('Password must be at least 6 characters.');
        return false;
    }

    return true; // Allow form submission
}
