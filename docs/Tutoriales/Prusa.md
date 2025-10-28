# 🖨️ **Impresora 3D Prusa MK4S**

<p align="center">
  <img src="../imgspr/Prusa.webp" width="300" /><br>
  <b>Una impresora moderna, precisa y diseñada para aprender sin complicaciones</b>
</p>

---

## 🔷 Introducción

La **Prusa MK4S** es una de las impresoras 3D más recomendadas para principiantes y entornos educativos.  
Combina **facilidad de uso, fiabilidad y resultados profesionales** gracias a su sistema de **autonivelación automática**, su **asistente de calibración inteligente** y el software **PrusaSlicer**.

Desde el primer encendido, guía al usuario paso a paso evitando errores comunes. Su funcionamiento es **silencioso**, su mantenimiento **sencillo**, y su comunidad **muy activa**, lo que facilita resolver dudas y aprender rápidamente.

---

## Materiales compatibles

La MK4S admite una gran variedad de filamentos gracias a su **boquilla de alta temperatura (hasta 300 °C)** y su **cama calefactora magnética (hasta 120 °C)**.  
Esto permite realizar desde piezas decorativas hasta componentes técnicos o flexibles.

| Material | Descripción | Temp. boquilla / cama | Dificultad | Recomendado para |
|:---------|:-------------|:---------------------:|:-----------:|:-----------------|
| **PLA** | Ideal para principiantes, biodegradable y fácil de imprimir | 200 °C / 60 °C | Fácil | Figuras, prototipos, piezas decorativas |
| **PETG** | Resistente, flexible y duradero | 240 °C / 85 °C | Media | Piezas funcionales y exteriores |
| **ABS** | Resiste altas temperaturas, puede deformarse sin cámara cerrada | 250 °C / 100 °C | Difícil | Piezas estructurales y mecánicas |
| **ASA** | Similar al ABS, pero más estable frente a rayos UV | 255 °C / 100 °C | Difícil | Piezas exteriores |
| **TPU** | Material elástico y flexible | 230 °C / 60 °C |  Media | Protectores, juntas, fundas |
| **Nylon** | Muy resistente y duradero | 260 °C / 90 °C |  Difícil | Engranajes, bisagras, componentes técnicos |

>  **Consejo:** si estás comenzando, imprime con **PLA**. Es económico, seguro y no requiere una cabina cerrada.

---

## Componentes principales de la Prusa MK4S

| Componente | Descripción |
|-------------|--------------|
| **Extrusor Nextruder** | Extrusor de nueva generación con sensor de carga que mejora la precisión de la primera capa. |
| **Boquilla (Nozzle)** | Fundición del filamento a alta temperatura (máx. 300 °C). Fácil de reemplazar. |
| **Cama calefactora magnética** | Superficie removible con calentamiento uniforme (hasta 120 °C). Facilita la extracción de piezas. |
| **Pantalla táctil a color** | Interfaz moderna e intuitiva para gestionar impresiones, filamento y calibraciones. |
| **Sensores de calibración** | Nivelación automática y detección precisa de posición del eje Z. |
| **Fuente de poder y placa base 32 bits** | Sistema electrónico silencioso con control de vibraciones (Input Shaper). |
| **Estructura de aluminio reforzada** | Alta estabilidad y rigidez, esencial para precisión dimensional. |

 *Sugerencia:* agrega aquí una imagen anotada con los componentes principales.  
Por ejemplo:  
`<img src="../imgspr/componentes_prusa.webp" width="600">`

---

## Software de laminado: **PrusaSlicer**

El programa **PrusaSlicer** convierte los modelos 3D en instrucciones que la impresora entiende, llamadas **G-code**.

### Pasos básicos
1. Abre **PrusaSlicer**.  
2. Selecciona **Original Prusa MK4S** como impresora.  
3. Carga tu modelo 3D (`Archivo → Importar → Modelo STL`).  
4. Ajusta su posición y orientación con **Move**, **Rotate**, y **Scale**.  
5. Configura los parámetros principales:
   - Material: *PLA recomendado para iniciar*  
   - Altura de capa: *0.20 mm (estándar)*  
   - Relleno: *20 %*  
   - Soportes: *solo si hay voladizos o huecos grandes*  
