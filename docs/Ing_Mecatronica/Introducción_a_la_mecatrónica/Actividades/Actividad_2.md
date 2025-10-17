<div style="background-color:#0d1117; color:white; padding:20px; border-radius:10px;">

<!-- Encabezado principal -->
<h1 align="center" style="font-weight: 900; letter-spacing: 2px;">
  <span style="color:#FF073A;"> <b>Actividad 2:</b> </span> 
  <span style="color:#228B22;"> <b>Parpadeo LED</b> </span>
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


## <span style="color:#0033A0;">**Circuito integrado 555**</span>

El **temporizador 555** es un componente de electrónica que sirve para generar tiempos o señales eléctricas. Puede funcionar de tres formas:

    1.Monoestable: produce un pulso de duración fija al recibir una señal

    2. Astable: genera una señal continua como una onda cuadrada (como un parpadeo).

    3.-Biestable: actúa como un interruptor que cambia entre dos estados.

Se usa en temporizadores, luces que parpadean, alarmas y osciladores.

## <span style="color:#0033A0;">**Actividad**</span>

Para la actividad que se no encargó utilizamos la [Calculadora](https://www.digikey.com.mx/es/resources/conversion-calculators/conversion-calculator-555-timer?srsltid=AfmBOorIMn9rovHiLriNQc45qD3LhIHQ_Ve1l8VCfuCqa09MgpDren3H) para el temporizador 555

Después de hacer los cálculos necesarios ya se reunen las restsitencias, capacitores y los materiales necesarios para armar el circuito

Una vez que se arma el circuito este se conecta al osciloscopio y se observa en la pantalla la señal que se recibe, en este caso se ve una señal cuadrada, en la cual representa valores constantes de High y Low, ya que son los valores que se buscan en la actividad

> .[!NOTE].
> No es la definción exacta de una señal cuadarada, solo es la explicación para este ejercicio

Por último se comprobaron los cálculos y el LED dentro del circuito prendía y apagaba cada 4 segundos aproximadamente

## <span style="color:#0033A0;">**Evidencia**</span>

<video width="100%" controls>
  <source src="../videos/Act1osciloscopio.mp4" type="video/mp4">
  Tu navegador no soporta video.
</video>
