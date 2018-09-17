<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="/static/main.css">
	<title>Fréttir.is</title>
</head>
<body>
	% include('haus.tpl')

	<div>
		<section class="row">
			<h3>Hurricane florence</h3>
			<img src="/static/florence_1.gif">			
		</section>
		<section class="row">
			<h3>Helstu fréttir</h3>
			<ul>
				<li><a href="/frett/0">Hurricane florence</a></li>
				<li><a href="/frett/1">Hurricane florence orðinn að Category 2</a></li>
				<li><a href="/frett/2">Af hverju er ég veikur?1?</a></li>
			</ul>
		</section>		
	</div>
	<div class="fotur">
		<link rel="stylesheet" href="/static/main.css">
		% include('fotur.tpl')
	</div>
	
</body>
</html>
