/* global bootstrap */

document.addEventListener('DOMContentLoaded', function () {
    var deleteButton = document.getElementById("deleteButton");
    if (deleteButton) {
        deleteButton.addEventListener("click", function() {
            var bookTitle = this.getAttribute("data-book-title");
            var bookId = this.getAttribute("data-book-id");

            // Update the modal text to show the book title
            document.getElementById("bookTitle").textContent = bookTitle;

            // Update the "Yes" button's href to the correct URL with the book ID
            document.getElementById("confirmDelete").setAttribute("href", "/bookstore/delete/" + bookId + "/");

            // Show the modal
            var myModal = new bootstrap.Modal(document.getElementById('deleteModal'), {
                keyboard: false
            });
            myModal.show();
        });
    }
});