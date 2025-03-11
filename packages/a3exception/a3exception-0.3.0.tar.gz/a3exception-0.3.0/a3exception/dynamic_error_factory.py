# -*- coding: utf-8 -*-
from typing import Type, Dict
from a3exception import errors
from a3py.practical.dynamic import find_all_subclasses


class DynamicErrorFactory:
    _has_build_cache = False
    _cache_errors: Dict[str, Type[errors.Error]] = dict()

    @classmethod
    def add_custom_error_cls(cls, err_cls: Type[errors.Error]):
        status = err_cls.__name__
        cls._cache_errors[status] = err_cls

    @classmethod
    def build_error_by_status(cls, status: str, **kwargs) -> errors.Error:
        if not cls._has_build_cache:
            for err_cls in find_all_subclasses(errors, errors.Error):
                cls.add_custom_error_cls(err_cls=err_cls)
            cls._has_build_cache = True

        err_cls = cls._cache_errors.get(status)
        assert err_cls is not None, (
            f"This custom error has not been added `{status}`, please use `add_custom_error_cls` to add it."
        )

        params = {"message": None, "cause": None, "detail": None}
        params.update(kwargs)
        error_instance = err_cls(**params)

        return error_instance
