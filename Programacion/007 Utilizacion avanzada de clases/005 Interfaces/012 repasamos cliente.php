<?php
	// Cuando utilizemos el foreach aunque añadamos nuevos elementos, siempre los va a recorrer todos
  $campos_cliente = [
  	"nombre",
    "apellidos",
    "email",
    "telefono"
  ];
  
  foreach($campos_cliente as $campo){
  	echo $campo."<br>";
  }

?>
