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
			<h3>Hurricane florence</h3>
			<img src="/static/florence_1.gif">
			<br>
			<br>
		</section>
		<section class="col1_2">
			<h3>Helstu fréttir</h3>
			<ul>
		    % cnt = 0
			% for i in frettir:
				<li><a href="/frett/{{ cnt }}">{{ i[0] }}</a></li>
				% cnt += 1
			%end

			</ul>
		</section>		
	</div>
	<div class="fotur group">
		<link rel="stylesheet" href="/static/main.css">
		% include('fotur.tpl')
	</div>
	
</body>
</html>
