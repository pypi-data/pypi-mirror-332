import json
from datetime import datetime
from typing import Dict, List, Optional

from httpx import Response
from pydantic import TypeAdapter

from luna_sdk.interfaces.qpu_token_repo_i import IQpuTokenRepo
from luna_sdk.schemas import QpuTokenOut
from luna_sdk.schemas.create import QpuTokenIn, QpuTokenTimeQuotaIn
from luna_sdk.schemas.enums.qpu_token_type import QpuTokenTypeEnum
from luna_sdk.schemas.qpu_token_time_quota import QpuTokenTimeQuotaOut

_ORGANIZATION_QPU_TOKENS_BACKEND = "shared"
_PERSONAL_QPU_TOKENS_BACKEND = "private"


class QpuTokenRepo(IQpuTokenRepo):
    @property
    def _endpoint(self) -> str:
        return "/qpu-tokens"

    def _get_endpoint_by_type(
        self, token_type: Optional[QpuTokenTypeEnum] = None
    ) -> str:
        if token_type is None:
            return f"{self._endpoint}"
        elif token_type == QpuTokenTypeEnum.PERSONAL:
            return f"{self._endpoint}/{_PERSONAL_QPU_TOKENS_BACKEND}"
        else:
            return f"{self._endpoint}/{_ORGANIZATION_QPU_TOKENS_BACKEND}"

    def _get_by_name(
        self, name: str, token_type: QpuTokenTypeEnum, **kwargs
    ) -> QpuTokenOut:
        response: Response = self._client.get(
            f"{self._get_endpoint_by_type(token_type)}/{name}", **kwargs
        )
        response.raise_for_status()

        qpu_token_data = response.json()
        qpu_token_data["token_type"] = token_type
        return QpuTokenOut.model_validate(qpu_token_data)

    def create(
        self,
        name: str,
        provider: str,
        token: str,
        token_type: QpuTokenTypeEnum,
        **kwargs,
    ) -> QpuTokenOut:
        qpu_token = QpuTokenIn(
            name=name,
            provider=provider,
            token=token,
        )

        response: Response = self._client.post(
            self._get_endpoint_by_type(token_type),
            content=qpu_token.model_dump_json(),
            **kwargs,
        )
        response.raise_for_status()
        qpu_token_data = response.json()
        qpu_token_data["token_type"] = token_type
        return QpuTokenOut.model_validate(qpu_token_data)

    def get_all(
        self,
        filter_provider: Optional[str] = None,
        token_type: Optional[QpuTokenTypeEnum] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs,
    ) -> Dict[QpuTokenTypeEnum, List[QpuTokenOut]]:
        params = {}
        if filter_provider:
            params["filter_provider"] = filter_provider

        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        if token_type == QpuTokenTypeEnum.PERSONAL:
            params["token_type"] = _PERSONAL_QPU_TOKENS_BACKEND
        if token_type == QpuTokenTypeEnum.GROUP:
            params["token_type"] = _ORGANIZATION_QPU_TOKENS_BACKEND

        response = self._client.get(
            self._endpoint,
            params=params,
            **kwargs,
        )
        ta = TypeAdapter(List[QpuTokenOut])
        to_return: Dict[QpuTokenTypeEnum, List[QpuTokenOut]] = {}
        resp = response.json()

        shared_tokens = resp.get(_ORGANIZATION_QPU_TOKENS_BACKEND, [])
        for qpu_token in shared_tokens:
            qpu_token["token_type"] = QpuTokenTypeEnum.GROUP
        to_return[QpuTokenTypeEnum.GROUP] = ta.validate_python(shared_tokens)

        personal_tokens = resp.get(_PERSONAL_QPU_TOKENS_BACKEND, [])
        for qpu_token in personal_tokens:
            qpu_token["token_type"] = QpuTokenTypeEnum.PERSONAL
        to_return[QpuTokenTypeEnum.PERSONAL] = ta.validate_python(personal_tokens)

        return to_return

    def get(
        self,
        name: str,
        token_type: QpuTokenTypeEnum = QpuTokenTypeEnum.PERSONAL,
        **kwargs,
    ) -> QpuTokenOut:
        qpu_token: QpuTokenOut = self._get_by_name(name, token_type, **kwargs)

        return qpu_token

    def rename(
        self, name: str, new_name: str, token_type: QpuTokenTypeEnum, **kwargs
    ) -> QpuTokenOut:
        qpu_token_update_data = {"name": new_name}

        token: QpuTokenOut = self.get(name, token_type)

        response = self._client.patch(
            f"{self._get_endpoint_by_type(token_type)}/{token.name}",
            content=json.dumps(qpu_token_update_data),
            **kwargs,
        )
        response.raise_for_status()

        qpu_token_data = response.json()
        qpu_token_data["token_type"] = token_type
        return QpuTokenOut.model_validate(qpu_token_data)

    def delete(self, name: str, token_type: QpuTokenTypeEnum, **kwargs) -> None:
        response = self._client.delete(
            f"{self._get_endpoint_by_type(token_type)}/{name}", **kwargs
        )
        response.raise_for_status()

    def create_group_time_quota(
        self,
        qpu_token_name: str,
        quota: int,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        **kwargs,
    ) -> None:
        time_quota = QpuTokenTimeQuotaIn(quota=quota, start=start, end=end)

        endpoint = self._get_endpoint_by_type(QpuTokenTypeEnum.GROUP)
        response = self._client.post(
            f"{endpoint}/quota/group/{qpu_token_name}",
            content=time_quota.model_dump_json(),
            **kwargs,
        )
        response.raise_for_status()

    def get_group_time_quota(
        self, qpu_token_name: str, **kwargs
    ) -> Optional[QpuTokenTimeQuotaOut]:
        endpoint = self._get_endpoint_by_type(QpuTokenTypeEnum.GROUP)
        response = self._client.get(
            f"{endpoint}/quota/group/{qpu_token_name}", **kwargs
        )
        response.raise_for_status()

        time_quota_data = response.json()

        if time_quota_data is None:
            return None
        return QpuTokenTimeQuotaOut.model_validate(time_quota_data)

    def update_group_time_quota(
        self,
        qpu_token_name: str,
        quota: Optional[int] = None,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        **kwargs,
    ) -> None:
        data = {"quota": quota, "start": start, "end": end}

        endpoint = self._get_endpoint_by_type(QpuTokenTypeEnum.GROUP)
        response = self._client.patch(
            f"{endpoint}/quota/group/{qpu_token_name}",
            content=json.dumps(data),
            **kwargs,
        )
        response.raise_for_status()

    def delete_group_time_quota(self, qpu_token_name: str, **kwargs) -> None:
        endpoint = self._get_endpoint_by_type(QpuTokenTypeEnum.GROUP)
        response = self._client.delete(
            f"{endpoint}/quota/group/{qpu_token_name}",
            **kwargs,
        )
        response.raise_for_status()

    def create_user_time_quota(
        self,
        qpu_token_name: str,
        user_email: str,
        quota: int,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        **kwargs,
    ) -> None:
        time_quota = QpuTokenTimeQuotaIn(quota=quota, start=start, end=end)

        endpoint = self._get_endpoint_by_type(QpuTokenTypeEnum.GROUP)
        response = self._client.post(
            f"{endpoint}/quota/user/{qpu_token_name}/{user_email}",
            content=time_quota.model_dump_json(),
            **kwargs,
        )
        response.raise_for_status()

    def get_user_time_quota(
        self, qpu_token_name: str, user_email: str, **kwargs
    ) -> Optional[QpuTokenTimeQuotaOut]:
        endpoint = self._get_endpoint_by_type(QpuTokenTypeEnum.GROUP)
        response = self._client.get(
            f"{endpoint}/quota/user/{qpu_token_name}/{user_email}", **kwargs
        )
        response.raise_for_status()

        time_quota_data = response.json()

        if time_quota_data is None:
            return None
        return QpuTokenTimeQuotaOut.model_validate(time_quota_data)

    def update_user_time_quota(
        self,
        qpu_token_name: str,
        user_email: str,
        quota: Optional[int] = None,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        **kwargs,
    ) -> None:
        data = {"quota": quota, "start": start, "end": end}

        endpoint = self._get_endpoint_by_type(QpuTokenTypeEnum.GROUP)
        response = self._client.patch(
            f"{endpoint}/quota/user/{qpu_token_name}/{user_email}",
            content=json.dumps(data),
            **kwargs,
        )
        response.raise_for_status()

    def delete_user_time_quota(
        self, qpu_token_name: str, user_email: str, **kwargs
    ) -> None:
        endpoint = self._get_endpoint_by_type(QpuTokenTypeEnum.GROUP)
        response = self._client.delete(
            f"{endpoint}/quota/user/{qpu_token_name}/{user_email}",
            **kwargs,
        )
        response.raise_for_status()
