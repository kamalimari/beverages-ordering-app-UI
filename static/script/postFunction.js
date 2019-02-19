function postUserNameAndPassword(){
    var request = new XMLHttpRequest();
	request.open('POST', 'http://localhost:5000/post-user', true);
	request.onload = function () {
		var data = this.response;
		console.log("data", data);
	};
	var formData = new FormData();
	formData.append("nam", document.getElementById("nam").value);
	formData.append("employee_id", document.getElementById("employee_id").value);
	request.send(formData);
}
