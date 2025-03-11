from __future__ import annotations

from typing import Any, Literal, overload

from httpx import AsyncClient

from jkit._base import CredentialObject
from jkit._codec import JSON_DECODER, JSON_ENCODER
from jkit.config import CONFIG, _DatasourceNameType
from jkit.constants import _RATELIMIT_STATUS_CODE
from jkit.exceptions import RatelimitError

HttpMethodType = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]

DATASOURCE_CLIENTS: dict[_DatasourceNameType, AsyncClient] = {
    "JIANSHU": CONFIG.datasources.jianshu._get_httpx_client(),
    "JPEP": CONFIG.datasources.jpep._get_httpx_client(),
    "BEIJIAOYI": CONFIG.datasources.beijiaoyi._get_httpx_client(),
}


@overload
async def send_request(
    *,
    datasource: _DatasourceNameType,
    method: HttpMethodType,
    path: str,
    params: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None,
    credential: CredentialObject | None = None,
    response_type: Literal["JSON"],
) -> dict[str, Any]: ...


@overload
async def send_request(
    *,
    datasource: _DatasourceNameType,
    method: HttpMethodType,
    path: str,
    params: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None,
    credential: CredentialObject | None = None,
    response_type: Literal["JSON_LIST"],
) -> list[dict[str, Any]]: ...


@overload
async def send_request(
    *,
    datasource: _DatasourceNameType,
    method: HttpMethodType,
    path: str,
    params: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None,
    credential: CredentialObject | None = None,
    response_type: Literal["HTML"],
) -> str: ...


@overload
async def send_request(
    *,
    datasource: _DatasourceNameType,
    method: HttpMethodType,
    path: str,
    params: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None,
    credential: CredentialObject | None = None,
    response_type: None,
) -> None: ...


async def send_request(  # noqa: PLR0913
    *,
    datasource: _DatasourceNameType,
    method: HttpMethodType,
    path: str,
    params: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None,
    credential: CredentialObject | None = None,
    response_type: Literal["JSON", "JSON_LIST", "HTML"] | None,
) -> dict[str, Any] | list[dict[str, Any]] | str | None:
    client = DATASOURCE_CLIENTS[datasource]

    headers = {"Accept": "text/html" if response_type == "HTML" else "application/json"}
    if body is not None:
        headers["Content-Type"] = "application/json"

    if credential:
        headers.update(credential.headers)

    response = await client.request(
        method=method,
        url=path,
        params=params,
        content=JSON_ENCODER.encode(body) if body else None,
        headers=headers,
    )

    if datasource == "JIANSHU" and response.status_code == _RATELIMIT_STATUS_CODE:
        raise RatelimitError

    response.raise_for_status()

    if response_type in {"JSON", "JSON_LIST"}:
        return JSON_DECODER.decode(response.content)
    if response_type == "HTML":
        return response.text
    return None
