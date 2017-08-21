#!/usr/bin/env bash
# Bash script to set up a web server for the deployment of web_static

# Install Nginx if not installed
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start
# Create the folder /data/web_static/releases/test/ if it doesn't already exist
mkdir -p /data/web_static/releases/test/
# Create the folder /data/web_static/shared/ if it doesn't already exist
mkdir -p /data/web_static/shared/
# Create HTML file /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
# If the link exists, delete and remake
if [ -h '/data/web_static/current' ]
then
    rm /data/web_static/current
    ln -s /data/web_static/releases/test/ /data/web_static/current
else
    ln -s /data/web_static/releases/test/ /data/web_static/current
fi
# Give ownership of the /data/ folder to the ubuntu user AND group, recursively
chown -R ubuntu: /data/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
TO_FIND="^server {$"
TO_ADD="server {\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}\n"
sudo sed -i "s/$TO_FIND/$TO_ADD/" /etc/nginx/sites-available/default
sudo service nginx reload
