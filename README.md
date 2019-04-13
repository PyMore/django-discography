# Discography API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```bash
$ sudo apt-get install python3-dev python3-venv
$ python -m venv /path/to/venv
$ source /path/to/venv/bin/activate
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```bash
(venv)$ pip install -r requirements.txt
```

### Making database migrations

```bash
(venv)$ python manage.py makemigrations
```

### Applying database migrations

```bash
(venv)$ python manage.py migrate
```

### Loading initial database data

```bash
(venv)$ python manage.py loaddata fixtures/initial.json
```

### Running django development server

```bash
(venv)$ python manage.py runserver
```



## Built With

* [Django framework](https://www.djangoproject.com/)
* [REST framework](http://www.django-rest-framework.org/)

