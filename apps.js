// Keresd meg az összes gombot az 'cardbtn' osztály alapján
const addToCartButtons = document.querySelectorAll('.cardbtn');

// Adj hozzá egy eseménykezelőt mindegyik gombhoz
addToCartButtons.forEach(button => {
  button.addEventListener('click', function() {
    // Először keresd meg a kis kosár számláló elemet
    const cartCount = document.querySelector('.kosár small');
    
    // Ha megtaláltad a számláló elemet
    if (cartCount) {
      // Számold ki az új értéket és növeld meg 1-el
      let count = parseInt(cartCount.textContent);
      count++;
      
      // Állítsd be a számláló új értékét
      cartCount.textContent = count;
    }
  });
});
