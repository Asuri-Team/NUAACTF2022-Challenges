<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>Welcome to NUAACTF</title>
        <link rel= stylesheet" rev="stylesheet" href="./css/style.css" type="text/css">
	</head>

    <body>
		<h2>I know you are really sese!</h2>
        <div>
			<img src="./setu.jfif"  alt="Setu" />
        </div>
        <br />
        <div class ="centered-wrapper">
        <div class="centered-content">
		<?php
    		error_reporting(0);
    			if ( isset( $_GET['file'] ) ) {
                    $str = str_replace("../","",$_GET['file']); 
                    
                    if (strpos($str,'php://filter/convert.base64-encode/resource') !== false) {
                        include ( $_GET['file'] . '.php');
                    }
                    else {
						include( "/var/www/html/" . $str . '.php' );
                    }
    			}
                else {
                    header("Location: setu.php?file=setu");
                }
    		?>
        
      </div>
      </div>
	</body>

</html>