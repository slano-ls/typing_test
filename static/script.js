document.addEventListener('DOMContentLoaded', function () {
    let quoteText = document.getElementById('quote-text');
    let typedText = '';

    quoteText.addEventListener('input', function (event) {
        typedText = event.target.innerText;
    });

    document.querySelector('form').addEventListener('submit', function (event) {
        event.preventDefault();
        // Perform typing speed and accuracy calculations
        // Send results to the server (optional)
    });
});

