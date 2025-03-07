# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["TransformDuplicateResponse", "Data"]


class Data(BaseModel):
    transform_id: str

    operations: Optional[Dict[str, str]] = None


class TransformDuplicateResponse(BaseModel):
    data: Data

    message: str
