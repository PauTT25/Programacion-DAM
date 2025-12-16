<?php
	// Cuando utilizemos el foreach aunque añadamos nuevos elementos, siempre los va a recorrer todos
  $campos_cliente = [
  	"nombre",
    "apellidos",
    "email",
    "telefono",
    "direccion"
  ];
  
  foreach($campos_cliente as $campo){
  	echo '<input type="text" placeholder="'.$campo.'">';  // Cuando utilizemos el type text nos deja escribir texto, junto con el placeholder para poder hacer un formulario y poder escribir en el.
  }

?>
