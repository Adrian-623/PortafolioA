<style>
    /* Contenedor relativo para posicionar el círculo sobre la imagen */
    .contenedor-interactivo {
        position: relative;
        display: inline-block;
        max-width: 100%;
    }

    .imagen-fondo {
        display: block;
        width: 100%;
        height: auto;
    }

    /* UBICACIÓN DEL CÍRCULO: Modifica estos porcentajes para moverlo a tu gusto */
    .punto-interactivo {
        position: absolute;
        top: 53%;   /* Ajusta la altura si necesitas moverlo verticalmente */
        left: 52%;  /* Ajusta la posición horizontal */
        width: 24px;
        height: 24px;
        cursor: pointer;
        z-index: 10;
    }

    /* El centro del círculo */
    .circulo-pulso {
        width: 100%;
        height: 100%;
        background-color: #ff3b30; 
        border-radius: 50%;
        position: relative;
    }

    /* El efecto de animación de pulso */
    .circulo-pulso::after {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        border-radius: 50%;
        background-color: rgba(255, 59, 48, 0.6);
        animation: pulso 1.8s infinite ease-out;
    }

    @keyframes pulso {
        0% { transform: scale(1); opacity: 1; }
        100% { transform: scale(3); opacity: 0; }
    }

    /* El cartelito informativo (Tooltip) */
    .cartelito {
        position: absolute;
        bottom: 32px;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(0, 0, 0, 0.85);
        color: #fff;
        padding: 6px 12px;
        border-radius: 4px;
        font-size: 13px;
        white-space: nowrap;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.3s ease, visibility 0.3s ease;
        font-family: sans-serif;
    }

    /* Muestra el cartelito al pasar el mouse */
    .punto-interactivo:hover .cartelito {
        opacity: 1;
        visibility: visible;
    }

    /* VENTANA FLOTANTE DEL VIDEO (Modal) */
    .modal {
        display: none; 
        position: fixed;
        z-index: 100;
        left: 0; top: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.8);
        justify-content: center;
        align-items: center;
    }

    .contenido-modal {
        position: relative;
        background-color: #000;
        padding: 5px;
        border-radius: 8px;
        width: 90%;
        max-width: 750px;
    }

    /* Botón de cerrar (X) */
    .cerrar-modal {
        position: absolute;
        top: -40px; right: 0;
        color: #fff;
        font-size: 35px;
        cursor: pointer;
        font-weight: bold;
    }
</style>

<div class="contenedor-interactivo">
    <img src="imgs/Mapa_Ibero.png" alt="Mapa interactivo" class="imagen-fondo">

    <div class="punto-interactivo" id="puntoVideo">
        <div class="circulo-pulso"></div>
        <span class="cartelito">Oficina Mecatrónica</span>
    </div>
</div>

<div id="modalVideo" class="modal">
    <div class="contenido-modal">
        <span class="cerrar-modal">&times;</span>
        <video id="reproductor" controls width="100%">
            <source src="vds/Oficina_Oliver1.mp4" type="video/mp4">
            Tu navegador no soporta la reproducción de videos.
        </video>
    </div>
</div>

<script>
    // Asegura que el script se ejecute correctamente en el entorno de MkDocs
    document.addEventListener("DOMContentLoaded", function() {
        const puntoVideo = document.getElementById('puntoVideo');
        const modalVideo = document.getElementById('modalVideo');
        const cerrarModal = document.querySelector('.cerrar-modal');
        const reproductor = document.getElementById('reproductor');

        if (puntoVideo && modalVideo && cerrarModal && reproductor) {
            // Abre el modal y reproduce el video al dar clic en el círculo
            puntoVideo.addEventListener('click', (e) => {
                e.preventDefault();
                modalVideo.style.display = 'flex';
                reproductor.play();
            });

            // Cierra el modal al dar clic en la (X)
            cerrarModal.addEventListener('click', () => {
                modalVideo.style.display = 'none';
                reproductor.pause();
                reproductor.currentTime = 0; 
            });

            // Cierra el modal si dan clic en el fondo negro exterior
            window.addEventListener('click', (e) => {
                if (e.target === modalVideo) {
                    modalVideo.style.display = 'none';
                    reproductor.pause();
                    reproductor.currentTime = 0;
                }
            });
        }
    });
</script>