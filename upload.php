<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$FileType = pathinfo($target_file,PATHINFO_EXTENSION);
// Check if uplaod is a text file
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        echo "File is a text file - " . $check["mime"] . ".";
        $uploadOk = 1;
    } else {
        echo "File is not a text file.";
        $uploadOk = 0;
    }
}
}
// Check file size
if ($_FILES["fileToUpload"]["size"] > 2097152) {
    echo "Sorry, your file is too large.";
else {
	echo "Size of selected file:"$_FILES['image']['size'];;
}
    $uploadOk = 0;
}
// Allow certain file formats
if($FileType != "txt" && $FileType != "doc" && $FileType != "docx" && $FileType != "etf" && $FileType != "odt" ) {
    echo "Sorry, only .doc, .odt, .txt, .docx, .etf files are allowed.";
    $uploadOk = 0;
}
/*
$expensions= array("txt","doc","docx");
      
      if(in_array($file_ext,$expensions)=== false){
         $errors[]="extension not allowed, please choose a text file.";
      }
      
      if($file_size > 2097152){
         $errors[]='File size must be excately 2 MB';
      }
      
      if(empty($errors)==true){
         move_uploaded_file($file_tmp,"images/".$file_name);
         echo "Success";
      }else{
         print_r($errors);
      }
*/
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
?>