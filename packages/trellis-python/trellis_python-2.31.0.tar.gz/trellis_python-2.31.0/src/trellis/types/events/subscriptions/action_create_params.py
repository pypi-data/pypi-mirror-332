# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ActionCreateParams", "Action"]


class ActionCreateParams(TypedDict, total=False):
    actions: Required[Iterable[Action]]

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


class Action(TypedDict, total=False):
    type: Required[Literal["refresh_transform", "run_extraction", "send_webhook"]]
    """An enumeration."""

    proj_id: str
    """Project ID to run the action on.

    Required for `run_extraction` and `send_webhook`. Either `proj_id` or
    `transform_id` must be present, but not both.
    """

    transform_id: str
    """Transformation ID to run the action on.

    Required for `refresh_transform`. Either `proj_id` or `transform_id` must be
    present, but not both.
    """

    webhook_id: str
    """Webhook ID to call. Only used when `send_webhook` is set as `type`"""
