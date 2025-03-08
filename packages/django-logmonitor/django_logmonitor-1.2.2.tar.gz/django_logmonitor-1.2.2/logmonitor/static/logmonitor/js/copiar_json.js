// static/logmonitor/js/copiar_json.js
function copiarJSON(event, id) {
    event.preventDefault(); // Evita cualquier comportamiento predeterminado (redireccionamiento)

    const jsonElement = document.getElementById(id);
    const jsonText = jsonElement.innerText;
    const button = event.currentTarget; // El botón que tiene el listener de evento

    console.log("Botón:", button); // Verifica que el botón sea el correcto
    console.log("TRANSLATIONS:", TRANSLATIONS); // Verifica que TRANSLATIONS esté definido

    // Copiar el JSON al portapapeles
    navigator.clipboard.writeText(jsonText)
        .then(() => {
            console.log("JSON copiado correctamente"); // Verifica que se copió correctamente
            // Cambiar el texto y el color del botón
            button.textContent = TRANSLATIONS.COPIADO; // Texto traducido
            button.style.backgroundColor = "#40b313"; // Color verde
            button.style.color = "#FFFFFF"; // Texto blanco

            // Restaurar el botón después de 2 segundos
            setTimeout(() => {
                button.textContent = TRANSLATIONS.COPIAR; // Texto traducido
                button.style.backgroundColor = ""; // Color original
                button.style.color = ""; // Color de texto original
            }, 2000); // 2000 milisegundos = 2 segundos
        })
        .catch(() => {
            console.log("Error al copiar el JSON"); // Verifica si hubo un error
            // Si hay un error, cambiar el texto y el color del botón
            button.textContent = TRANSLATIONS.ERROR_COPIA; // Texto traducido
            button.style.backgroundColor = "#FF0000"; // Color rojo
            button.style.color = "#FFFFFF"; // Texto blanco

            // Restaurar el botón después de 2 segundos
            setTimeout(() => {
                button.textContent = TRANSLATIONS.COPIAR; // Texto traducido
                button.style.backgroundColor = ""; // Color original
                button.style.color = ""; // Color de texto original
            }, 2000); // 2000 milisegundos = 2 segundos
        });
}