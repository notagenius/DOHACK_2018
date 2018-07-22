<head>
<meta http-equiv="refresh" content="6">
</head>

<?php

echo "<h1>WIFI NODES WORKING In Real Time</h1>";


include 'db.php';


$query = "SELECT * FROM PEOPLE_COUNT";
$result = mysqli_query($mysqli, $query);

echo "<table>";

echo "current number of devices is";


while($row = mysqli_fetch_array($result, MYSQLI_ASSOC))
{
  $count_current = $row[COUNT];
}

echo " </tr><td><h1>" . $count_current . "</h1></td><tr>";

echo "</table>";

if($count_current < 30) echo "<h1>ー( ´ ▽ ` )ﾉ </h1>";

elseif($count_current >  70) echo "<h1>ଲ(⁃̗̀❍⃓ˑ̫❍⃓⁃̠́)ଲ</h1>";

else echo "<h1>(￣_￣ )</h1>";

mysql_close();


?>

~                                                                                             
~                     
