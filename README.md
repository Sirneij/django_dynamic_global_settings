# dynamic_settings

![main](https://github.com/Sirneij/django_dynamic_global_settings/actions/workflows/django.yml/badge.svg?branch=main)
![issues](https://img.shields.io/github/issues/Sirneij/django_dynamic_global_settings)
![forks](https://img.shields.io/github/forks/Sirneij/django_dynamic_global_settings)
![stars](https://img.shields.io/github/stars/Sirneij/django_dynamic_global_settings)
![license](https://img.shields.io/github/license/Sirneij/django_dynamic_global_settings)

This repository accompanies [this tutorial][1] on dev.to. It has been deployed to heroku and can be accessed live via [this link][2].

## Run locally

It can be run locally by first editing `dynamic_settings/settings.py` to reflect your PostgreSQL database configuration or create a `.env` file in your root directory and put the following in:

```bash
DB_NAME=your database name
DB_USER=your database user's username
DB_PASSWORD=your database password
```

Then, create a virtual environment using any of `venv`, `poetry`, `virtualenv`, and `pipenv`. I used `virtualenv` while developing the app. Having created the virtual environment, activate it and install the project's dependencies by issuing the following command in your terminal:

```bash
pip install -r requirements.txt
```

Then, `migrate` the database:

```bash
python manage.py migrate
```

Thereafter, run the project:

```bash
python manage.py run
```

[1]: https://dev.to/sirneij/making-django-global-settings-dynamic-the-singleton-design-pattern-25en 'Making Django Global Settings Dynamic: The Singleton Design Pattern'
[2]: https://dynamic-settings.herokuapp.com/ 'Live app version'
