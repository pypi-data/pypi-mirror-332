"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from pydantic import ConfigDict, model_serializer
from pydantic import BaseModel as PydanticBaseModel
from typing import TYPE_CHECKING, Literal, Optional, TypeVar, Union, NewType
from typing_extensions import TypeAliasType, TypeAlias


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, protected_namespaces=()
    )


class Unset(BaseModel):
    @model_serializer(mode="plain")
    def serialize_model(self):
        return UNSET_SENTINEL

    def __bool__(self) -> Literal[False]:
        return False


UNSET = Unset()
UNSET_SENTINEL = "~?~unset~?~sentinel~?~"


T = TypeVar("T")
if TYPE_CHECKING:
    Nullable: TypeAlias = Union[T, None]
    OptionalNullable: TypeAlias = Union[Optional[Nullable[T]], Unset]
else:
    Nullable = TypeAliasType("Nullable", Union[T, None], type_params=(T,))
    OptionalNullable = TypeAliasType(
        "OptionalNullable", Union[Optional[Nullable[T]], Unset], type_params=(T,)
    )

UnrecognizedInt = NewType("UnrecognizedInt", int)
UnrecognizedStr = NewType("UnrecognizedStr", str)
