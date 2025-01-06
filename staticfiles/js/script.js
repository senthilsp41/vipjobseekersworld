
    // Logout Button Click Event
    const logoutButton = document.getElementById('logoutButton');
    if (logoutButton) {
        logoutButton.addEventListener('click', function (event) {
            const confirmLogout = confirm('Are you sure you want to log out?');
            if (!confirmLogout) {
                event.preventDefault(); // Prevents the default behavior (redirect) if Cancel is clicked
            } else {
                alert('You have been logged out successfully.');
                window.location.href = "{% url 'jobs:logout' %}";  // Redirect to logout
            }
        });
    }


    function showCustomPopup(event) {
        event.preventDefault();  // Prevent form from submitting immediately
        document.getElementById('customPopup').style.display = 'block'; // Show the custom popup

        // Submit the form after a short delay
        setTimeout(() => {
            event.target.submit();
        }, 1000);  // Adjust delay as needed
    }

    function closePopup() {
        document.getElementById('customPopup').style.display = 'none';
    }
    
