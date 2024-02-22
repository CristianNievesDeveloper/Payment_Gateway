console.log(total);

// Variables globales
let buyingLives = 0;
let totalLives = 0;
const pricePerLife = 0.01;

// Función para actualizar el total de vidas
function updateTotal() {
    // Calcula el total de vidas compradas multiplicando el número de vidas compradas por el precio por vida
    const total = (buyingLives * pricePerLife).toFixed(2);
    // Actualiza el elemento HTML con el id 'total' con el texto formateado
    document.getElementById('total').innerText = `Total: $${total} USD`;

    // Actualiza el valor del input hidden con el nuevo valor de buyingLives
    document.getElementById('hidden-amount').value = buyingLives;
}



// Función para comprar vidas
function comprarVida() {
    // Aquí podrías implementar la lógica para enviar la cantidad de vidas al servidor (Django) para procesar la compra.
    // Por ejemplo, puedes realizar una solicitud AJAX o enviar un formulario al servidor.
    totalLives += buyingLives;
    buyingLives = 0;
    // Actualiza el elemento HTML con el id 'buying-lives' con el número de vidas compradas
    document.getElementById('buying-lives').innerText = buyingLives;
    // Actualiza el elemento HTML con el id 'lives' con el total de vidas
    document.getElementById('lives').innerText = totalLives;
    // Actualiza el total de vidas
    updateTotal();
    // Muestra un mensaje de confirmación
    alert(`Compraste ${totalLives} vidas por un total de $${(totalLives * pricePerLife).toFixed(2)} USD.`);
}

// Función para aumentar el número de vidas compradas
function aumentarVidas() {
    buyingLives += 1;
    // Actualiza el elemento HTML con el id 'buying-lives' con el número de vidas compradas
    document.getElementById('buying-lives').innerText = buyingLives;
    // Actualiza el total de vidas
    updateTotal();
}

// Función para disminuir el número de vidas compradas
function disminuirVidas() {
    if (buyingLives > 0) {
        buyingLives -= 1;
        // Actualiza el elemento HTML con el id 'buying-lives' con el número de vidas compradas
        document.getElementById('buying-lives').innerText = buyingLives;
        // Actualiza el total de vidas
        updateTotal();
    }
}


// eyes password-----------------------------------------------
function togglePasswordVisibility(passwordId) {
    var passwordInput = document.getElementById(passwordId);
    var toggleButton = document.querySelector('.toggle-password[data-password="' + passwordId + '"]');

    if (passwordInput && toggleButton) {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            toggleButton.classList.remove('fa-eye');
            toggleButton.classList.add('fa-eye-slash');
        } else {
            passwordInput.type = 'password';
            toggleButton.classList.remove('fa-eye-slash');
            toggleButton.classList.add('fa-eye');
        }
    } else {
        console.error('Element not found.');
        console.error('passwordId:', passwordId);
        console.error('passwordInput:', passwordInput);
        console.error('toggleButton:', toggleButton);
    }
}


