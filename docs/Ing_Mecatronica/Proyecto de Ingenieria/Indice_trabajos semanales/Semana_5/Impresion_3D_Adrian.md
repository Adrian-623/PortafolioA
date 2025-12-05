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

  <h1 align="center" style="font-family:Georgia; color:#EDEDED;"> Semana 5: Impresion 3D</h1>

  <p>Proyecto de ingeniería</p>

  <div class="imagen-con-degradado">
    <img src="../imgs/public.webp" alt="Hollow Knight">
  </div>

</body>
</html>

Hacer un boceto con una pieza que no pueda ser fabricada por medios extractivos, modelar la pieza en Solidworks e imprimir la pieza para la siguiente semana

Decidí hacer al personaje del "caballero" del videojuego "Hollow Knight", pero para que pudiera aplicar a los requisitos de ser fabricado por medios extractivos, a las extremidades les otorgué articulaciones para que tuvieran movilidad 

- Pasos 

* 1.- El primer paso que realicé para hacer el modelado de mi figura fue buscar una imagen del personaje y la puse a escala en Solidworks 

* 2.- Una vez colocada la imagen, calqué la cabeza y la extruí, para la parte del centro fue con la opción de revolución y los cuernos fue con extrusión normal y luego se redondearon

<p align="center">
    <img src="../imgs/Cabeza.png" width="550">
</p>

Para finalizar con la cabeza en la parte posterior se extruyó el corte para poder unir la cabeza con el cuerpo, además de un hoyo en la parte inferior para poder unirlo con el cuerpo

<p align="center">
    <img src="../imgs/CabezaE.png" width="550">
</p>

* 3.- Para la parte del cuerpo se hicieron 2 círculos, uno en cada plano de manera vertical y se usó Recubrir para hacer un cono, después el redondeo, porque el cuerpo es redondo, no hay muchas partes planas

<p align="left">
    <img src="../imgs/RecubrirC.png" width="550">
</p>

<p align="right">
    <img src="../imgs/ReondeoC.png" width="550">
</p>

Después se extruyó desde la parte superior un círculo para poder introducirlo en la cabeza y en la capa

Además de que con la herramienta de Saliente por barrido se hicier las partes de "cadenas" para formar las articulaciones, se hicieron para las 2 piernas y un solo brazo

<p align="center">
    <img src="../imgs/Cuerpo.png" width="550">
</p>

* 4.- Ahora para la capa se extruyó un círculo con un agujero en el centro para ser introducido en la saliente del cuerpo

Para la parte de la forma de la capa, en un plano horizontal tracé son Spline la forma cerrandola con el círculo que se extruyó anteriormente, y esa forma la extruí con la opción de Revolución pero no por completo para dejar un espacio para el brazo

<p align="center">
    <img src="../imgs/RevCa.png" width="550">
</p>

Para el patrón de la parte inferior se creó un plano con respecto a la vista lateral y se pusieron varios circulos pegados unos a otros y se cortaron a la mitad. Ya al final solo se extruyó el corte por toda la figura

<p align="center">
    <img src="../imgs/CorteCa.png" width="550">
</p>

Y así quedó:

<p align="center">
    <img src="../imgs/Capa.png" width="550">
</p>

* 5.- Para poder hacer el brazo se hizo algo parecido que a la cabeza, primero se marcó la mitad del brazo con spline y por en medio un eje de construcción para cerrar la figura y se utilzó la opción de "Revolución"

<p align="center">
    <img src="../imgs/MitadB.png" width="550">
</p>

Para poder hacer la articulación nuevamente se hizo un croquis marcando el camino que sigue la articulación y después se usó "Saliente por barrido"

<p align="center">
    <img src="../imgs/BarrB.png" width="550">
</p>

Ya por último con un plano es extruyó un corte en forma de circulo para colocar la espada

<p align="center">
    <img src="../imgs/Brazo.png" width="550">
</p>

* 6.- Para hacer la pierna se hicieron 2 piezas principalmente:

 - Una parte que se unía con el cuerpo y tenía una ligera forma de cadena para poder añadir otra nuevamente en la parte inferior y alargar la pierna. Se utilizó nuevamente Saliente por barrido para hacer las articulaciones

<p align="center">
    <img src="../imgs/Pierna1.png" width="550">
</p> 

- Para la última parte se hizo una forma de cono porque las piernas del personaje terminan en punta y no son simplemente formas de cilindro

<p align="center">
    <img src="../imgs/Pierna2.png" width="550">
</p>

* 7.- Finalmente para la ultima pieza necesaria para armar al personaje es la espada

Para esta pieza nuevamente se utilizó la herramienta de "Recubrir", pero en este caso fuente entre la forma de un diamante y un circulo para recrear la forma de la espada.

Ya por último se extruyó un círculo por la parte de abajo para generar el mango de la espada

<p align="center">
    <img src="../imgs/Espada.png" width="550">
</p>

* 8.- Todas las piezas se ensamblaron en la misma aplicación de Solidworks y simplemente con el software de Ultimaker Cura generamos el gcode para usar la impresora 3D

<video width="100%" controls>
  <source src="../vids/Impresion.mp4" type="video/mp4">
  Tu navegador no soporta video.
</video>

Y así fue cómo quedó la impresión:

<p align="center">
    <img src="../imgs/HollowK.png" width="700">
</p>