# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetsExtractExtractParams"]


class AssetsExtractExtractParams(TypedDict, total=False):
    asset_ids: List[str]
    """Optional. Asset IDs to run extraction on. Overrides transform_id."""

    blocking: bool
    """Optional, defaults to False.

    If True, a response will come back after at most 120 seconds with the extracted
    values.
    """

    parse_strategy: Literal["optimized", "ocr", "xml", "markdown", "advanced_markdown"]
    """Enum representing different parsing strategies.

    Note that OCR and XML will be deprecated soon.
    """

    transform_id: str
    """Optional. Transformation ID of the transform housing the assets to extract."""

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
