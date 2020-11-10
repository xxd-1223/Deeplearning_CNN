function F_Open_dialog()
{
	document.getElementById("btn_file").click();

}
function check(form) {
	

	// f.onchange
	if (form.icon.value == ""){
		alert("请上传图片");
		return false
	}
	else {
		return true
	}
}


// function clear()
// {
//   document.getElementById("999").click();
// }