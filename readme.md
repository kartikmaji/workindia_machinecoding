* pip install -r requirements.txt
* CREATE DATABASE notes_data;
* CREATE USER 'djangouser'@'%' IDENTIFIED WITH password BY 'password';
* GRANT ALL ON notes_data.* TO 'djangouser'@'%';
* FLUSH PRIVILEGES;

* Resources
** https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database