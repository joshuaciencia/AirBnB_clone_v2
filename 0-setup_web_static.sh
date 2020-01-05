#!/usr/bin/env bash
#  sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo " <!DOCTYPE html>
	<html>
	<head>
	<title>Nginx correctly installed</title>
	</head>
	<body>

	<h1>Nginx</h1>
	<p>installed</p>

	</body>
	</html> " | sudo tee -a /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -ie "60i location /hbnb_static {\nalias \/data\/web_static\/current\/;\nautoindex off;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
