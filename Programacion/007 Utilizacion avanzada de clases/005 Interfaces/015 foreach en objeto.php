<?php
	
  $cliente = [
  	"nombre" => "Pau",
    "apellidos" => "Contreras Romero",
    "email" => "correo@gmail.com"
  ];
  
  foreach($cliente as $clave=>$valor){					// Utilizando el foreach de esta forma nos mostrara en pantalla cada clave con su respectivo valor
  	echo $clave.": ".$valor."<br>";
  }
 

?>
