# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ParamCreateParams"]


class ParamCreateParams(TypedDict, total=False):
    validation_columns: Required[List[str]]
    """The columns to be used in validation"""

    validation_name: Required[str]
    """The name of the validation operation"""

    validation_endpoint: str
    """The URL of the validation API.

    If not provided, the validation_rule will be ran directly.
    """

    validation_rule: str
    """The rules to be applied to the column"""

    api_version: Annotated[str, PropertyInfo(alias="API-Version")]
    """
    Pass in an API version to guarantee a consistent response format.The latest
    version should be used for all new API calls. Existing API calls should be
    updated to the latest version when possible.

    **Valid versions:**

    - Latest API version (recommended): `2025-03`

    - Previous API version (maintenance mode): `2025-02`

    If no API version header is included, the response format is considered unstable
    and could change without notice (not recommended).
    """
