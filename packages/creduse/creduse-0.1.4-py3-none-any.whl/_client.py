import os

from pydantic import UUID4
from .models.response_models import (
    AddCreditModel,
    ActiveBalance,
    CycleModelResponse,
    SubtractCreditModel,
    StartCycleModel,
    StopCycleModel,
    GetBalanceRequest,
)
from ._httpclient import SyncHttpClient, AsyncHttpClient


class CreduseClient:
    def __init__(
        self, api_key: str | None = None, http_client: SyncHttpClient | None = None
    ) -> None:
        if api_key is None:
            api_key = os.environ.get("CREDUSE_API_KEY")
        if api_key is None:
            raise ValueError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CREDUSE_API_KEY environment variable"
            )
        self.api_key = api_key
        self.http_client = (
            SyncHttpClient(self.api_key) if http_client is None else http_client
        )

    def add(
        self, end_user_id: UUID4, amount: int, validity_days: int = 31
    ) -> AddCreditModel:
        if amount < 0:
            raise ValueError("Amount must be positive")
        if validity_days < 0:
            raise ValueError("Validity days must be positive")
        body = AddCreditModel(
            end_user_id=end_user_id, amount=amount, validity_days=validity_days
        ).model_dump(mode="json")
        json_response = self.http_client.post("/add", body)
        return AddCreditModel(**json_response)

    def subtract(self, end_user_id: UUID4, amount: int) -> SubtractCreditModel:
        if amount < 0:
            raise ValueError("Amount must be positive")
        body = SubtractCreditModel(end_user_id=end_user_id, amount=amount).model_dump(
            mode="json"
        )
        response = self.http_client.post("/subtract", body)
        return SubtractCreditModel(**response)

    def start_cycle(
        self, end_user_id: UUID4, amount: int, validity_days: int = 31
    ) -> StartCycleModel:
        if amount < 0:
            raise ValueError("Amount must be positive")
        if validity_days < 0:
            raise ValueError("Validity days must be positive")
        json_body = StartCycleModel(
            end_user_id=end_user_id, amount=amount, validity_days=validity_days
        ).model_dump(mode="json")
        response = self.http_client.post("/start-cycle", json_body)
        return CycleModelResponse(**response)

    def stop_cycle(self, end_user_id: UUID4) -> StopCycleModel:
        json_body = StopCycleModel(end_user_id=end_user_id).model_dump(mode="json")
        response = self.http_client.post("/stop-cycle", json_body)
        return CycleModelResponse(**response)

    def get_balance(self, end_user_id: UUID4) -> ActiveBalance:
        body = GetBalanceRequest(end_user_id=end_user_id).model_dump(mode="json")
        response = self.http_client.get("/get-active-balance", body)
        return ActiveBalance(**response)


class AsyncCreduseClient:
    def __init__(self, api_key: str | None = None, http_client=None) -> None:
        if api_key is None:
            api_key = os.environ.get("CREDUSE_API_KEY")
        if api_key is None:
            raise ValueError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CREDUSE_API_KEY environment variable"
            )
        self.api_key = api_key
        self.http_client = (
            AsyncHttpClient(self.api_key) if http_client is None else http_client
        )

    async def add(
        self, end_user_id: UUID4, amount: int, validity_days: int = 31
    ) -> AddCreditModel:
        if amount < 0:
            raise ValueError("Amount must be positive")
        if isinstance(amount, float):
            raise TypeError("Amount must be an integer")
        if validity_days < 0:
            raise ValueError("Validity days must be positive")
        body = AddCreditModel(
            end_user_id=end_user_id, amount=amount, validity_days=validity_days
        ).model_dump(mode="json")
        json_response = await self.http_client.post("/add", body)
        return AddCreditModel(**json_response)

    async def subtract(self, end_user_id: UUID4, amount: int) -> SubtractCreditModel:
        if amount < 0:
            raise ValueError("Amount must be positive")
        body = SubtractCreditModel(end_user_id=end_user_id, amount=amount).model_dump(
            mode="json"
        )
        response = await self.http_client.post("/subtract", body)
        return SubtractCreditModel(**response)

    async def start_cycle(
        self, end_user_id: UUID4, amount: int, validity_days: int = 31
    ) -> StartCycleModel:
        if amount < 0:
            raise ValueError("Amount must be positive")
        if validity_days < 0:
            raise ValueError("Validity days must be positive")
        json_body = StartCycleModel(
            end_user_id=end_user_id, amount=amount, validity_days=validity_days
        ).model_dump(mode="json")
        response = await self.http_client.post("/start-cycle", json_body)
        return CycleModelResponse(**response)

    async def stop_cycle(self, end_user_id: UUID4) -> CycleModelResponse:
        json_body = StopCycleModel(end_user_id=end_user_id).model_dump(mode="json")
        response = await self.http_client.post("/stop-cycle", json_body)
        return CycleModelResponse(**response)

    async def get_balance(self, end_user_id: UUID4) -> ActiveBalance:
        body = GetBalanceRequest(end_user_id=end_user_id).model_dump(mode="json")
        response = await self.http_client.get("/get-active-balance", body)
        return ActiveBalance(**response)
