<div style="background-color:#0d1117; color:white; padding:20px; border-radius:10px;">

<!-- Encabezado principal -->
<h1 align="center" style="font-weight: 900; letter-spacing: 2px; font-family:Consolas;">
  <span style="color:#FF073A;"> <b>Actividad 3:</b> </span> 
  <span style="color:#228B22;"> <b>Encender LED con botón</b> </span>
</h1>
<p align="center">
  <i>Introducción a la Mecatrónica</i>
</p>
</div>
---

## <span style="color:#0033A0;">**Materiales**</span>

    -Microcontrolador ESP32
    -Cable USB para conexión y carga del código
    -Protoboard
    -LED rojo
    -Resistencia de 330Ω
    -Botón


## <span style="color:#0033A0;">**Push button**</span>

El **push button** (botón pulsador) es un **interruptor** que permite **abrir o cerrar un circuito eléctrico** al ser presionado. Se utiliza para enviar señales en dispositivos electrónicos, como encender, apagar o reiniciar un sistema, y vuelve automáticamente a su posición inicial al soltarlo.

## <span style="color:#0033A0;">**Actividad**</span>

Al iniciar la actividad se escribió el código correspondiente a lo que queríamos que hiciera, el cual es el siguiente:

``` codigo

#define LED 23
#define BUTTON 33

void setup() {
    pinMode(LED, OUTPUT);
    pinMode(BUTTON, INPUT);
}

void loop() {
    if (digitalRead(BUTTON) == HIGH) {
        digitalWrite(LED, HIGH);
    } else {
        digitalWrite(LED, LOW);
    }
}

```

Se utilizó principalmente el mismo armado que el de la actividad anterior, solo se agregó un pin más y se agrego el interruptor en la protoboard 

## <span style="color:#0033A0;">**Evidencia**</span>

<video width="100%" controls>
  <source src="../videos/Boton.mp4" type="video/mp4">
  Tu navegador no soporta video.
</video>
