
const removeBtns = document.querySelectorAll('.remove-from-wishlist');
const confirmRemoveBtn = document.getElementById('confirm-remove-btn');
removeBtns.forEach(btn => {
  btn.addEventListener('click', function (e) {
    e.preventDefault();
    const bookId = this.dataset.bookId;
    const removeUrl = this.href;

    // Set the confirmation URL for the "Remove" button
    confirmRemoveBtn.href = removeUrl;

    // Show the modal
    const removeModal = new bootstrap.Modal(document.getElementById('removeModal'));
    removeModal.show();
  });
});