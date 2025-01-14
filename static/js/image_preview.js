/* jshint esversion: 6 */

document.addEventListener("DOMContentLoaded", () => {
    const newImageInput = document.getElementById("id_cover_image");
    if (newImageInput) {
        newImageInput.addEventListener("change", () => {
            const file = newImageInput.files[0];
            if (file) {
                const fileName = document.getElementById("filename");
                if (fileName) {
                    fileName.textContent = `Image will be set to: ${file.name}`;
                }
            }
        });
    }
});
