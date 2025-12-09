<?php
	
  // Original
  
	$contrasena = "contraseñasegura1234";
  echo $contrasena;
  echo "<br>";
  
  // Codificar
  
  $codificado = base64_encode($contrasena);
  echo $codificado;
  echo "<br>";
  
  
  // Descodificamos
  
  $descodificado = base64_encode($codificado);
  echo $descodificado;
  echo "<br>";
  
?>
