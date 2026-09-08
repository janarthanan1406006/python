const cart = [];
const cartButton = document.getElementById('cartButton');
const cartDrawer = document.getElementById('cartDrawer');
const closeCart = document.getElementById('closeCart');
const overlay = document.getElementById('overlay');
const cartItems = document.getElementById('cartItems');
const cartCount = document.getElementById('cartCount');
const cartTotal = document.getElementById('cartTotal');
const toast = document.getElementById('toast');

function toggleCart(isOpen) {
  cartDrawer.classList.toggle('open', isOpen);
  overlay.classList.toggle('open', isOpen);
  cartDrawer.setAttribute('aria-hidden', String(!isOpen));
}

function renderCart() {
  cartCount.textContent = cart.length;
  cartTotal.textContent = `$${cart.reduce((total, item) => total + item.price, 0)}`;
  if (!cart.length) {
    cartItems.innerHTML = '<p class="empty-cart">Your bag is waiting.<br>Choose a piece to get started.</p>';
    return;
  }
  cartItems.innerHTML = cart.map((item, index) => `
    <div class="cart-item">
      <div><h3>${item.name}</h3><p>One / Selected online</p></div>
      <strong>$${item.price}</strong>
      <button class="remove-item" data-index="${index}" aria-label="Remove ${item.name}">×</button>
    </div>`).join('');
}

document.querySelectorAll('.product-card').forEach((card) => {
  card.querySelector('.product-image').addEventListener('click', () => {
    cart.push({ name: card.dataset.name, price: Number(card.dataset.price) });
    renderCart();
    toast.classList.add('show');
    window.setTimeout(() => toast.classList.remove('show'), 1800);
  });
});

cartItems.addEventListener('click', (event) => {
  const removeButton = event.target.closest('.remove-item');
  if (!removeButton) return;
  cart.splice(Number(removeButton.dataset.index), 1);
  renderCart();
});

cartButton.addEventListener('click', () => toggleCart(true));
closeCart.addEventListener('click', () => toggleCart(false));
overlay.addEventListener('click', () => toggleCart(false));
document.getElementById('checkoutButton').addEventListener('click', () => {
  if (cart.length) alert('Thanks for shopping with Jack Sparrow. Checkout is coming soon.');
});

renderCart();