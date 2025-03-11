# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    event_type: Required[Literal["asset_extracted", "asset_uploaded", "transform_completed"]]
    """An enumeration."""

    proj_id: str
    """Project ID for the event subscription.

    Either proj_id or transform_id must be present.
    """

    transform_id: str
    """Transformation ID for the event subscription.

    Either proj_id or transform_id must be present.
    """

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
