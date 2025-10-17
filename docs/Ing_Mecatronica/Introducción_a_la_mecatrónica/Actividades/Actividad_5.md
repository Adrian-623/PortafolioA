<div style="background-color:#0d1117; color:white; padding:20px; border-radius:10px;">

<!-- Encabezado principal -->
<h1 align="center" style="font-weight: 900; letter-spacing: 2px; font-family:Consolas;">
  <span style="color:#FF073A;"> <b>Actividad 5:</b> </span> 
  <span style="color:#228B22;"> <b>Acelerar y desacelerar motor</b> </span>
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
    -App Serial Bluetooth Terminal


## <span style="color:#0033A0;">**Señales Bluetooth**</span>

La **ESP32** recibe señales **Bluetooth** mediante su módulo integrado, que le permite **conectarse con otros dispositivos** y **recibir datos inalámbricamente**. Estos datos pueden luego **procesarse o usarse** para controlar distintos componentes electrónicos.

<p align="center">
  <img src="../imgs/Antena.png" width="100%" /><br>
  </p> 

## <span style="color:#0033A0;">**Actividad**</span>

Al iniciar la actividad se escribió el código correspondiente a lo que queríamos que hiciera, el cual es el siguiente:

``` codigo

#include "BluetoothSerial.h"
BluetoothSerial SerialBT;
 
const int LED=14;
 
void setup() {
    Serial.begin(115200);
    SerialBT.begin("Adrian");
    pinMode(LED, OUTPUT);
}
 
void loop() {
    if (SerialBT.available()) {
        String mensaje = SerialBT.readString();
        Serial.print("Recibido: " + mensaje);
        Serial.print(mensaje);
 
        if (mensaje.toInt()==1) {
          digitalWrite(LED, HIGH);
          Serial.print(mensaje + "si");
 
        } else if (mensaje.toInt()==0) {
            digitalWrite(LED, LOW);
            Serial.print(mensaje + "no");
        }
    }
   // delay(1000);
}

```

Se abrió la aplicación móvil y se mandaban los mensajes de "1" y "0" para prender y apagar la luz LED 

## <span style="color:#0033A0;">**Evidencia**</span>

<video width="100%" controls>
  <source src="../videos/Bluetooth.mp4" type="video/mp4">
  Tu navegador no soporta video.
</video>
