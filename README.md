# Diggin' Philly

The Diggin’ Philly project is a large and ambitious project to document black Philadelphia particularly against a backdrop of rapid urban change including massive gentrification. To accomplish this we have developed a Django based CMS that serves as a home to the project and provide access to a variety of content, including an interactive map.

## Getting Started

TODO: These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. Python
2. Django
3. Install spatial libraries needed for GeoDjango ([detailed instructions can be found here](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/install/geolibs/)).
    * Debian/Ubuntu only: `apt-get install binutils libproj-dev gdal-bin`
    * GEOS
    * PROJ.4
    * GDAL
4. PostGres & PostGIS `apt-get install postgresql postgresql-contrib postgis libpq-dev`
5. Psycopg module: `pip install psycopg2`

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

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

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
