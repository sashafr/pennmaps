# Diggin' Philly

The Diggin’ Philly project is a large and ambitious project to document black Philadelphia particularly against a backdrop of rapid urban change including massive gentrification. To accomplish this we have developed a Django based CMS that serves as a home to the project and provide access to a variety of content, including an interactive map.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. Python: `apt-get install python3 python3-dev`
2. Django
3. Install spatial libraries needed for GeoDjango ([detailed instructions can be found here](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/install/geolibs/)).
    * Debian/Ubuntu only: `apt-get install binutils libproj-dev gdal-bin`
    * GEOS
    * PROJ.4
    * GDAL
4. PostGres & PostGIS: `apt-get install postgresql postgresql-contrib postgis libpq-dev`
5. Psycopg module: `pip install psycopg2`
6. Apache: `apt-get install apache2 apache2-dev`
    * Edit `/etc/apache2/apache2.conf`, add `ServerName server_domain_or_IP` to bottom of file
    * Run `ufw allow in "Apache Full"`
7. mod_wsgi: [follow these instructions](http://modwsgi.readthedocs.io/en/develop/user-guides/quick-installation-guide.html) - you may have to specify the python version
8. `pip install django-ckeditor`

*Note: You may have to add `/usr/local/lib` on a new line in `/etc/ld.so.conf` and then run `ldconfig` after each `make install`*

#### *Setting up Your Database*

```
$ su - postgres
$ psql
postgres=# create user [USER] password '[PASSWORD]';
postgres=# alter user [USER] with superuser;
postgres=# create database [DATABASE NAME] owner [USER];
postgres=# create extension postgis;
```

### Installing

1. Clone this repo
2. Make a copy of settings-dist.py and rename to settings.py, edit `DATABASES` and `ALLOWED_HOSTS`
3. From the command line, run the following to generate a secret key and then edit settings.py to add your `SECRET_KEY`:
```
>>> import random
>>> ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
```
4. `python3 manage.py migrate`
5. `python3 manage.py createsuperuser`
6. Test install: `python3 manage.py runserver [server IP][port number]`
7. Edit your `/etc/apache2/sites-available/000-default.conf`:
```
<VirtualHost *:80>

	ServerAdmin webmaster@localhost
	DocumentRoot /project/home
        WSGIScriptAlias / /project/home/digginphilly/wsgi.py

        <Directory /project/home>
            AllowOverride all
            Require all granted
            Options FollowSymlinks
        </Directory>

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf

        Alias /robots.txt /project/home/static/robots.txt
        Alias /favicon.ico /project/home/static/favicon.ico
        Alias /media/ /project/home/media/
        Alias /static/ /project/home/static/

        <Directory /project/home/static>
            Require all granted
        </Directory>

        <Directory /project/home/media>
            Require all granted
        </Directory>

        <Directory /project/home/digginphilly>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet

```
8. Check install `apache2ctl configtest`, if Syntax OK, then `systemctl restart apache2`
9. `chgrp -R www-data /project/home`
10. `chmod -R g+w /project/home/media`
11. Test your install by going to your IP address in a browser

## Running the tests

TODO

## Deployment

TODO

## Built With

* [Python 3.5.2](https://www.python.org/)
* [Django 2.0.6](https://www.djangoproject.com/) - web framework
* [GEOS 3.6.2](https://trac.osgeo.org/geos)
* [PROJ.4 4.9.1](https://proj4.org/)
* [GDAL 1.11.2](https://trac.osgeo.org/gdal/)
* [PostgreSQL 9.5.13](https://www.postgresql.org/)
* [PostGIS 2.2.1](https://postgis.net/)


## Contributing

TODO

## Authors

* **Sasha Renninger** - *Lead Developer* - [Github](https://github.com/sashafr)
* **Siyang You** - *Assistant Django Developer*
* **Nia Hammond** - *Web Design & Development*
* **Miranda Mote** - *Graphic Design*

## License

TODO

## Acknowledgments

* Hat tip to anyone who's code was used
