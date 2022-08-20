<!DOCTYPE>
<html>
	<head>	
		<title></title>
	</head>
	<body>
		<h1>Comentarios</h1>

		<form method = "GET">
			<input type = "textarea" name = "texto">
			<input type = "submit" value = "Subir Comentario" name = "boton_submit">
		</form>

		<?php
			$text_area = $_GET['texto'];
			$myfile = fopen("comentarios.html", "r");
			echo fread($myfile, filesize("comentarios.html"));
			fclose($myfile);
			if(isset($_GET['boton_submit']))
			{
				$myfile = fopen("comentarios.html", "a");
				$txt = "Comentario:".$text_area."</br>";
				fwrite($myfile, $txt);
				fclose($myfile);

				echo "Comentario Subido!";
			}

		?>
	</body>
</html>