6. Pulsa **Slice Now** para generar el archivo.  
7. Guarda el `.gcode` en una memoria USB.  

> **Dato técnico:** el archivo G-code contiene coordenadas (X, Y, Z), temperatura y flujo de extrusión para cada capa.

 *Opcional:* imagen de la interfaz de PrusaSlicer mostrando el modelo cargado.  
`<img src="../imgspr/prusaslicer_ui.webp" width="700">`

---

## Preparación y calibración inicial

1. Enciende la impresora y espera que cargue el menú principal.  
2. Dirígete a **Settings → Calibration → Selftest**.  
3. El sistema verificará:  
   - Movimiento de los ejes (X, Y, Z)  
   - Sensor de filamento  
   - Calibración del extrusor y de la cama calefactora  
4. Si todo está correcto, mostrará **Selftest Passed**.

> **No es necesario nivelar manualmente la cama.**  
> La MK4S usa sensores de carga y un sistema de calibración automática (Load Cell) que mide la presión real de contacto.

---

##  Cargar o cambiar el filamento

1. Menú → **Filament → Load Filament**.  
2. El extrusor calentará la boquilla automáticamente.  
3. Inserta el filamento y deja que el motor lo guíe.  
4. Espera a que salga un flujo uniforme.  
5. Para cambiar material: **Unload Filament** → luego carga el nuevo.  
6. Corta el exceso de material antes de iniciar la impresión.

> **Precaución:** nunca toques la boquilla caliente (puede superar los 250 °C).

---

##  Iniciar una impresión

1. Inserta la memoria USB con el archivo `.gcode`.  
2. Menú → **Print → USB Storage** → selecciona el modelo.  
3. La impresora precalienta la cama y la boquilla automáticamente.  
4. Observa la primera capa: debe verse uniforme y bien adherida.  
5. Si el filamento no se adhiere, ajusta con **Live Z Adjust**.  

> 💡 La MK4S incorpora *Input Shaper*, un sistema que reduce vibraciones y mejora la calidad de impresión a altas velocidades (hasta 250 mm/s).

---

##  Retirar la pieza impresa

1. Espera a que la temperatura de la cama baje a menos de 35 °C.  
2. Retira la **hoja magnética** y flexiónala suavemente.  
3. Usa una espátula con cuidado si la pieza está muy adherida.  
4. Limpia la cama con alcohol isopropílico antes de la siguiente impresión.  

---

## Mantenimiento básico

- Limpia la boquilla con aguja o cepillo de latón.  
- Lubrica varillas y husillos cada 3 meses.  
- Mantén los ventiladores libres de polvo.  
- Guarda el filamento en bolsas con desecante.  
- Actualiza el firmware desde [help.prusa3d.com](https://help.prusa3d.com/).  

 *Opcional:* imagen de limpieza y mantenimiento de boquilla.  
`<img src="../imgspr/mantenimiento_prusa.webp" width="600">`

---

## Resolución de problemas comunes

| Problema | Posible causa | Solución |
|-----------|----------------|-----------|
| Primera capa no se adhiere | Cama sucia o mal calibrada | Limpia la cama y ajusta el eje Z |
| No sale filamento | Boquilla obstruida | Calienta y limpia o reemplaza la boquilla |
| Filamento quebradizo | Humedad o mala calidad | Usa filamento seco y revisa el tubo guía |
| Capas desplazadas | Correas flojas o atascos | Ajusta correas y verifica los ejes |
| Impresión detenida | Fallo de energía o USB defectuosa | Usa otro dispositivo o la función *Resume Print* |

---

##  Recomendaciones finales

- Inicia con modelos simples como el **3DBenchy** o un **cubo de calibración**.  
- No apagues la impresora hasta que se enfríe por completo.  
- Mantén el área de trabajo limpia y bien ventilada.  
- Aprende nuevos perfiles de impresión en [Printables.com](https://www.printables.com/).  

---

###  Conclusión

La **Prusa MK4S** permite a cualquier persona iniciarse en la impresión 3D sin complicaciones.  
Su diseño inteligente, sensores avanzados y software intuitivo hacen que el aprendizaje sea fluido y confiable.  
Con práctica y curiosidad, podrás dominar las técnicas de impresión, calibración y diseño 3D desde los primeros proyectos.
