# The goblinfish.aws.local.lpi_apis Package

> Provides a decorator that can be applied to Flask-application endpoints that convert the incoming request to a "native" endpoint into an AWS Lambda Proxy Integration data-structure, and call a local (importable) Lambda Handler with an added standard LambdaContext object as part of the request.

## Quick Start

Install in your project:

```shell
# Install with pip
pip install goblinfish-aws-local-lpi-apis
```

```shell
# Install with pipenv
pipenv install goblinfish-aws-local-lpi-apis
```

Import in your code, and create a Flask application

```python
from goblinfish.aws.local.lpi_apis import map_to_lambda_handler
from flask import Flask, request

app = Flask('my-app-name')
```

Create endpoint functions as normal, and decorate them to point at the related Lambda Handler function in your code, either by name:

```python
@app.route('/', methods=['GET'])
# Assuming that lambda_handler.home_get_handler is the Lambda Function
# handler that this route needs to call for local development purposes
@map_to_lambda_handler('lambda_handler.home_get_handler')
def get_home():
    logging.info(f'{app}.get_home called: {vars()}')
    logging.info(f'- request.json: {request.json}')
```

...or by direct import:

```python
from lambda_handler import home_get_handler

@app.route('/', methods=['GET'])
# Assuming that lambda_handler.home_get_handler is the Lambda Function
# handler that this route needs to call for local development purposes
@map_to_lambda_handler(home_get_handler)
def get_home():
    logging.info(f'{app}.get_home called: {vars()}')
    logging.info(f'- request.json: {request.json}')
```

Run the application using the local Flask server:

```python
app.run(host='0.0.0.0', port=8080)
```

More detailed examples can be found in [the `app_example` directory](https://bitbucket.org/stonefish-software-studio/goblinfish-aws-local-lpi_apis/src/main/app_example/) in the repository.

## Contribution guidelines

At this point, contributions are not accepted — I need to finish configuring the repository, deciding on whether I want to set up automated builds for pull-requests, and probably several other items. That said, if you have an idea that you want to propose as an addition, a bug that you want to call out, etc., please feel free to contact the maintainer(s) (see below).

## Who do I talk to?

The current maintainer(s) will always be listed in the `[maintainers]` section of [the `pyproject.toml` file](https://bitbucket.org/stonefish-software-studio/goblinfish-aws-local-lpi_apis/src/main/pyproject.toml) in the repository.
