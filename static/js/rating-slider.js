/* jshint esversion: 6 */

document.addEventListener('DOMContentLoaded', function () {
    const slider = document.getElementById('rating-slider');
    const ratingValue = document.getElementById('rating-value');

    if (slider && ratingValue) {

        ratingValue.textContent = slider.value;

        slider.addEventListener('input', function () {
            ratingValue.textContent = slider.value;
        });
    }
});
