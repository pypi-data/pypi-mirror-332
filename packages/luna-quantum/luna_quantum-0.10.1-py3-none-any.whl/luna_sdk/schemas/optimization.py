from typing import Any, Dict, Generic, Optional, TypeVar

from pydantic import BaseModel, ConfigDict

from luna_sdk.schemas.enums.optimization import OptFormat
from luna_sdk.schemas.optimization_formats.bqm import BQMSchema
from luna_sdk.schemas.optimization_formats.cqm import CQMSchema
from luna_sdk.schemas.optimization_formats.lp import LPSchema
from luna_sdk.schemas.optimization_formats.qubo import QuboSchema
from luna_sdk.schemas.pretty_base import PrettyBase
from luna_sdk.schemas.wrappers import PydanticDatetimeWrapper


class Optimization(PrettyBase):
    """
    Pydantic model for optimization going OUT.
        Attributes
    ----------
    id: str
        Id of the optimization
    created_date: Optional[DatetimeWrapper]
        Date when optimization was created
    created_by: Optional[str]
        Id of the user who created optimization
    modified_date: Optional[DatetimeWrapper]
        Date when optimization was modified
    modified_by: Optional[str]
        Id of the user who modified optimization
    """

    id: str
    name: Optional[str] = None
    created_date: PydanticDatetimeWrapper
    created_by: str
    modified_date: Optional[PydanticDatetimeWrapper] = None
    modified_by: Optional[str] = None
    original_format: Optional[OptFormat] = None
    use_case_name: Optional[str] = None
    params: Optional[Dict[str, Any]] = None

    verbose: bool = False

    def __str__(self):
        if self.verbose:
            return self.details()
        return self.subset()

    def details(self):
        trimmed_keys = [
            "verbose",
        ]
        data = self.model_dump()
        output = ""
        data_subset = {key: data[key] for key in data if key not in trimmed_keys}
        ordered_subset = {
            "id": data_subset.pop("id"),
            "name": data_subset.pop("name"),
            "original_format": data_subset.pop("original_format"),
            "created_date": data_subset.pop("created_date"),
            **data_subset,
        }
        output += self._pretty_print(ordered_subset)
        return output

    def subset(self):
        trimmed_keys = [
            "id",
            "name",
            "original_format",
            "created_date",
        ]
        data = self.model_dump()
        output = ""
        data_subset = {key: data[key] for key in data if key in trimmed_keys}

        ordered_subset = {
            "id": data_subset.pop("id"),
            "name": data_subset.pop("name"),
            "original_format": data_subset.pop("original_format"),
            **data_subset,
        }
        output += self._pretty_print(ordered_subset)
        return output

    model_config = ConfigDict(extra="ignore", from_attributes=False)


class OptimizationBQM(Optimization, BQMSchema): ...


class OptimizationCQM(Optimization, CQMSchema): ...


class OptimizationLP(Optimization, LPSchema): ...


class OptimizationUseCase(Optimization, QuboSchema):
    use_case: Dict[str, Any]


class OptimizationQubo(Optimization, QuboSchema): ...


T = TypeVar("T")


class OptimizationCreate(BaseModel, Generic[T]):
    """Pydantic model for optimization coming IN."""

    instance: T
