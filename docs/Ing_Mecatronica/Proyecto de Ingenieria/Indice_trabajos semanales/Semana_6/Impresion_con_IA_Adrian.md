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

  <h1 align="center" style="font-family:Georgia; color:#EDEDED;"> Semana 6: Impresion 3D con IA</h1>

  <p>Proyecto de ingeniería</p>

  <div class="imagen-con-degradado">
    <img src="../imgs/StarWars.jpg" alt="Star Wars">
  </div>

</body>
</html>

En esta clase se nos solicitó que con ayuda de la IA de Gemini generáramos una figura de nuestro gusto que pudiéramos imprimir en las impresoras 3D.</p>

Para el primer intento decidí crear la imagen de un dragón futurístico; se veía muy bien cómo quedaría. Pero cuando se realizó la impresión, toda la estructura estaba muy delicada y se rompió al retirar los soportes.

Después se me ocurrió generar la impresión de un droide muy famoso de la saga de Star Wars, el cual es BB-8, y ya una vez que se lo solicité a Gemini, lo inserté en Tripo para que lo transformara en STL y así lo pude imprimir y quedó así:

<p align="center">
    <img src="../imgs/BB8.jpg" width="600">
</p>