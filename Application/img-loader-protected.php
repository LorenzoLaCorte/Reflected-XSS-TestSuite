<?php

$target = $_GET['target'];
// WARNING
// If you have PHP 8.1+, this is the same as img-loader-protected2.php
$target = htmlspecialchars($target);
echo "<img src='$target'/>";

