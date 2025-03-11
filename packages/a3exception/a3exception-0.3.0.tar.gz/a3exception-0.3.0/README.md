# a3exception

English | [简体中文](README_ZH.md)

`a3exception` is a package for unifying exceptions during front-end and back-end communication.

## 1. Introduction

### errors

* Base exception: Error
* Predefined client exceptions: ValidationError, NotFoundError ...
* Predefined server exceptions: ServerKnownError, ServerUnknownError

### DynamicErrorFactory

* Generate a exception dynamically according to the dictionary: build_error_by_status
* Add a custom exception: add_custom_error_cls

## 2. Usage

### Install

```shell
pip install a3exception

```

### Examples

```python
from a3exception.dynamic_error_factory import DynamicErrorFactory
from a3exception.errors import Error


class MyError(Error):
    def __init__(self, message: str, **kwargs):
        super().__init__(message=message, **kwargs)

        
if __name__ == "__main__":
    DynamicErrorFactory.add_custom_error_cls(MyError)
    
    error_message = "custom error"
    error = DynamicErrorFactory.build_error_by_status(status=MyError.__name__, message=error_message)
    assert isinstance(error, MyError)
    assert error.message == error_message

```
