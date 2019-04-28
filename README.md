# Django Sample Store

This is a demo project that shows how to use the [Django Admin](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/) to mange a store and how some other libraries like [django-rest-framework](https://www.django-rest-framework.org/) could be connected.

## Setup dependencies

```
# installs PIP globally
curl https://bootstrap.pypa.io/get-pip.py | python

# creates a virtualenv
python3 -m venv venv

# activates the virtualenv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

## Sample Data

Sample data is stored in `db.sqlite3` and will be used. This is configured in the `settings.py` using `DATABASES`

## Using the Django Admin

Here is the Admin user's info:

```
Username: admin
Password: admin
```

Start the Django local server with:

```
./manage.py runserver
```

Then go to: [http://localhost:8000/admin/](http://localhost:8000/admin/)

Enter credentials. Data will be loaded from previous step and viewable by type.

## django-rest-framework

Start the Django local server

```
./manage.py runserver
```

The API can be viewed here using DRF's browesable API: [http://localhost:8000/api/](http://localhost:8000/api/)

Or here using [coreapi](https://www.coreapi.org/): [http://localhost:8000/docs/](http://localhost:8000/docs/)

## Testing

```
./manage.py test
```

## License

MIT
