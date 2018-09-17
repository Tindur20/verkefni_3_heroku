<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="/static/main.css">
	<title>Fréttir.is</title>
</head>
<body>
	% include('haus.tpl')

	<div class="group">
		<section class="col1_2">
			<h3>{{ fyrirsogn }}</h3>
			<img src="/static/{{ mynd }}">
			<br>
			<br>
		</section>
		<section class="col1_2">
			<h3>{{ fyrirsogn }}</h3>
			<p>{{ frett }}</p>
			<h6>{{ hofundur }}</h6>
			<a href="/b">Til baka</a>
		</section>
	</div>

	<link rel="stylesheet" href="/static/main.css">
	% include('fotur.tpl')


</body>
</html>
