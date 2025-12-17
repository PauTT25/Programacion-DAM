<!doctype html>
<html>
	<head>
  	<link rel="stylesheet" href="css/estilo.css">
  </head>
  <body>
		<?php include "inc/conexion_bd.php"; ?>
    <nav>
    	<?php include "controladores/poblar_menu.php" ?>
    </nav>
    <main>
      <table>
      <?php
      // PRIMERO CREO LAS CABECERAS //////////////////
        $resultado = $conexion->query("
          SELECT * FROM ".$_GET['tabla']." LIMIT 1;
        ");	// SOLO QUIERO UN ELEMENTO !!!!!!!!!!!!!!!!
        while ($fila = $resultado->fetch_assoc()) {
          echo "<tr>";
          foreach($fila as $clave=>$valor){
            echo "<th>".$clave."</th>";		// En lugar de enseñarme el valor, enseñame la clave
          }
          echo "</tr>";
         }
      ?>
      <?php
      // Y LUEGO EL RESTO DE DATOS //////////////
        $resultado = $conexion->query("
          SELECT * FROM ".$_GET['tabla'].";
        ");
        while ($fila = $resultado->fetch_assoc()) {
          echo "<tr>";
          foreach($fila as $clave=>$valor){
            echo "<td>".$valor."</td>";
          }
          echo "</tr>";
         }
      ?>
      </table>
    </main>
  </body>
</html>
