<?php
include 'db.php';

if(!isset($_GET["token"]) || $_GET["token"] != "8888"){
echo "wrong_token";
exit();
}


$DEVICE_ID = $_GET["DEVICE_ID"];
$MAC = $_GET["MAC"];
$POWER = $_GET["POWER"];
echo $temp;

$sql = "INSERT INTO AG_Reader (DATA_ID,DEVICE_ID,MAC,POWER,TIMESTAMP) VALUES (NULL,'" . $DEVICE_ID ."','". $MAC ."','". $POWER ."', CURRENT_TIMESTAMP);";
$result = mysqli_query($mysqli, $sql);


?>

