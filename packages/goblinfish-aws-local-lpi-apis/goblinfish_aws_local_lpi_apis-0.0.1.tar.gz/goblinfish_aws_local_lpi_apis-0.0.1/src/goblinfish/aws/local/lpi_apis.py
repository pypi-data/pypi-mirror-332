#!/usr/bin/env python3.11
"""
"""

from __future__ import annotations

# Built-In Imports
import http.client
import io
import json
import logging
import os

from datetime import datetime, timedelta
from functools import cache, wraps
from importlib import import_module
from typing import Any, Callable, NewType, Mapping
from uuid import uuid4
from urllib.parse import parse_qs

# Third-Party Imports
from awslambdaric.lambda_context import LambdaContext
from flask import make_response, request
from typeguard import typechecked

# Path Manipulations (avoid these!) and "Local" Imports

# Temporary imports and related

logging.basicConfig(level='INFO')

# Module "Constants" and Other Attributes
NamespacePath = NewType('NamespacePath', str)
logger = logging.getLogger('local-api')
logger.setLevel(os.getenv('API_LOG_LEVEL', 'INFO').upper())
_module_name = __file__.split(os.sep)[-1]


# Module Functions
@typechecked
def create_lambda_integration_payload(flask_request: request) -> dict:
    """
    Creates a minimum viable Lambda Proxy Integration payload dictionary
    from a Flask request object.

    Parameters:
    -----------
    flask_request : flask.request object
        The request to build the payload from

    Notes:
    ------
    Several of the fields in the Lambda Proxy Integration input structure
    (see https://docs.aws.amazon.com/apigateway/latest/developerguide/
        set-up-lambda-proxy-integrations.html
        #api-gateway-simple-proxy-for-lambda-input-format)
    are not included in this version. I could not see any particular use
    for them in a local API testing context. They include:
    - requestContext (though a formal LambdaContext objet is being
      provided)
    - stageVariables (I have no idea how to handle this yet)
    - isBase64Encoded

    In addition:
    - The resource, and path values in the payload are, for now, just
      going to contain the PATH_INFO.
    - The pathParameters parameter will be re-evaluated for inclusion
      as soon as a use case where it applies surfaces.
    """
    logger.debug(
        f'{_module_name}.create_lambda_integration_payload called '
        f'with {flask_request}'
    )
    payload = {
        # Resource and path just use the PATH_INFO, for now
        "resource": request.environ['PATH_INFO'],
        "path": request.environ['PATH_INFO'],
        "httpMethod": request.environ['REQUEST_METHOD'],
        "headers": {
            key: value for key, value in flask_request.headers.items()
        },
        "multiValueHeaders": {
            key: [item.strip() for item in value.split(',')]
            for key, value in flask_request.headers.items()
        },
        "queryStringParameters": {
            key: ','.join(value)
            for key, value
            in parse_qs(request.environ['QUERY_STRING']).items()
        },
        "multiValueQueryStringParameters":
            parse_qs(request.environ['QUERY_STRING']),
        "body": request.data.decode(),
    }
    logger.debug(f'payload: {payload}')
    logger.info(f'{_module_name}.create_lambda_integration_payload completed')
    return payload

@cache
@typechecked
def get_handler_from_namespace(namespace: str) -> Callable:
    """
    Finds and returns the source callable identified by a Python namespace.

    Parameters:
    -----------
    namespace : str
        The string namespace identifier for the target handler function.

    Raises:
    -------
    ImportError
        If the identified target callable cannot be imported.
    """
    logger.debug(
        f'{_module_name}.get_handler_from_namespace called '
        f'with {namespace}'
    )
    # Assume that all namespaces must have at least two segments:
    # package.or.module.target_callable
    *module, target = namespace.split('.')
    module = import_module('.'.join(module))
    logger.debug(f'module: {module}')
    target = getattr(module, target)
    logger.debug(f'target: {target}')
    logger.info(
        f'{_module_name}.get_handler_from_namespace({namespace}) completed'
    )
    return target


@typechecked
def map_to_lambda_handler(handler: NamespacePath | Callable) -> Callable:
    """
    Decorates a Flask endpoint function so that it will call the specified
    handler function or method with an AWS API Gateway Lambda Proxy
    Integration request payload data structure.

    Parameters:
    -----------
    handler : namespace-string | function | method
        The callable to execute with the Lambda Proxy Integration request.
        If passed a string, that string is expected to be a namespace path
        to the callable.

    Returns:
    --------
    A decorated callable.
    """
    logger.debug(
        f'{_module_name}.map_to_lambda_handler called '
        f'with {handler} ({type(handler).__name__})'
    )
    # Parameters provided to the decorator are captured here before the
    # wrapper is defined
    if isinstance(handler, str):
        handler = get_handler_from_namespace(handler)
        logger.debug(f'Resolved {handler} from string namespace')

    # Decorator to call against the target
    @typechecked
    def _decorator(target: Callable):
        """
        The decorator wrapper for the target callable.

        Parameters:
        -----------
        target : Callable
            The function or method to decorate.
        """
        logger.debug(
            f'{_module_name}.map_to_lambda_handler is decorating {target}.'
        )
        @wraps(handler)
        def _caller(*args, **kwargs):
            """
            The caller of the handler that wraps the target
            """
            logger.debug(f'Creating event and context to pass to {target}.')
            event = create_lambda_integration_payload(request)
            logger.debug(f'event: {json.dumps(event)}')
            deadline = int(
                (datetime.now() + timedelta(minutes=15)).timestamp() * 1000
            )
            context = LambdaContext(
                invoke_id=str(uuid4()),
                client_context=None,
                cognito_identity=None,
                epoch_deadline_time_in_ms=deadline,
            )
            logger.debug(f'context: {context}')
            handler_response = handler(event, context)
            logger.debug(f'handler_response: {json.dumps(handler_response)}')
            response = make_response(json.dumps(handler_response))
            response.headers['content-type'] = 'application/json'
            logger.info(
                f'{target} call decorated by {_module_name}.map_to_'
                'lambda_handler completed'
            )
            logger.debug(f'response: {response}')
            return response

        return _caller
    return _decorator


# Module Metaclasses

# Module Abstract Base Classes

# Module Concrete Classes

# Code to run if the module is executed directly
if __name__ == '__main__':
    pass
