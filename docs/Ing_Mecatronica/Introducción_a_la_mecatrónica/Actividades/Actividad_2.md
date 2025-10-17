<div style="background-color:#0d1117; color:white; padding:20px; border-radius:10px;">

<!-- Encabezado principal -->
<h1 align="center" style="font-weight: 900; letter-spacing: 2px; font-family:Consolas;">
  <span style="color:#FF073A;"> <b>Actividad 2:</b> </span> 
  <span style="color:#228B22;"> <b>Parpadeo de LED</b> </span>
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


## <span style="color:#0033A0;">**ESP32**</span>

El **ESP32** es un microcontrolador con Wi-Fi y Bluetooth integrados, diseñado para proyectos de electrónica. Destaca por su **bajo consumo de energía**, **alta velocidad de procesamiento** y **gran variedad de pines** para conectar sensores y dispositivos.

### <span style="color:#0033A0;">**Esquema de ESP32**</span>
<p align="center">
  <img src="../imgs/ESP32.png" width="100%" /><br>
  <b>Diagrama de los pines del microcontrolador</b>
</p> 

## <span style="color:#0033A0;">**Actividad**</span>

Al iniciar la actividad se escribió el código correspondiente a lo que queríamos que hiciera, el cual es el siguiente:

``` codigo

#define led 23
void setup() {
  pinMode(LED, OUTPUT);

}

void loop() {
  digitalWrite(LED, HIGH); 
    delay(1000); 
    digitalWrite(LED, LOW); 
    delay(1000); 
}

```

> [NOTE]\
> Se comprobó que el pin seleccionado fuera un OUTPUT para que pudiera mandar la señal

Después de comprobar el funcionamiento de la ESP32 conectamos todo a la protoboard, y una vez se subió el código se pudo observar que todo funcionaba correctamente

## <span style="color:#0033A0;">**Evidencia**</span>

<video width="100%" controls>
  <source src="../videos/Parpadeo.mp4" type="video/mp4">
  Tu navegador no soporta video.
</video>
