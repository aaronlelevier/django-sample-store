# Django Sample Store

This is a demo project that shows how to use the [Django Admin](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/) to mange a store and how some other libraries like [django-rest-framework](https://www.django-rest-framework.org/) could be connected.

## Local Setup

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

## Testing

```
py.test
```

## License

MIT
