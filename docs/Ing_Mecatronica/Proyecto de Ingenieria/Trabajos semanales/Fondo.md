<!DOCTYPE html>
<html>
<head>
<style>
  body {
    background-color: #000000ff; /* fondo oscuro */
    color: #f2f2f2;
    font-family: 'Georgia', serif;
    margin: 0;
    padding: 0;
  }
  h1 {
    font-family: Georgia, serif;
    color: #EDEDED;
    text-align: center;
  }
  p {
    text-align: center;
  }
  .imagen-con-degradado {
    position: relative;
    width: 100%;
    display: inline-block;
  }
  .imagen-con-degradado img {
    display: block;
    width: 100%;
    height: auto;
  }
  /* Degradado solo en los lados izquierdo y derecho */
  .imagen-con-degradado::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, rgba(0,0,0,0.8) 0%, transparent 10%, transparent 90%, rgba(0,0,0,0.8) 100%);
    pointer-events: none;
  }
</style>
</head>
<body>

  <h1 align="center" style="font-family:Georgia; color:#EDEDED;"> Semana 5</h1>

  <p>Proyecto de ingeniería</p>

  <div class="imagen-con-degradado">
    <img src="../imgs copy/public.webp" alt="Hollow Knight">
  </div>

</body>
</html>

Hacer un boceto con una pieza que no pueda ser fabricada por medios extractivos, modelar la pieza en Solidworks e imprimir la pieza para la siguiente semana

Decidí hacer al personaje del "caballero" del videojuego "Hollow Knight", pero para que pudiera aplicar a los requisitos de ser fabricado por medios extractivos, a las extremidades les otorgué articulaciones para que tuvieran movilidad 

1.- El primer paso que realicé para hacer el modelado de mi figura fue buscar una imagen del personaje y la puse a escala en Solidworks 