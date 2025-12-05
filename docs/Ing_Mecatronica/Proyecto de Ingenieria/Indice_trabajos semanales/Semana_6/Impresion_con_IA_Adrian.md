<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Semana 6</title>
<style>
  body {
    margin: 0;
    padding: 0;
    background: black;
    overflow-x: hidden;
    font-family: Consolas, monospace;
  }

  /* Fondo de estrellas estilo galaxia */
  .stars {
    width: 100%;
    height: 100vh;
    background: black;
    background-image:
      radial-gradient(2px 2px at 20% 30%, white 100%, transparent),
      radial-gradient(1.5px 1.5px at 70% 80%, white 100%, transparent),
      radial-gradient(1.8px 1.8px at 40% 60%, white 100%, transparent),
      radial-gradient(1.2px 1.2px at 90% 20%, white 100%, transparent),
      radial-gradient(2px 2px at 10% 70%, white 100%, transparent),
      radial-gradient(1.3px 1.3px at 50% 10%, white 100%, transparent);
    background-repeat: repeat;
  }

  .container {
    position: absolute;
    top: 0;
    width: 100%;
    padding: 20px;
  }

  .card {
    background-color: #0d1117;
    color: white;
    padding: 20px;
    border-radius: 10px;
  }

  h1 {
    font-weight: 900;
    letter-spacing: 2px;
    text-align: center;
  }
</style>
</head>
<body>
  <div class="stars"></div>

  <div class="container">
    <div class="card">

      <h1>
        <span style="color:#FF073A;"><b>Semana 6:</b></span>
        <span style="color:#228B22;"><b> impresión con IA</b></span>
      </h1>
      <p align="center"><i>Proyecto de Ingeniería</i></p>

      <p>En esta clase se nos solicitó que con ayuda de la IA de Gemini generáramos una figura de nuestro gusto que pudiéramos imprimir en las impresoras 3D.</p>

      <p>Para el primer intento decidí crear la imagen de un dragón futurístico; se veía muy bien cómo quedaría. Pero cuando se realizó la impresión, toda la estructura estaba muy delicada y se rompió al retirar los soportes.</p>

      <p>Después se me ocurrió generar la impresión de un droide muy famoso de la saga de Star Wars, el cual es BB-8, y ya una vez que se lo solicité a Gemini, lo pude imprimir.</p>

    </div>
  </div>
</body>
</html>
