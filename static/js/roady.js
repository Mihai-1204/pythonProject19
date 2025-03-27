document.getElementById('priceForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);

    fetch('/calculate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.price) {
            document.getElementById('price').textContent = `Estimated price per person: ${data.price} RON`;
        } else {
            document.getElementById('price').textContent = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        document.getElementById('price').textContent = `Error communicating with the server: ${error}`;
    });
});