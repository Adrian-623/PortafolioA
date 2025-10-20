<div style="background-color:#0d1117; color:white; padding:20px; border-radius:10px;">

<!-- Encabezado principal -->
<h1 align="center" style="font-weight: 900; letter-spacing: 2px; font-family:Consolas;">
  <span style="color:#FF073A;"> <b>Actividad 6:</b> </span> 
  <span style="color:#228B22;"> <b>Movilidad de servomotor</b> </span>
</h1>
<p align="center">
  <i>Introducción a la Mecatrónica</i>
</p>
</div>
---

## <span style="color:#0033A0;">**Materiales**</span>

    -Microcontrolador ESP32
    -Cable USB para conexión y carga del código
    -Servomotor


## <span style="color:#0033A0;">**Puente H**</span>

Un **servomotor** es un motor eléctrico que permite controlar con precisión la posición en base a angulos. Cuenta con un sistema de realimentación (sensor) que ajusta su movimiento según la señal de control.

## <span style="color:#0033A0;">**Diagrama Servomotor**</span>
<p align="center">
  <img src="../imgs/Servo.png" width="100%" /><br>
  </p> 

## <span style="color:#0033A0;">**Actividad**</span>

Al iniciar la actividad se escribió el código correspondiente a lo que queríamos que hiciera, el cual es el siguiente:

``` codigo

#define pwm 12 

int duty = 0;
int grados = 0;

void setup() {
  Serial.begin(115200);

    // Parámetros: (pin, frecuencia, resolución, canal)
  ledcAttachChannel(pwm, 50, 12, 0); // 50 Hz para servo, 12 bits, canal 0

  Serial.println("Inicio del programa: Servo de 0° a 180° en pasos de 30°");
}

void loop() {

  // Recorre de 0 a 180 en pasos de 30°
  for (grados = 0; grados <= 180; grados += 30) {
    duty = map(grados, 0, 180, 205, 410);
    ledcWrite(pwm, duty);

    Serial.print("Ángulo: ");
    Serial.print(grados);
    Serial.print("Duty: ");
    Serial.println(duty);

    delay(1000); 
  }

  }


```

La función principal del código es ir aumentando 30 grados consecutivamente hasta llegar a los 180

