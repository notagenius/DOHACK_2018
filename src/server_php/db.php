<?php>
DEFINE('DBUSERNAME','xxxx');
DEFINE('DB_PASSWORD','xxxx');
DEFINE('DB_HOST','xxxx');
DEFINE('DB_DATABASE','ADESSO');

$mysqli = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

if (mysqli_connect_error()){
die('Connect Error('.mysqli_connect_error().')'.mysqli_connect_error());

}

echo '<i>DataBase Connected!  </i>';

?>

