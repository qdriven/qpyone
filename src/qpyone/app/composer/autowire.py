import typing
from inspect import Parameter, Signature, isclass, signature
from types import FunctionType

from fastapi import Depends


class Autowirer:
    def __init__(self, registry_factory: typing.Callable = dict):
        self._registry = registry_factory()

    def register(self, callable_, key=None):
        return self._register(
            key or self._get_default_registry_key(callable_), callable_
        )

    def _register(self, key, callable_):
        self._registry[key] = callable_
        return callable_

    def _get_default_registry_key(self, callable_):
        if isclass(callable_):
            return callable_
        elif isinstance(callable_, FunctionType) or callable(callable_):
            return signature(callable_).return_annotation
        else:
            raise NotImplementedError

    def autowire(self, callable_):
        if isclass(callable_):
            new_callable = self._aw_cls(callable_)
        elif isinstance(callable_, FunctionType) or callable(callable_):
            new_callable = self._aw_callable(callable_)
        else:
            raise NotImplementedError

        self.register(new_callable, self._get_default_registry_key(callable_))

        return new_callable

    def _aw_callable(self, callable_):
        cbl_signature = signature(callable_)
        new_parameters = []
        for order, (name, param) in enumerate(cbl_signature.parameters.items()):
            resolved_ = self._resolve_annotation_to_callable(param.annotation)
            new_default = Depends(resolved_) if resolved_ else param.default
            new_parameters.append(
                Parameter(
                    param.name,
                    kind=param.kind,
                    default=new_default,
                    annotation=param.annotation,
                )
            )

        fn = FunctionType(
            callable_.__code__,
            callable_.__globals__,
            callable_.__name__,
            callable_.__defaults__,
            callable_.__closure__,
        )
        fn.__dict__.update(callable_.__dict__)
        fn.__signature__ = Signature(
            new_parameters, return_annotation=cbl_signature.return_annotation
        )
        return fn

    def _aw_cls(self, cls):
        init = cls.__init__
        init_signature = signature(init)
        new_parameters = []
        for order, (name, param) in enumerate(init_signature.parameters.items()):
            new_default = param.default
            if order > 0:
                resolved_ = self._resolve_annotation_to_callable(param.annotation)
                if resolved_:
                    new_default = Depends(resolved_)

            new_parameters.append(
                Parameter(
                    param.name,
                    kind=param.kind,
                    default=new_default,
                    annotation=param.annotation,
                )
            )
        init.__signature__ = Signature(
            new_parameters, return_annotation=init_signature.return_annotation
        )

        wrapped = type(cls.__name__, (cls,), {"__init__": init})
        return wrapped

    def _resolve_annotation_to_callable(self, annotation):
        return self._registry.get(annotation)
