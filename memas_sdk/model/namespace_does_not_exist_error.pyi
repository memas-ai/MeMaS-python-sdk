# coding: utf-8

"""
    MeMaS APIs

    This is the Control Plane and Data Plane APIs for MeMaS (Memory Management Service). See https://github.com/memas-ai/MeMaS for more details.  # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Contact: max.yu@memas.ai
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from memas_sdk import schemas  # noqa: F401


class NamespaceDoesNotExistError(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Error returned when the namespace object (corpus/user) does not exist
    """


    class MetaOapg:
        required = {
            "msg",
            "error_code",
        }
        
        class properties:
            
            
            class error_code(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NAMESPACE_DOES_NOT_EXIST(cls):
                    return cls("namespace_does_not_exist")
            msg = schemas.StrSchema
            details = schemas.StrSchema
            __annotations__ = {
                "error_code": error_code,
                "msg": msg,
                "details": details,
            }
    
    msg: MetaOapg.properties.msg
    error_code: MetaOapg.properties.error_code
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_code"]) -> MetaOapg.properties.error_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["msg"]) -> MetaOapg.properties.msg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["error_code", "msg", "details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_code"]) -> MetaOapg.properties.error_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["msg"]) -> MetaOapg.properties.msg: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["error_code", "msg", "details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        msg: typing.Union[MetaOapg.properties.msg, str, ],
        error_code: typing.Union[MetaOapg.properties.error_code, str, ],
        details: typing.Union[MetaOapg.properties.details, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NamespaceDoesNotExistError':
        return super().__new__(
            cls,
            *_args,
            msg=msg,
            error_code=error_code,
            details=details,
            _configuration=_configuration,
            **kwargs,
        )
