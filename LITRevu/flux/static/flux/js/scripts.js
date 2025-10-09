document.addEventListener('DOMContentLoaded', function() {
    const image_input = document.getElementById('id_image');
    image_input.style.display = 'none';
    const custom_image_button = document.getElementById('custom_image_button');
    const fileName = document.getElementById('fileName');
    const image = document.getElementById("ticket_image");
    if (!image.hasAttribute('src') || image.getAttribute('src') === "") {
    image.style.display = 'none';
    }
    custom_image_button.addEventListener("click", () => {
        image_input.click();
    })
    image_input.addEventListener("change", () => {
        if (image_input.files.length > 0) {
            fileName.textContent = 'Fichier séléctionné : ' + image_input.files[0].name;
            const file = image_input.files[0]
            if (file) {
                fileName.textContent = 'Fichier sélectionné : ' + file.name;
                image.src = URL.createObjectURL(file);
                image.style.display = 'block'
            }
        }
    })
})