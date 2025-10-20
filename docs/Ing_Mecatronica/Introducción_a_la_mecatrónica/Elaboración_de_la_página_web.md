<div style="background-color:#0d1117; color:white; padding:20px; border-radius:10px;">

<!-- Encabezado principal -->
<h1 align="center" style="font-weight: 900; letter-spacing: 2px; font-family:Consolas;">
  <span style="color:#FF073A;"> <b>Elaboración de la página web</b> </span> 
  </h1>
<p align="center">
  <i>Introducción a la Mecatrónica</i>
</p>
</div>

Se nos indicó que usaríamos Github para crear un repositorio en el cual podamos documentar nuestras actividades a lo largo del semestre

Pasos a seguir:

1. Mover la plantilla para la página web a un nuevo repositorio de github. 
2. Configurarl: 
    - Escribir el nombre oficial de la página
    - Establecer la visibilidad como "Pública"  
3. Clic en "Crear repositorio". 
4. Como se copio ya un repositorio, no se puede volver a copiar 
5. Para modificar la página se ingresa a la parte del código, luego se da clic con la tecla de "." y abre el editor de Visual Studio local
6. Después nos dirigimos a la parte de "Control de código fuente", nombramos el cambio del código y se actualiza la página

## Si se gusta editar: 

- Si queremos editar el menú de Home necesitamos editar el menú de Home, se debe editar el archivo de "index.md"

> Para que toda la página funcione siempre debe existir el archivo de "index.md"

- Para varios comandos que se utilizaron en la página se consiguieron el archivo de "comandos.md", el cual viene por defecto 

- Para cambiar el tipo de fuentes, el color, grosor se utilizaba el comando de "style"

> Para tipo de fuente es: "font-family", para color: "color", el tamaño: "font-size",  

- Para los recuadros donde se pone texto se utilizaron los comandes de "div", "style", "text-align", "padding", "background", "border" "solid", "border-radius", "margin-bottom"

> "Div": Crea un contenedor

> "Style": Aplica estilos al div

> "Text-align": Centra el texto

> "Padding": Espacio entre el borde y el texto

> "Bakcground: El color del fondo

> "Border": Grosor del borde

> "Border radius": Redondea las esquinas

> "Margin bottom": Espacio debajo del contenedor

- Para el índice se utilizaron "display", "flex-wrap", "justify-content", "gap"

> "Display": Coloca los elementos en fila

> "Flex-wrap": Permite que los elementos bajen a otra línea si no caben

> "Justify-content": Centra todas las tarjetas horizontalmente

> "Gap": Espacio entre tarjetas

- Para generar color en las palabras del índice cuando se pone el curso encima se usó "const links = document.querySelectorAll", "links.forEach(link =>{}", "link.addEventListener('mouseover', ...)", "link.style.color", "link.addEventListener", "</ script>"

> "Const links: document.querySelectorAll": Selecciona todos los enlaces de la página

> "links.forEach(link => {}": Recorre cada enlace encontrado

> "link.addEventListener('mouseover', ...)": Detecta cuando el mouse pasa encima del enlace

> "link.style.color": Cambia el color del texto el mouse está encima

> "link.addEventListener('mouseout', ...)": Cambia el color de nuevo
