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

  <h1>Hollow Knight</h1>

  <p>Bienvenido a mi repositorio.</p>

  <div class="imagen-con-degradado">
    <img src="../imgs/public.webp" alt="Hollow Knight">
  </div>

</body>
</html>
