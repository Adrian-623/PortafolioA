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
  .imagen-con-degradado {
    position: relative;
    display: inline-block;
    width: 100%;
  }
  .imagen-con-degradado img {
    display: block;
    width: 100%;
    height: auto;
  }
    .imagen-con-degradado::after {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(
      circle at center,
      transparent 60%, 
      rgba(0, 0, 0, 0.8) 100%
    );
    pointer-events: none
  }
</style>
</head>
<body>

  <h1>Hollow Knight</h1>
  <p align="center">Bienvenido a mi repositorio.</p>

  <div class="imagen-con-degradado">
    <img src="../imgs/public.webp" alt="Hollow Knight">
  </div>

</body>
</html>
