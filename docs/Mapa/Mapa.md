<style>
    /* Contenedor relativo para posicionar los círculos sobre la imagen */
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

    /* ESTILO GENERAL DE LOS PUNTOS */
    .punto-interactivo {
        position: absolute;
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
    <img src="../imgs/Mapa_Ibero.png" alt="Mapa interactivo" class="imagen-fondo">

    <div class="punto-interactivo" style="top: 80%; left: 45%;" onclick="abrirModalVideo('../vds/Oficina_Oliver1.mp4')">
        <div class="circulo-pulso"></div>
        <span class="cartelito">Oficina Mecatrónica</span>
    </div>

    <div class="punto-interactivo" style="top: 35%; left: 42%;" onclick="abrirModalVideo('../vds/Laboratorio_Electronica.mp4')">
        <div class="circulo-pulso"></div>
        <span class="cartelito">Bodega</span>
    </div>

    <div class="punto-interactivo" style="top: 26%; left: 31%;" onclick="abrirModalVideo('../vds/Enfermería.mp4')">
        <div class="circulo-pulso"></div>
        <span class="cartelito">Enfermería</span>
    </div>

    <div class="punto-interactivo" style="top: 20%; left: 60%;" onclick="abrirModalVideo('../vds/Centro_Computo.mp4')">
        <div class="circulo-pulso"></div>
        <span class="cartelito">Aidel</span>
    </div>

    <div class="punto-interactivo" style="top: 27%; left: 52%;" onclick="abrirModalVideo('../vds/Ciencias_Básicas.mp4')">
        <div class="circulo-pulso"></div>
        <span class="cartelito">Ciencias básicas</span>
    </div>

    <div class="punto-interactivo" style="top: 10%; left: 34%;" onclick="abrirModalVideo('../vds/Biblioteca.mp4')">
        <div class="circulo-pulso"></div>
        <span class="cartelito">Servicios escolares</span>
    </div>

    <div class="punto-interactivo" style="top: 15%; left: 30%;" onclick="abrirModalVideo('../vds/Auditorio.mp4')">
        <div class="circulo-pulso"></div>
        <span class="cartelito">Auditorio </span>
    </div>

    <div class="punto-interactivo" style="top: 20%; left: 40%;" onclick="abrirModalVideo('../vds/Canchas_Deportivas.mp4')">
        <div class="circulo-pulso"></div>
        <span class="cartelito">Oficina Marícruz</span>
    </div>

    <div class="punto-interactivo" style="top: 32%; left: 59%;" onclick="abrirModalVideo('../vds/Salon_Computo.mp4')">
        <div class="circulo-pulso"></div>
        <span class="cartelito">Oficna para instalar aplicaciones</span>
    </div>

</div>

<div id="modalVideo" class="modal" onclick="cerrarModalFondo(event)">
    <div class="contenido-modal">
        <span class="cerrar-modal" onclick="cerrarModalVideo()">&times;</span>
        <video id="reproductor" controls width="100%">
            <source id="videoSource" src="" type="video/mp4">
            Tu navegador no soporta la reproducción de videos.
        </video>
    </div>
</div>

<script>
    // Esta función recibe dinámicamente el video correspondiente al círculo presionado
    function abrirModalVideo(rutaVideo) {
        var modal = document.getElementById('modalVideo');
        var reproductor = document.getElementById('reproductor');
        
        if (modal && reproductor) {
            reproductor.src = rutaVideo; // Asigna el video correcto
            reproductor.load();         // Fuerza la recarga del elemento de video
            modal.style.display = 'flex';
            reproductor.play();
        }
    }

    function cerrarModalVideo() {
        var modal = document.getElementById('modalVideo');
        var reproductor = document.getElementById('reproductor');
        if (modal && reproductor) {
            modal.style.display = 'none';
            reproductor.pause();
            reproductor.currentTime = 0; // Reinicia el tiempo
        }
    }

    function cerrarModalFondo(event) {
        var modal = document.getElementById('modalVideo');
        if (event.target === modal) {
            cerrarModalVideo();
        }
    }
</script>