const cartItemsContainer = document.querySelector('.cart-items');
const totalPriceElement = document.getElementById('total-price');
const checkoutButton = document.getElementById('checkout-btn');

function updateCartUI(cartItems) {
    cartItemsContainer.innerHTML = '';
    let total = 0;

    cartItems.forEach(item => {
        const itemTotal = item.price * item.quantity;
        total += itemTotal;

        const itemElement = document.createElement('div');
        itemElement.classList.add('cart-item');
        itemElement.innerHTML = `
            <div class="item-name">${item.name}</div>
            <div class="item-quantity">Quantity: ${item.quantity}</div>
            <div class="item-total">$${itemTotal.toFixed(2)}</div>
        `;
        cartItemsContainer.appendChild(itemElement);
    });

    totalPriceElement.textContent = `$${total.toFixed(2)}`;
}

fetch('/api/cart')
    .then(response => response.json())
    .then(data => {
        updateCartUI(data);
    })
    .catch(error => {
        console.error('Error fetching cart data:', error);
    });

checkoutButton.addEventListener('click', () => {
    // Redirect to the checkout page or implement desired behavior
    // Example: window.location.href = 'checkout.html';
});