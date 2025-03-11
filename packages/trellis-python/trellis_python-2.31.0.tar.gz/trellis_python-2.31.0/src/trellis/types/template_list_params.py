# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    category_id: str
    """Category id (optional)"""

    owned_only: bool
    """Include only templates owned by you.

    If false, only templates from others are included.
    """

    template_ids: List[str]
    """List of template ids (optional). Takes priority over category_id"""

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
