# ***Impresora 3D Ender S1 PRO***

<p align="center">
  <img src="../imgs/Ender 3.jpg" width="300" /><br>
  <b>Constituyen el motor principal de la impresión 3D</b>
</p>

La **Ender 3 S1 Pro** es como tener un “asistente personal” para tus primeras creaciones en 3D.
Está pensada para que cualquier principiante pueda empezar a imprimir sin complicaciones: viene casi lista para usar, con un montaje sencillo y funciones modernas que normalmente solo se ven en impresoras más avanzadas.

Su sistema de nivelación automática se encarga del ajuste por ti, la cama caliente permite imprimir muchos tipos de materiales, y su pantalla táctil a color hace que todo sea tan fácil como usar un celular. Además, su extrusor de metal asegura acabados limpios y detallados.

## **Materiales que puede usar**

Las impresoras 3D trabajan con “hilos de plástico” llamados **filamentos**. Imagina un carrete de estambre, pero en vez de hilo es un cable de plástico que la máquina derrite y va colocando capa por capa.

La Ender 3 S1 Pro es muy versátil y soporta varios tipos de filamento:

* PLA **(Polylactic Acid)**: El más usado por principiantes. Es fácil de imprimir, barato, y viene en muchos colores. Ideal para juguetes, figuras, soportes y prototipos.

* ABS **(Acrilonitrilo Butadieno Estireno)**: Más resistente y duradero que el PLA. Se usa para piezas que necesitan aguantar golpes, pero huele un poco fuerte al imprimirse.

* PETG **(Tereftalato de Polietileno Glicol)**: Un punto medio: fuerte como el ABS pero fácil de usar como el PLA. Se usa mucho en piezas que necesitan ser resistentes y flexibles (ej. soportes, piezas para casa).


* TPU **(poliuretano termoplástico)**: Es flexible, como una goma. Sirve para imprimir llaveros elásticos, fundas, juguetes blandos, etc.

## **Software que utiliza** 
La impresora por sí sola no entiende qué quieres imprimir. Necesita que le mandes las instrucciones.

El que se utiliza es: **Ultimaker Cura**: Gratuito, fácil de usar y compatible con la Ender 3 S1 Pro.

Este software convierte el modelo 3D (un archivo .STL o .OBJ) en un conjunto de instrucciones (archivo .gcode) que la impresora entiende.
  
### **Cómo instalar el software**

* 1.- Ve a la página oficial de **Ultimaker Cura**: https://ultimaker.com/software/ultimaker-cura/

* 2.- Descarga la versión que corresponda a tu sistema operativo (Windows, Mac o Linux)

* 3.- Instala el programa como cualquier otro software (siguiente → siguiente → finalizar) 

* 4.- La primera vez que abras Cura te pedirá que elijas tu impresora.
    * Busca en la lista “Creality Ender 3 S1 Pro” (si no aparece, puedes seleccionar la “Ender 3 S1” y luego ajustar manualmente los parámetros, pero en versiones recientes ya viene incluida).

* 5.- Ya puedes abrir un modelo 3D}

## **Reglas de diseño**

| Regla | Descriçión | Imagen       |
|-----------:|:-----:|-------------|
| Sobresaliente|Los salientes se refieren a partes del modelo que <br> se extienden sobre un área sin material debajo de ellos.  | <img src="../imgs/Ender 3.jpg" width="150" /><br>          |
| Ángulo de impresión      | El ángulo en el que se puede imprimir una característica sin soporte.<br> Los ángulos de hasta 45 grados suelen ser manejables sin soporte, pero <br> esto puede variar en función de la tecnología de material e impresión.     |    <img src="../imgs/Ender 3.jpg" width="150" /><br>  |
|Bridging |Se refiere a abarcar un hueco entre dos partes <br> de una impresión sin soporte debajo.| imagen |
|Grosor de pared|Las paredes delgadas pueden no imprimirse bien, mientras <br> que las paredes muy gruesas pueden perder material y tiempo. |imagen|
|Dimensiones|Las dimensiones exactas son cruciales. La impresión 3D puede <br> introducir varianzas debido a problemas de contracción <br> de materiales o calibración de la impresora. |imagen|
|Anisotropía|Los objetos impresos pueden tener diferentes resistencias en <br> diferentes direcciones debido a la construcción capa por capa.||
|Surface Finish |El acabado de superficie está influenciado por la resolución <br> de la impresora, el material y las técnicas de post-procesamiento <br> como lijado o suavización química. ||
|Limpieza|La limpieza implica el espacio entre las estructuras de soporte <br> y la parte real que se está imprimiendo. El aclaramiento adecuado <br> garantiza que los soportes puedan eliminarse fácilmente sin dañar la <br> impresión, normalmente alrededor de 0,2 mm a 0,5 mm dependiendo <br> del material y la resolución de impresión. ||
|Infill|El interior de una impresión 3D se llama infill, y se puede ajustar en <br> términos de densidad 0% es hueco, mientras que el 100% es sólido.||

## **Cómo utilizar la impresora**
