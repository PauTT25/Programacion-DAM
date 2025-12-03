<?php
	// Comprobación de existencia isset
	if(isset($_POST['nombre'])){
		echo $_POST['nombre'];
  }
?>

<form action="?" method="POST">
  <p>Introduce tu nombre</p>
  <input type="text" name="nombre">
  <input type="submit">
</form>

EL $_Post nos sirve para recoger datos que le digamos
echo nos sirve para mostrar los datos que le hemos dicho
