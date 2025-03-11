# Custom HTTP Exceptions for FastAPI

## Project Description
This library provides a set of custom HTTP exceptions for FastAPI applications, inspired by Starlette's built-in exceptions. With these custom exceptions, you can simplify error handling by using pre-configured, standard HTTP exception classes tailored to common HTTP status codes.

## Installation
To get started, simply install the package via pip:

```bash
pip install fastapi-http-exceptions
```

## Usage
Instead of duplicating exception handling code throughout your Starlette application, you can use the pre-defined exceptions from this library. 
Raise these exceptions directly without worrying about writing boilerplate code for every status code.

### Example 1: Raising Unauthorized Exception
Instead of manually creating HTTP exceptions like this:

```python
from fastapi import HTTPException, status

# Some application logic...
raise HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Authentication credentials were not provided"
)
```

You can import and use a pre-configured exception like this:

```python
from fastapi_http_exceptions import UnauthorizedException

# Some application logic...
raise UnauthorizedException(
  detail="Authentication credentials were not provided",
  headers={}
)
```

## Available Exceptions

| Exception                               | Status Code                         |
| :-------------------------------------- | :---------------------------------- |
| `BadRequestException`                   | 400 Bad Request                     |
| `UnauthorizedException`                 | 401 Unauthorized                    |
| `ForbiddenException`                    | 403 Forbidden                       |
| `NotFoundException`                     | 404 Not Found                       |
| `MethodNotAllowedException`             | 405 Method Not Allowed              |
| `NotAcceptableException`                | 406 Not Acceptable                  |
| `ProxyAuthenticationRequiredException`  | 407 Proxy Authentication Required   |
| `RequestTimeoutException`               | 408 Request Timeout                 |
| `ConflictException`                     | 409 Conflict                        |
| `GoneException`                         | 410 Gone                            |
| `LengthRequiredException`               | 411 Length Required                 |
| `PreconditionFailedException`           | 412 Precondition Failed             |
| `RequestEntityTooLargeException`        | 413 Request Entity Too Large        |
| `RequestUriTooLongException`            | 414 Request URI Too Long            |
| `UnsupportedMediaTypeException`         | 415 Unsupported Media Type          |
| `RequestedRangeNotSatisfiableException` | 416 Requested Range Not Satisfiable |
| `ExpectationFailedException`            | 417 Expectation Failed              |
| `ImATeapotException`                    | 418 I'm a Teapot                    |
| `MisdirectedRequestException`           | 421 Misdirected Request             |
| `UnprocessableEntityException`          | 422 Unprocessable Entity            |
| `LockedException`                       | 423 Locked                          |
| `FailedDependencyException`             | 424 Failed Dependency               |
| `UpgradeRequiredException`              | 426 Upgrade Required                |
| `PreconditionRequiredException`         | 428 Precondition Required           |
| `TooManyRequestsException`              | 429 Too Many Requests               |
| `RequestHeaderFieldsTooLargeException`  | 431 Request Header Fields Too Large |
| `UnavailableForLegalReasonsException`   | 451 Unavailable For Legal Reasons   |


