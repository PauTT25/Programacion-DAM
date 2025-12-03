<?php
  $cliente = [];
  $cliente['nombre'] = "Pau";
  $cliente['apellidos'] = "Contreras Romero";
  $cliente['email'] = "pau@gmail.com";
  
  $json = json_encode($cliente);
  echo $json;
?>
