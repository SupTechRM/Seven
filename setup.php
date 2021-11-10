<?php

$name = $_POST['Name'];
$dateCreated = date("F j, Y");

$userInfo = new stdClass();
$userInfo->name = $name;
$userInfo->dateAccountCreated = $dateCreated;

$myJSON = json_encode($userInfo);
$filename = "user.json";

$fileCreate = fopen($filename, "x+");
if (!$fileCreate) {
    die('Error creating the file ' . $filename);
}
else{
    file_put_contents($filename, $myJSON);
}

?>