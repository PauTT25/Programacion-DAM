<?php
	
  $cliente = [
  	"nombre" => "Pau",
    "apellidos" => "Contreras Romero",
    "email" => "correo@gmail.com"
  ];
  
  foreach($cliente as $clave=>$valor){
  	echo "<label>".$clave."</label>";								// Utilizando label aparece el formulario en horizontal
  																									// Utilizando legend aparece el formulario en vertical
  	echo "<input type='text' value='".$valor."'>";
    
  }
 

?>
